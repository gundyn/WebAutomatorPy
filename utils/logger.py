import os
import logging
import sys

print("Executing logger.py code")

# Get the absolute path of the current directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Specify the logs directory path
logs_dir = os.path.join(base_dir, 'logs')

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Specify the log file path
log_file = os.path.join(logs_dir, 'test.log')

# Configure the logging
try:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
except Exception as e:
    print(f"Error occurred while configuring logging: {str(e)}")

# Create a logger instance
logger = logging.getLogger()
