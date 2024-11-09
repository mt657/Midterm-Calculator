import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def setup_logging():
    """Set up the logging configuration for the application."""
    log_file = os.getenv("LOG_FILE", "default.log")  # Fallback to "default.log" if LOG_FILE is not set
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
