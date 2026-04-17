import sys
import os
import random
from datetime import date, time, timedelta

# add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)
from src.models.person import Person
from conf.logger_conf import setup_logger
logger = setup_logger("main.log")

def create_person():
    """
    Create a person object with generated data
    """
    person = Person(adharCardNo="1234-5678-9012", mobileNo=1234567890)
    print(f"Created Person: Adhar Card No: {person.adharCardNo}, Mobile No: {person.mobileNo}")

    """
    update mobile number and print updated details
    """
    try:
        person.mobileNo = random.randint(10**9, 10**10 - 1)
        print(f"Updated Person: Adhar Card No: {person.adharCardNo}, Mobile No: {person.mobileNo}")
        logger.info(f"Updated Person: Adhar Card No: {person.adharCardNo}, Mobile No: {person.mobileNo}")
    except ValueError as e:
        print(f"Error updating mobile number: {e}")
        logger.error(f"Error updating mobile number: {e}")


if __name__ == "__main__":
    create_person()