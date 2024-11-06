import os
import re
import importlib
from openai import OpenAI
from typing import List

from .lazy_rag import LazyRAG
from .prompt_generator import PromptMaker  

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
        self.n_shot = ctx.n_shot
        self.oai_client = OpenAI(**ctx.openai_cfg)
        self.query_generator = PromptMaker(ctx.prompt_mode, ctx.n_shot)
        self.temp_python_fp = os.path.join(ctx.temp_dir, "code_solution.py")
        self.py_block = r'```python\n(.*?)\n```'
        self.rag = LazyRAG(ctx)

    def generate_code(self, item, additional_context=None) -> bool:
        """
        Generate Python code based on the instruction
        
        Args:
            item (dict): Dataset item containing instruction and examples
            additional_context (str, optional): Additional documentation context
        
        Returns:
            bool: True if code generation successful, False otherwise
        """
        try:
            query = self.query_generator.get_prompt_by_mode(item)
            if additional_context:
                query += f"\n\nRelevant Documentation:\n{additional_context}"
            self.logger.info(f"Code generation query:\n{query}")
        except ValueError as e:
            self.logger.error(f"Error when generating prompt: {e}")
            return False
        
        messages = [
            {"role": "system", "content": "You are a Python code generator based on the given instruction."},
            {"role": "user", "content": f"{query}\n\nYou are required to write an executable function that performs the task. The function input and output are both string. You must format the python code as below:\n\n```python\ndef solution(input):\n    # Coding here...\n    return output\n```"
            }
        ]

        try:
            completion = self.oai_client.chat.completions.create(
                model=self.oai_model,
                messages=messages,
                temperature=0.2
            )
            response = completion.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Error when generating code: {e}")
            return False

        # Extract the code snippet from the response
        code_match = re.search(self.py_block, response, re.DOTALL)
        if code_match:
            code_snippet = code_match.group(1)
            # Verify that the code snippet contains a function definition
            if re.search(r'def\s+solution\s*\(', code_snippet):
                # Write the function to a temp file for execution
                with open(self.temp_python_fp, 'w') as f:
                    f.write(code_snippet)

                # store a copy of the code snippet in the code_fp
                self.save_code(self.code_dir, item['file_path'], code_snippet)
                return True
            else:
                self.logger.warning("Generated code does not contain a 'solution' function.")
                return False
        else:
            self.logger.warning("No Python code block found in the response.")
            return False

    
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


    def execute_code(self, tests, chat) -> List[dict]:
        """
        Execute generated code against test cases
        
        Args:
            tests (list): List of test cases with input/output pairs
            chat (str): Original chat message for error context
            
        Returns:
            list: Test cases with execution results
            
        Example input:
            tests = [{'input': 'hello', 'output': 'HELLO', 'code_output': None}]
            
        Example output:
            [{'input': 'hello', 'output': 'HELLO', 'code_output': 'HELLO'}]
        """
        try:
            # Attempt to reload the solution function
            solution_func = self._reload_func()
        except ImportError as e:
            # Handle import error with RAG
            self.rag.handle_import_error(e, chat)
            # Try to get relevant documentation
            docs = self.rag.get_function_context(chat)
            if docs:
                # Regenerate code with documentation context
                self.generate_code(tests, additional_context=docs)
                return self.execute_code(tests, chat)  # Retry execution
            return tests
        except Exception as e:
            self.logger.error(f"Code solution error occurred: {e}")
            return tests

        for t in tests:
            try:
                # Call the solution function
                func_output = solution_func(t['input'])
                t['code_output'] = func_output
            except ValueError as e:
                # the value error will be handled in the Sanity Reflection module
                self.logger.error(f"Value error:  {e}")
            except Exception as e:
                self.logger.error(f"Code solution error occurred: {e}")
            
        return tests

    # Reload the solution function
    def _reload_func(self):    
        """Reload the solution function from temporary module"""
        importlib.reload(temp.code_solution)  # Reload the module
        from temp.code_solution import solution  # Import the updated solution function
        return solution

    def run(self, item) -> List[dict]:
        """
        Main execution method - generates and tests code
        
        Args:
            item (dict): Dataset item containing:
                - file_path: Path to test file
                - tuples: List of test cases
                - chat: Original instruction
                
        Returns:
            list: Test cases with execution results
            
        Example:
            tests = generator.run({
                'file_path': 'test1.json',
                'tuples': [{'input': 'hello', 'output': 'HELLO'}],
                'chat': 'Convert to uppercase'
            })
        """
        # prepare test, skip the few shot examples
        tests = [{'input': t['input'], 'output': t['output'], 'code_output': None} for t in item['tuples'][self.n_shot:]]
        self.logger.info(f"Generating code for {item['file_path']}")
        
        if self.generate_code(item):
            self.logger.info(f"Generation done, executing code...")
            tests = self.execute_code(tests, item['file_path'])
            
            # clear the content of temp file
            with open(self.temp_python_fp, 'w') as f:
                f.write('')
        
        return tests

