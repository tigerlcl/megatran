import os
import logging
import yaml

class Context:
    def __init__(self, args):
        self.exp_name = args.exp_name
        self.dataset_name = args.dataset_name
        self.cfg = self._load_config(args.config)  # Load the config once
        self.logger = self.setup_logger()  # Initialize the logger first
        
        # Setup directories
        self.code_dir = self.setup_directory(os.path.join('exp', self.exp_name, 'code'))
        self.result_dir = self.setup_directory(os.path.join('exp', self.exp_name, 'result'))
        self.temp_dir = self.setup_directory('temp')  # For executable python files

    def _load_config(self, config_path):
        """Load the configuration from the YAML file."""
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)  # Return the loaded config

    def setup_directory(self, directory):
        """Ensure that a directory exists; create it if it does not."""
        os.makedirs(directory, exist_ok=True)
        self.logger.info(f"Ensured directory exists: {directory}")
        return directory

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
