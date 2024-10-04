import logging
import os
from datetime import datetime

def log_init(log_to_console):
### log_to_console is a bool to determine whether to log output to the console, will log to file by default
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')

    log_make_dir()

    logging.basicConfig(
        filename = 'logs/{:%Y-%m-%d_%I:%M:%S%p}.log'.format(datetime.now()),
        level = logging.DEBUG,
        format = '[%(asctime)s] %(levelname)s - %(message)s'
    )

    # #Option to enable logging to console
    if(log_to_console == 1):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger

# Returns logger to be used with logging functions
def get_logger():
    return logger

def log_make_dir():
    CWD = os.getcwd()
    log_dir_path = os.path.join(CWD,"logs")
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)

if __name__ == "__main__":
    logger = log_init(1)
    # Now you can log messages with different levels
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')