# Configure log format
import logging
"""
set up logger for healthcare appln
"""
def setup_logger():
    """
    create logger for healthcare application
    """
    logger = logging.getLogger("healthcare_logger")
    logger.setLevel(logging.DEBUG)
    """
    check if logger already has handlers to avoid duplicate logs
    """
    # to check already log exists or not
    if logger.hasHandlers():
        return logger
    """
    create file handler to store logs in healthcare.log file
    """
    #storing log inside the file so create file handler
    file_handler = logging.FileHandler("healthcare.log")
    logger.setLevel(logging.DEBUG)

    #how the file format should be
    """
    create formatter to specify log message format
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

