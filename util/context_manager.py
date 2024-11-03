import os
import yaml
import shutil
import logging


class Context:
    def __init__(self, args):
        self.exp_name = args.exp_name
        self.dataset_name = args.dataset_name
        self.testing = args.testing
        self.config = self._load_config(args.config)  # Load the config once

        # clear the exp directory for re-do
        if os.path.exists(os.path.join('exp', self.exp_name)):
            shutil.rmtree(os.path.join('exp', self.exp_name))
        
        # Setup directories
        self.code_dir = os.path.join('exp', self.exp_name, 'code')
        os.makedirs(self.code_dir, exist_ok=True)
        
        self.result_dir = os.path.join('exp', self.exp_name, 'result')
        os.makedirs(self.result_dir, exist_ok=True)
        
        self.temp_dir = 'temp'
        os.makedirs(self.temp_dir, exist_ok=True)  # For executable python files

        # Initialize logger
        self.logger = self._setup_logger()

        self.logger.info(f"Code backend LLM: {self.openai_model}")

    def _load_config(self, config_path):
        """Load the configuration from the YAML file and set as instance properties."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)  # Load the config
            for key, value in config.items():
                setattr(self, key, value)  # Set each key as an instance property


    def _setup_logger(self):
        """Configure the logger for experiment tracking."""
        log_fp = os.path.join('exp', self.exp_name, f'{self.exp_name}.log')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_fp, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info("Logger initialized.")
        return logger

    def get(self, key, default=None):
        return getattr(self, key, default)
