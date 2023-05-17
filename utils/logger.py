import os
import logging
import sys

# Get the absolute path of the current directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Specify the logs directory path
logs_dir = os.path.join(base_dir, 'logs')

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Specify the log file path
log_file = os.path.join(logs_dir, 'test.log')

# Delete the existing log file, if it exists
if os.path.exists(log_file):
    os.remove(log_file)

# Create a logger instance
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.INFO)

# Create a file handler and set its formatter
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Create a stream handler and set its formatter
stream_handler = logging.StreamHandler(sys.stdout)
stream_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Now you can use the logger to log messages
logger.info('Executing logger.py code')
