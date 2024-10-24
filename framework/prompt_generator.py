# TODO: Merge ChatPrompt and CodePrompt, extend the 'chat' with 'inst'

class PromptMaker:
    """
    PromptMaker is used to generate the prompt for LLM.

    e.g., mode = "chat_ctx_example", then the prompt will be:
    "### Instruction ###\n{chat}\n\n### Context ###\n{ctx}\n\n### Examples ###\n{example}"
    """
    # keywords
    CHAT: str = "chat"
    CTX: str = "ctx"
    EXAMPLE: str = "example"
    

    def __init__(self, mode: str, n_shot: int):
        self.mode = mode
        self.n_shot = n_shot

    def get_prompt_by_mode(self, item: dict):
        query = ""

        # add instruction
        if self.CHAT in self.mode and self.CHAT in item:
            query += f"### Instruction ###\n{item['chat']}"
        
        # add context
        if self.CTX in self.mode and self.CTX in item:
            item_ctx = f'Input: {item["context"]["input"]}\nOutput: {item["context"]["output"]}'
            query += f"\n\n### Context ###\n{item_ctx}"
        
        # add examples
        if self.EXAMPLE in self.mode: #and self.EXAMPLE in item: temp
            item_examples = '\n'.join([f'Input: {example["input"]}\nOutput: {example["output"]}' 
                                                for example in item["tuples"][:self.n_shot]])
            query += f"\n\n### Examples ###\n{item_examples}"

        if not query:
            raise ValueError(f"Invalid query mode: {self.mode}")

        return query
