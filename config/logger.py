import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name="industry_analyst"):
    """
    Configures a professional logger that outputs to both the console and a file.
    
    - Console: INFO level (clean output for the user)
    - File: DEBUG level (deep detail for engineering/debugging)
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "crew_run.log"

    # 1. Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # 2. Formatter
    # Detailed for file, slightly cleaner for console
    detail_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '%(message)s'
    )

    # 3. Console Handler (Standard Output)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # 4. File Handler (Rotating, keeps 5 MB per file, max 3 files)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detail_formatter)

    # 5. Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Global instance for easy import
logger = setup_logger()
