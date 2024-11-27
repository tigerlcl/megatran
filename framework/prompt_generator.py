class PromptMaker:
    """
    PromptMaker generates prompts for LLMs by combining different components:
    - chat: User's natural language instruction
    - ctx: Input/output context information  
    - example: Example input/output pairs
    
    Example modes:
    - "chat": Only instruction
    - "chat_ctx": Instruction with context
    - "chat_example": Instruction with examples
    - "chat_ctx_example": Full prompt with all components
    """
    
    # Component keywords
    CHAT: str = "chat"
    CTX: str = "ctx" 
    EXAMPLE: str = "example"
    CODE:str = "code"

    def __init__(self, mode: str, n_shot: int):
        self.mode = mode
        self.n_shot = n_shot

    def get_prompt_by_mode(self, item: dict) -> str:
        """
        Generate prompt based on mode and item data
        
        Args:
            item (dict): Dataset item containing:
                - chat: Instruction text
                - context: Input/output format
                - tuples: Example pairs
                
        Returns:
            str: Formatted prompt text
        """
        query = ""

        # Code LLM
        if self.CODE in self.mode:
            query += f"### Instruction ###\nWrite function to transform the input data into the desired output"

        # add instruction
        if self.CHAT in self.mode:
            query += f"### Instruction ###\n{item['chat']}"
        
        # add context
        if self.CTX in self.mode:
            item_ctx = f'Input: {item["context"]["input"]}\nOutput: {item["context"]["output"]}'
            query += f"\n\n### Context ###\n{item_ctx}"
        
        # add examples
        if self.EXAMPLE in self.mode:
            item_examples = '\n'.join([f'Input: {example["input"]}\nOutput: {example["output"]}' 
                                                for example in item["tuples"][:self.n_shot]])
            query += f"\n\n### Examples ###\n{item_examples}"

        return query
