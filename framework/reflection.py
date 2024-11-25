from dataclasses import dataclass
from typing import Optional
from openai import OpenAI

@dataclass
class SanityCheckReflection:
    """SanityCheckReflection is used to generate debug suggestion for the code based on check list"""

    def __init__(self, ctx):
        self.oai_model = ctx.openai_model
        self.oai_temperature = ctx.openai_temperature
        self.ref_client = OpenAI(api_key=ctx.openai_api_key, base_url=ctx.openai_base_url)
        self.analyzer = ctx.result_analyzer
        self.logger = ctx.logger

        # Python Error Check List - common error types to handle
        self.py_err_check_list = [
            # ImportError,
            # ModuleNotFoundError,
            SyntaxError, 
            NameError,
            TypeError,
            ValueError,
            AttributeError,
            IndexError,
            KeyError,
            ZeroDivisionError,
            RuntimeError
        ]

    def _should_reflect(self, err: Exception) -> bool:
        """Check if the error type is in the predefined checklist"""
        return any(isinstance(err, err_type) for err_type in self.py_err_check_list)

    def get_reflection_prompt(self, code_snippet: str, err: Exception) -> Optional[str]:
        """Generate debug message if error type is in checklist"""
        
        # Check if we should handle this error type
        if not self._should_reflect(err):
            self.logger.info(f"Error type {type(err).__name__} not in checklist, skipping reflection")
            return None
        
        # Build the prompt with code and error context
        prompt = f"\n\n### Previous code attempt ###\n```python\n{code_snippet}\n```"
        prompt += f"\n\n### Runtime error ###\n{type(err).__name__}: {str(err)}\n"
        
        if prompt:
            prompt += "\nAnalyze the code and error message above. Provide a clear and concise debug suggestion. Format your response with '### Debug ###' followed by your suggestion."

        messages = [
            {"role": "system", "content": "You are a Python code debugger. Provide clear and actionable debug suggestions."},
            {"role": "user", "content": prompt}
        ]

        completion = self.ref_client.chat.completions.create(
            model=self.oai_model,
            messages=messages,
            temperature=self.oai_temperature
        )
        
        response = completion.choices[0].message.content
        self.logger.info(f"Reflection token usage: Prompt: {completion.usage.prompt_tokens}, Completion: {completion.usage.completion_tokens}")

        self.analyzer.add_token_usage("reflection", completion.usage.prompt_tokens, completion.usage.completion_tokens)

        return f'\n\n{response}\n\nYou can use the above debug message to improve your code.'

