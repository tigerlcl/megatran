import os
import logging
import yaml

class Context:
    def __init__(self, args):
        self.exp_name = args.exp_name
        self.config = self._load_config(args.config)  # Load the config once
        
        # Initialize the logger first
        self.logger = self.setup_logger()  
        
        # Setup directories
        self.code_dir = os.path.join('exp', self.exp_name, 'code')
        os.makedirs(self.code_dir, exist_ok=True)
        
        self.result_dir = os.path.join('exp', self.exp_name, 'result')
        os.makedirs(self.result_dir, exist_ok=True)
        
        self.temp_dir = 'temp'
        os.makedirs(self.temp_dir, exist_ok=True)  # For executable python files

    def _load_config(self, config_path):
        """Load the configuration from the YAML file and set as instance properties."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)  # Load the config
            for key, value in config.items():
                setattr(self, key, value)  # Set each key as an instance property


    def setup_logger(self):
        """Configure the logger for experiment tracking."""
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(os.path.join(log_dir, f'{self.exp_name}.log'), mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info("Logger initialized.")
        return logger
