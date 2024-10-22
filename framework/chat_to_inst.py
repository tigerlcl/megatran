import concurrent.futures
from openai import OpenAI
from .prompt_generator import ChatPrompt


class ChatBuilder:
    """
    ChatBuilder is used to translate the user's query with our fine-tuned LLM.
    We explore various query combinations of three components:
    1. chat: the user's chat
    2. context/ctx: the context information
    3. tuples/examples: the transformation examples

    """
    def __init__(self, dataset, ctx):
        self.dataset = dataset
        self.model_path = ctx.vllm_model
        
        self.vllm_client = OpenAI(**ctx.vllm_cfg)
        self.query_generator = ChatPrompt(ctx.chat_mode, ctx.n_shot)
        self.logger = ctx.logger
    
    def _process_data(self, item):
        self.logger.info(f"Generating instruction for {item['file_path']}")
        try:
            query = self.query_generator.get_prompt_by_mode(item)
        except ValueError as e:
            self.logger.error(f"Error when generating prompt: {e}")
            return None

        completion = self.vllm_client.chat.completions.create(
            model=self.model_path,
            messages=[{"role": "user", "content": query}],
            temperature=0.2
        )
        response = completion.choices[0].message.content
        item['code_inst'] = response

        return item
    
    # batch processing
    def run(self):
        instruction_lst = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_inst = {executor.submit(self._process_data, item): item for item in self.dataset}
            for future in concurrent.futures.as_completed(future_to_inst):
                result = future_to_inst[future]
                try:
                    inst = future.result()
                except Exception as e:
                    self.logger.error(f"Error processing item {result}: {e}")
                
                instruction_lst.append(inst)

        return instruction_lst

