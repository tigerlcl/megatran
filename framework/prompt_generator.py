
class ChatPrompt:
    """
    ChatPrompt is used to generate the prompt for the chat-to-instruction task.
    """

    CHAT: str = "chat"
    CTX: str = "ctx"
    EXAMPLE: str = "example"
    CHAT_CTX: str = "chat_ctx"
    CHAT_EXAMPLE: str = "chat_example"
    CTX_EXAMPLE: str = "ctx_example"
    CHAT_CTX_EXAMPLE: str = "chat_ctx_example"

    def __init__(self, mode: str, n_shot: int):
        self.mode = mode
        self.n_shot = n_shot

    def get_prompt_by_mode(self, item: dict):
        item_ctx = f'Input: {item["context"]["input"]}\nOutput: {item["context"]["output"]}'
    
        tuple_shots = item["tuples"][:self.n_shot]
        item_examples = '\n'.join([f'Input: {example["input"]}\nOutput: {example["output"]}' 
                                                for example in tuple_shots])

        if self.mode == self.CHAT:
            new_query = f"### Instruction ###\n{item['chat']}"
        elif self.mode == self.CHAT_CTX:
            new_query = f"### Instruction ###\n{item['chat']}\n\n### Context ###\n{item_ctx}"
        elif self.mode == self.EXAMPLE:
            new_query = f"### Examples ###\n{item_examples}"
        elif self.mode == self.CHAT_EXAMPLE:
            new_query = f"### Instruction ###\n{item['chat']}\n\n### Examples ###\n{item_examples}"
        else:
            raise ValueError(f"Invalid query mode: {self.mode}")

        return new_query


class CodePrompt:
    """
    CodePrompt is used to generate the prompt for the code generation task.
    """

    CHAT: str = "chat"
    INST: str = "inst"
    INST_EXAMPLE: str = "inst_example"
    INST_CTX: str = "inst_ctx"
    INST_CTX_EXAMPLE: str = "inst_ctx_example"

    def __init__(self, mode: str, n_shot: int):
        self.mode = mode
        self.n_shot = n_shot

    def get_prompt_by_mode(self, item: dict):
        item_ctx = f'Input: {item["context"]["input"]}\nOutput: {item["context"]["output"]}'
    
        tuple_shots = item["tuples"][:self.n_shot]
        item_examples = '\n'.join([f'Input: {example["input"]}\nOutput: {example["output"]}' 
                                                for example in tuple_shots])

        if self.mode == self.CHAT:
            new_query = f"### Instruction ###\n{item['chat']}" 
        elif self.mode == self.INST:
            new_query = f"### Instruction ###\n{item['code_inst']}"
        elif self.mode == self.INST_CTX:
            new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Context ###\n{item_ctx}"
        elif self.mode == self.INST_EXAMPLE:
            new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Examples ###\n{item_examples}"
        elif self.mode == self.INST_CTX_EXAMPLE:
            new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Context ###\n{item_ctx}\n\n### Examples ###\n{item_examples}"
        else:
            raise ValueError(f"Invalid query mode: {self.mode}")

        return new_query
