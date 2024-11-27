import os
import yaml
import logging
from .analyzer import ResultAnalyzer

from dotenv import load_dotenv
load_dotenv() # take environment variables from .env file

class Context:
    """
    Context manages experiment configuration and result analysis:
    1. Loads configuration from YAML
    2. Sets up experiment directories
    3. Configures logging
    4. Provides access to experiment settings
    5. Add ResultAnalyzer
    """
    
    def __init__(self, args):
        """
        Initialize experiment context
        
        Args:
            args: ArgumentParser args containing:
                - exp_name: Experiment name
                - dataset_name: Dataset to use
                - testing: Boolean for test mode
                - config: Path to config YAML
        """
        self.exp_name = args.exp_name
        self.dataset_name = args.dataset_name
        self.testing = args.testing
        self.config = self._load_config(args.config)


        # OpenAI Auth
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_base_url = os.getenv("OPENAI_BASE_URL")
        
        # Setup experiment directories
        self._setup_directories()
        
        # Initialize logger
        self.logger = self._setup_logger()
        self.logger.info(f"Code backend LLM: {self.openai_model}")

        # Framework config
        self.chat_to_inst = self.get('chat_to_inst', False)
        self.allow_reflection = self.get('allow_reflection', False)
        self.allow_rag = self.get('allow_rag', False)
        self.logger.info(f"Chat-to-inst: {self.chat_to_inst}, Reflection: {self.allow_reflection}, Lazy RAG: {self.allow_rag}")

        # Initialize Result Analyzer
        self.result_analyzer = ResultAnalyzer(self.result_dir)

    def _setup_directories(self):
        """
        Create experiment directory structure:
        exp/
        ├── {exp_name}/
        │   ├── code/      # Generated code storage
        │   ├── result/    # Experiment results
        │   └── {exp_name}.log
        └── temp/          # Temporary files
        """
        # Check if experiment directory already exists
        if os.path.exists(os.path.join('exp', self.exp_name)) and not self.testing:
            raise ValueError(f"Experiment directory 'exp/{self.exp_name}' already exists. Please use a different experiment name to avoid overwriting existing results.")
        
        # Create new directories
        self.code_dir = os.path.join('exp', self.exp_name, 'code')
        os.makedirs(self.code_dir, exist_ok=True)
        
        self.result_dir = os.path.join('exp', self.exp_name, 'result')
        os.makedirs(self.result_dir, exist_ok=True)
        
        self.temp_dir = 'temp'
        os.makedirs(self.temp_dir, exist_ok=True)

    def _load_config(self, config_path):
        """Load YAML config and set as instance attributes"""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            for key, value in config.items():
                setattr(self, key, value)
            return config

    def _setup_logger(self):
        """Configure experiment logger with both file and console output"""
        log_fp = os.path.join('exp', self.exp_name, f'{self.exp_name}.log')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # File handler
        file_handler = logging.FileHandler(log_fp, mode='w')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        
        # Stream handler (console)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        logger.addHandler(stream_handler)
        
        logger.info("Logger initialized.")
        return logger

    def get(self, key, default=None):
        """Safely get configuration value"""
        return getattr(self, key, default)
