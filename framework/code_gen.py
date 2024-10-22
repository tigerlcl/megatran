import os
import re
from openai import OpenAI
from .prompt_generator import CodePrompt

import importlib
import temp.code_solution  # Import the module first

class CodeGenerator:
    def __init__(self, ctx):
        
        self.code_dir = ctx.code_dir
        self.oai_model = ctx.openai_model
        self.logger = ctx.logger

        self.oai_client = OpenAI(**ctx.openai_cfg)
        self.query_generator = CodePrompt(ctx.code_mode)
        
        self.temp_python_fp = os.path.join(ctx.temp_dir, "code_solution.py")
        self.py_block = r"^```python\n|\n```$"
    

    def generate_code(self, item):
        try:
            query = self.query_generator.get_prompt_by_mode(item)
        except ValueError as e:
            self.logger.error(f"Error when generating prompt: {e}")
            return None
        
        messages = [
            {"role": "system", "content": "You are a Python code generator based on the given instruction."},
            {"role": "user", "content": f"{query}\n\nYou are required to write an executable function that performs the task. The function input and output are both string. You must format the python code as below:\n\n```python\ndef solution(input):\n    # Coding here...\n    return output\n```"}
        ]

        completion = self.oai_client.chat.completions.create(
            model=self.oai_model,
            messages=messages,
            temperature=0.2
        )
        response = completion.choices[0].message.content

        # extract the code snippet from the response
        code_snippet = re.sub(self.py_block, "", response, flags=re.MULTILINE)
        isCodeGen = len(code_snippet) > 0

        # Write the function to a temp file for execution
        with open(self.temp_python_fp, 'w') as f:
            f.write(code_snippet)

        # store a copy of the code snippet in the code_fp
        self.save_code(self.code_dir, item['file_path'], code_snippet)

        return isCodeGen

    
    def save_code(self, code_dir, file_path, code_snippet):
        # prepare the code file path
        dir_name, base_name = os.path.split(file_path)
        dir_name = os.path.join(code_dir, dir_name.replace('./data/', ''))
        os.makedirs(dir_name, exist_ok=True)
        
        base_name = os.path.splitext(base_name)[0] + '.py'
        code_fp = os.path.join(dir_name, base_name)

        with open(code_fp, 'w') as f:
            f.write(code_snippet)

    def execute_code(self, tests):
        solution_func = self._reload_func()

        for t in tests:
            try:
                func_output = solution_func(t['input'])
            except Exception:
                func_output = None
            
            t['code_output'] = func_output

        # Add code execution result
        return tests

    # Reload the solution function
    def _reload_func(self):
        importlib.reload(temp.code_solution)  # Reload the module
        from temp.code_solution import solution  # Import the updated solution function
        return solution


    def run(self, item):
        self.logger.info(f"Generating code for {item['file_path']}")
        try:
            isCodeGen = self.generate_code(item)
        except Exception as e:
            self.logger.error(f"Error when generating code: {e}")
            isCodeGen = False
        
        # Execute code and evaluate result
        tests = item['tuples']
        if isCodeGen:
            try:
                tests = self.execute_code(tests)
            except Exception as e:
                self.logger.error(f"Error when executing code: {e}")
        
        return tests









