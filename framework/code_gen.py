import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class CodeGenerator:
    def __init__(self, cfg):
        self.temp_python_fp = cfg["temp_python_file"]
        self.py_block = r"^```python\n|\n```$"

        self.llm = ChatOpenAI(
            model_name=cfg["model_name"],
            api_key=cfg["api_key"],
            temperature=0.2,  # pre-set now
        )

    def run(self, instruction, code_fp):
        prompt_template = """You are a Python code generator.
You are given an instruction, which is a description of a task.

{inst}

You are required to write an executable function that performs the task.
The function input is string. You must format the python code as below:
```python
def solution(input):
    # Coding here...
    return output
```    
"""

        prompt = ChatPromptTemplate.from_template(prompt_template)
        llm_chain = prompt | self.llm
        llm_response = llm_chain.invoke({"inst": instruction})
        code_snippet = re.sub(self.py_block, "", llm_response.content, flags=re.MULTILINE)

        isCodeGen = len(code_snippet) > 0

        # Write the function to a temp file for execution
        with open(self.temp_python_fp, 'w') as f:
            f.write(code_snippet)

        # store a copy of the code snippet in the code_fp
        with open(code_fp, 'w') as f:
            f.write(code_snippet)

        return isCodeGen, llm_response.response_metadata['token_usage']











