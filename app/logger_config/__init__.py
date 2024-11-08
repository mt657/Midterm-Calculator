import logging

def setup_logging():
    """Set up the logging configuration for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("calculator.log"),
            logging.StreamHandler()
        ]
    )
