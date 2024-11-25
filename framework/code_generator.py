import os
import re
import importlib
from openai import OpenAI

from .prompt_generator import PromptMaker
from .lazy_rag import LazyRAG
from .reflection import SanityCheckReflection

import temp.code_solution # temp code holder, it will be empty at first

class CodeGenerator:
    """
    CodeGenerator handles code generation and execution:
    1. Generates code based on instructions (if chat_to_inst is enabled)
    2. Executes generated code in a controlled environment
    3. Integrates with LazyRAG for API documentation lookup
    4. Integrates with Reflection for error handling and code improvement

    """
    def __init__(self, ctx):
        """Initialize CodeGenerator with context"""

        self.code_dir = ctx.code_dir
        self.code_n_shot = ctx.n_shot
        self.code_attempt = ctx.code_attempt
        self.logger = ctx.logger
        self.analyzer = ctx.result_analyzer

        self.oai_model = ctx.openai_model
        self.oai_temperature = ctx.openai_temperature
        self.oai_client = OpenAI(api_key=ctx.openai_api_key, base_url=ctx.openai_base_url)
        self.prompt_maker = PromptMaker(ctx.prompt_mode, ctx.n_shot)
        self.temp_python_fp = os.path.join(ctx.temp_dir, "code_solution.py")
        
        if ctx.allow_reflection:
            self.reflection = SanityCheckReflection(ctx)
            self.logger.info("Reflection enabled")

        if ctx.allow_rag:
            self.lazy_rag = LazyRAG(ctx)
            self.logger.info("Lazy RAG enabled")


        # regexes
        self.py_block = r'```python\n(.*?)\n```'
        self.func_def = r'def\s+solution\s*\('

        # Check if the OpenAI backend client is connected
        try:
            self.oai_client.chat.completions.create(
                model=self.oai_model,
                messages=[{"role": "user", "content": "Test connection"}],
                temperature=self.oai_temperature
            )
            self.logger.info(f"Code Generator: OpenAI backend connected")
        except Exception:
            raise RuntimeError("Failed to connect to the OpenAI client, please check your config.")

    def _generate_code(self, item: dict) -> str:
        """Generate Python code based on the instruction"""
        # Get base prompt
        prompt = self.prompt_maker.get_prompt_by_mode(item)
        
        # append last attempt
        if self.last_attempt:
            prompt += f"\n\n### Last Coding Attempt ###\n{self.last_attempt}"
        
        # append reflection prompt if enabled
        if self.reflection_prompt:
            prompt += self.reflection_prompt

        # append RAG prompt if enabled
        if self.rag_prompt:
            prompt += self.rag_prompt

        self.logger.info(f"Code generation query:\n{prompt}")
        
        messages = [
            {"role": "system", "content": "You are a Python code generator based on the given instruction."},
            {"role": "user", "content": f"{prompt}\n\nYou are required to write an executable function that performs the task. The function input and output are both string. You must format the python code as below:\n\n```python\ndef solution(input):\n    # Coding here...\n    return output\n```"
            }
        ]

        completion = self.oai_client.chat.completions.create(
            model=self.oai_model,
            messages=messages,
            temperature=self.oai_temperature
        )
        response = completion.choices[0].message.content
        self.logger.info(f"Code generation token usage: Prompt: {completion.usage.prompt_tokens}, Completion: {completion.usage.completion_tokens}")
        self.analyzer.add_token_usage("code_generation", completion.usage.prompt_tokens, completion.usage.completion_tokens)

        # Extract the code snippet
        code_match = re.search(self.py_block, response, re.DOTALL)
        if not code_match:
            raise RuntimeError("No Python code block found in the response.")
        
        code_snippet = code_match.group(1)
        if not re.search(self.func_def, code_snippet):
            raise RuntimeError("Generated code does not contain a 'solution' function.")

        # Save the code
        with open(self.temp_python_fp, 'w') as f:
            f.write(code_snippet)
        self.save_code(self.code_dir, item['file_path'], code_snippet)
        
        return code_snippet

    def save_code(self, code_dir, file_path, code_snippet):
        """Save generated code to file"""
        # prepare the code file path
        dir_name, base_name = os.path.split(file_path)
        dir_name = os.path.join(code_dir, dir_name.replace('./data/', ''))
        os.makedirs(dir_name, exist_ok=True)
        
        base_name = f"{os.path.splitext(base_name)[0]}.py"
        code_fp = os.path.join(dir_name, base_name)

        with open(code_fp, 'w') as f:
            f.write(code_snippet)

    # Reload the solution function
    def _reload_func(self):    
        """Reload the solution function from temporary module"""
        importlib.reload(temp.code_solution)  # Reload the module
        from temp.code_solution import solution  # Import the updated solution function
        return solution

    def run(self, item: dict) -> list:
        """Main execution loop with sanity-check reflection and lazy RAG"""
        
        self.logger.info(f"Generating code...")

        # debug with first n examples
        debugs = [{'input': t['input'], 'output': t['output'], 'code_output': None} 
                       for t in item['tuples'][:self.code_n_shot]]

        # test with the rest of the examples
        tests = [{'input': t['input'], 'output': t['output'], 'code_output': None} 
                       for t in item['tuples'][self.code_n_shot:]]
        
        
        # Initialize prompts for each attempt
        self.last_attempt = None
        self.reflection_prompt = None
        self.rag_prompt = None
        
        retry_count = 0
        while retry_count < self.code_attempt:
            try:
                # Try to generate code
                code_snippet = None
                code_snippet = self._generate_code(item)
                self.logger.info("Code generated successfully, running tests...")

                # load the code
                solution_func = self._reload_func()

                # debug the code using the first n examples
                for debug in debugs:
                    debug['code_output'] = solution_func(debug['input'])
                
                    # compare the code output with the expected output
                    if debug['code_output'] != debug['output']:
                        raise RuntimeError(f"Solution output: {debug['code_output']} != expected output: {debug['output']}")

                break # debug cases all passed, no need to retry
            except Exception as e:
                if isinstance(e, (ImportError, ModuleNotFoundError)):
                    self.logger.warning(f"{type(e).__name__}: {str(e)}. Please handle it manually.")
                    break # no more attempt

                # save the last attempt
                self.last_attempt = code_snippet
                
                retry_count += 1
                self.logger.warning(f"Code Generation attempt {retry_count}/{self.code_attempt} failed")

                # Only get reflection and RAG prompts if we have more attempts left
                if retry_count < self.code_attempt:
                    # Sanity check reflection
                    if hasattr(self, 'reflection') and self.reflection:
                        self.reflection_prompt = self.reflection.get_reflection_prompt(code_snippet, e)
                    
                    # Lazy RAG
                    if hasattr(self, 'lazy_rag') and self.lazy_rag:
                        self.rag_prompt = self.lazy_rag.get_rag_prompt(code_snippet)

        # run tests with the rest of the examples (unseen to the framework)
        try:
            for test in tests:
                test['code_output'] = solution_func(test['input'])
        except Exception as e:
            self.logger.error(f"Current task failed: {e}")

        # clean temporary code file content
        with open(self.temp_python_fp, 'w') as f:
            f.write('')
        
        return tests

