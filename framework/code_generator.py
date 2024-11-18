import os
import re
import importlib
from openai import OpenAI
from typing import Optional

from .lazy_rag import LazyRAG
from .prompt_generator import PromptMaker
from .reflection import ReflectionCtx
import temp.code_solution # temp code holder, it will be empty at first


class CodeGenerator:
    """
    CodeGenerator handles code generation and execution:
    1. Generates code based on instructions using LLM
    2. Executes generated code in a controlled environment
    3. Integrates with LazyRAG for API documentation lookup
    4. Handles import errors and package dependencies
    
    Workflow:
    1. Get prompt from PromptMaker
    2. Retrieve relevant docs from LazyRAG if needed
    3. Generate code using LLM
    4. Execute code and return results
    """
    def __init__(self, ctx):
        """
        Initialize CodeGenerator with context
        Args:
            ctx: Context object containing:
                - code_dir: Directory for saving generated code
                - openai_model: Model name for code generation
                - logger: Logging instance
                - n_shot: Number of examples to use
                - openai_cfg: OpenAI API configuration
                - temp_dir: Directory for temporary python script
        """
        self.code_dir = ctx.code_dir
        self.oai_model = ctx.openai_model
        self.logger = ctx.logger
        self.code_n_shot = ctx.n_shot
        self.code_retry = ctx.code_retry

        self.oai_client = OpenAI(**ctx.openai_cfg)
        self.prompt_maker = PromptMaker(ctx.prompt_mode, ctx.n_shot)
        self.temp_python_fp = os.path.join(ctx.temp_dir, "code_solution.py")
        self.rag = LazyRAG(ctx)
    
        # regexes
        self.py_block = r'```python\n(.*?)\n```'
        self.func_def = r'def\s+solution\s*\('
        self.import_stmt = r'^(import .+|from .+ import .+)'


    def generate_code(self, item: dict, reflection_ctx: Optional[ReflectionCtx] = None) -> str:
        """
        Generate Python code based on the instruction
        
        Args:
            item: Dataset item containing instruction and examples
            reflection_ctx: Optional context from previous attempts
        
        Returns:
            str: Generated code snippet
        
        Raises:
            ValueError: If code generation fails
        """
        # Get base prompt
        prompt = self.prompt_maker.get_prompt_by_mode(item)
        
        # Add reflection context if available
        if reflection_ctx:
            prompt += reflection_ctx.build_reflection_prompt()

        self.logger.info(f"Code generation query:\n{prompt}")
        
        messages = [
            {"role": "system", "content": "You are a Python code generator based on the given instruction."},
            {"role": "user", "content": f"{prompt}\n\nYou are required to write an executable function that performs the task. The function input and output are both string. You must format the python code as below:\n\n```python\ndef solution(input):\n    # Coding here...\n    return output\n```"
            }
        ]

        completion = self.oai_client.chat.completions.create(
            model=self.oai_model,
            messages=messages,
            temperature=0.2
        )
        response = completion.choices[0].message.content
    

        # Extract the code snippet
        code_match = re.search(self.py_block, response, re.DOTALL)
        if not code_match:
            raise ValueError("No Python code block found in the response.")
        
        code_snippet = code_match.group(1)
        if not re.search(self.func_def, code_snippet):
            raise ValueError("Generated code does not contain a 'solution' function.")

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
        
        base_name = os.path.splitext(base_name)[0] + '.py'
        code_fp = os.path.join(dir_name, base_name)

        with open(code_fp, 'w') as f:
            f.write(code_snippet)

    def execute_code(self, tests: list) -> list:
        """Execute generated code with reflection on errors"""
        try:
            solution_func = self._reload_func()
        except ImportError as e:
            self.rag.handle_import_error(e)
            return tests

        for t in tests:
            # runtime error will be captured by the outside try-except block
            func_output = solution_func(t['input'])
            t['code_output'] = func_output

            if func_output != t['output']:
                raise ValueError(f"Test failed: expected {t['output']}, got {func_output}")

        return tests

    # Reload the solution function
    def _reload_func(self):    
        """Reload the solution function from temporary module"""
        importlib.reload(temp.code_solution)  # Reload the module
        from temp.code_solution import solution  # Import the updated solution function
        return solution

    def run(self, item: dict):
        """Main execution loop with reflection and lazy RAG"""
        self.logger.info(f"Generating code for {item['file_path']}...")
        tests = [{'input': t['input'], 'output': t['output'], 'code_output': None} 
                 for t in item['tuples'][self.code_n_shot:]]
        
        reflection_ctx = ReflectionCtx()
        retry_count = 0

        while retry_count < self.code_retry:
            try:
                # Try to generate code
                code_snippet = self.generate_code(item, reflection_ctx)
                self.logger.info("Code generated successfully, running tests...")
                tests = self.execute_code(tests)
                break
            except Exception as e:
                reflection_ctx.code_snippet = code_snippet

                # Update reflection context
                reflection_ctx.runtime_err = str(e)

                # Capture import statements
                import_statements = re.findall(self.import_stmt, code_snippet, re.MULTILINE)
                self.logger.info(f"Captured import statements: {import_statements}")

                reflection_ctx.rag_doc = self.rag.find_pkg_info(import_statements)
                
                retry_count += 1
                self.logger.warning(f"Test attempt {retry_count}/{self.code_retry} failed: {e}")
            
        # clean temporary code file content
        with open(self.temp_python_fp, 'w') as f:
            f.write('')
        
        return tests

