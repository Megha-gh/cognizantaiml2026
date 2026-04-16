import sys
import os

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application. this module initializes the logger and defines the main function to run the application.
"""
logger = setup_logger()
def run():
    """
    test logger
    """
    logger.info("app run")
"""
handle entry point of the application
"""
if __name__ == "__main__":
    run()