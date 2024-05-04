import os
import sys
import logging

# Configuration parameters
logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Create handlers
console_handler = logging.StreamHandler(sys.stdout)  # Handler for console output
file_handler = logging.FileHandler(log_filepath)     # Handler for file output

# Set formatter
formatter = logging.Formatter(logging_str)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Create logger
logger = logging.getLogger('diabetes_classification_project')
logger.setLevel(logging.INFO)  # Set the logging level
logger.addHandler(console_handler)  # Add console handler
logger.addHandler(file_handler)  # Add file handler
