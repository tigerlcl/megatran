from dataclasses import dataclass
from typing import Optional

@dataclass
class ReflectionCtx:
    """
    ReflectionCtx stores context for code generation reflection:
    - code_snippet: Previously generated code (may have failed)
    - runtime_err: Error message from code execution
    - rag_doc: Retrieved documentation from RAG
    
    This context helps GPT understand and fix issues in generated code.
    """
    code_snippet: Optional[str] = None
    runtime_err: Optional[str] = None
    rag_doc: Optional[str] = None
    
    def build_reflection_prompt(self) -> str:
        """
        Build reflection prompt from available context
        
        Returns:
            str: Formatted reflection context for prompt
        """
        prompt = ""
        
        if self.code_snippet:
            prompt += f"\n\n### Previous code attempt ###\n```python\n{self.code_snippet}\n```"
            
        if self.runtime_err:
            prompt += f"\n\n### Runtime error ###\n{self.runtime_err}"
            
        if self.rag_doc:
            prompt += f"\n\n### Relevant Documentation ###\n{self.rag_doc}"
            
        if prompt:
            prompt += "\n\nPlease reflect on the previous attempt and errors to generate improved code."
            
        return prompt


