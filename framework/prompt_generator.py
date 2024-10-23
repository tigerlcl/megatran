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


# class CodePrompt:
#     """
#     CodePrompt is used to generate the prompt for the code generation task.
#     """

#     # baseline
#     CHAT: str = "chat"
#     CHAT_EXAMPLE: str = "chat_example"
    
#     # below for framwork
#     INST: str = "inst"
#     INST_EXAMPLE: str = "inst_example"
#     INST_CTX: str = "inst_ctx"
#     INST_CTX_EXAMPLE: str = "inst_ctx_example"

#     def __init__(self, mode: str, n_shot: int):
#         self.mode = mode
#         self.n_shot = n_shot

#     def get_prompt_by_mode(self, item: dict):
#         item_ctx = f'Input: {item["context"]["input"]}\nOutput: {item["context"]["output"]}'
    
#         tuple_shots = item["tuples"][:self.n_shot]
#         item_examples = '\n'.join([f'Input: {example["input"]}\nOutput: {example["output"]}' 
#                                                 for example in tuple_shots])

#         if self.mode == self.CHAT:
#             new_query = f"### Instruction ###\n{item['chat']}"
#         elif self.mode == self.CHAT_EXAMPLE:
#             new_query = f"### Instruction ###\n{item['chat']}\n\n### Examples ###\n{item_examples}"  
#         elif self.mode == self.INST:
#             new_query = f"### Instruction ###\n{item['code_inst']}"
#         elif self.mode == self.INST_CTX:
#             new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Context ###\n{item_ctx}"
#         elif self.mode == self.INST_EXAMPLE:
#             new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Examples ###\n{item_examples}"
#         elif self.mode == self.INST_CTX_EXAMPLE:
#             new_query = f"### Instruction ###\n{item['code_inst']}\n\n### Context ###\n{item_ctx}\n\n### Examples ###\n{item_examples}"
#         else:
#             raise ValueError(f"Invalid query mode: {self.mode}")

#         return new_query
