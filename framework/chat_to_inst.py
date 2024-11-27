from openai import OpenAI
from .prompt_generator import PromptMaker

class ChatBuilder:
    """
    ChatBuilder is used to translate the user's query with our fine-tuned LLM.
    We explore various query combinations of three components:
    1. chat: the user's chat
    2. context/ctx: the context information
    3. tuples/examples: the transformation examples
    """
    def __init__(self, ctx):
        self.model_path = ctx.vllm_model
        self.vllm_client = OpenAI(**ctx.vllm_cfg)
        self.temperature = ctx.vllm_temperature
        self.prompt_maker = PromptMaker(ctx.prompt_mode, ctx.n_shot)
        self.analyzer = ctx.result_analyzer
        self.logger = ctx.logger
            
        # Check if the vllm backend client is connected
        try:
            self.vllm_client.chat.completions.create(
                model=self.model_path,
                messages=[{"role": "user", "content": "Test connection"}],
                temperature=self.temperature
            )
            self.logger.info(f"Chat-to-inst: vllm backend connected")
        except Exception:
            raise RuntimeError("Failed to connect to the vLLM client, please check your config.")


    def run(self, item: dict) -> dict:
        query = self.prompt_maker.get_prompt_by_mode(item)
        self.logger.info(f"Chat-to-inst query:\n{query}")

        completion = self.vllm_client.chat.completions.create(
            model=self.model_path,
            messages=[{"role": "user", "content": query}],
            temperature=self.temperature
        )
        code_inst = completion.choices[0].message.content
        self.logger.info(f"Chat-to-inst token usage: Prompt: {completion.usage.prompt_tokens}, Completion: {completion.usage.completion_tokens}")
        
        self.analyzer.add_token_usage("chat_to_inst", completion.usage.prompt_tokens, completion.usage.completion_tokens)
        
        # item['chat'] = f"{item['chat']}\n{code_inst}"
        item['chat'] = code_inst
        
        return item
