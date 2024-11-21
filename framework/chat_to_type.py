import threading
from queue import Queue
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
    def __init__(self, dataset, ctx):
        self.dataset = dataset
        self.model_path = ctx.vllm_model
        self.vllm_client = OpenAI(**ctx.vllm_cfg)
        self.prompt_maker = PromptMaker(ctx.prompt_mode, ctx.n_shot)
        self.logger = ctx.logger
        self.result_queue = Queue()
        self.max_workers = 16
        # Lock for thread-safe logging
        self.log_lock = threading.Lock()

        # Check if the vllm backend client is connected
        if not self._check_client_connection():
            raise RuntimeError("Failed to connect to the vLLM client, please check your config.")
    
    def _check_client_connection(self):
        try:
            # Attempt to make a simple API call to check connection
            self.vllm_client.chat.completions.create(
                model=self.model_path,
                messages=[{"role": "user", "content": "Test connection"}],
                temperature=0.0
            )
            return True  # Connection successful
        except Exception as e:
            self.logger.error(f"Connection check failed: {e}")
            return False  # Connection failed

    def _process_data(self, item, idx):
        # Use lock to ensure thread-safe logging
        with self.log_lock:
            query = self.prompt_maker.get_prompt_by_mode(item)
            self.logger.info(f"[{idx}] Chat-to-Type for {item['file_path']}, query:\n{query}")

        completion = self.vllm_client.chat.completions.create(
            model=self.model_path,
            messages=[{"role": "user", "content": query}],
            temperature=0.2
        )
        code_inst = completion.choices[0].message.content
        
        item['chat'] = f"{item['chat']}\n{code_inst}"
        self.result_queue.put((idx, item))
    
    def run(self):
        instruction_lst = [None] * len(self.dataset)
        
        threads = []
        for idx, item in enumerate(self.dataset):
            thread = threading.Thread(
                target=self._process_data,
                args=(item, idx)
            )
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        while not self.result_queue.empty():
            idx, result = self.result_queue.get()
            instruction_lst[idx] = result
        
        return instruction_lst