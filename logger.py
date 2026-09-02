"""
Logging module for Crypto Arbitrage Bot
Provides centralized logging configuration
"""
import logging
import os
from datetime import datetime
from config import Config


def setup_logger(name):
    """
    Setup logger with file and console handlers
    
    Args:
        name (str): Logger name
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(Config.LOG_FILE)
    file_handler.setLevel(getattr(logging, Config.LOG_LEVEL))
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, Config.LOG_LEVEL))
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    if not logger.handlers:  # Avoid duplicate handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger


# Create main logger
logger = setup_logger('crypto_arbitrage_bot')
