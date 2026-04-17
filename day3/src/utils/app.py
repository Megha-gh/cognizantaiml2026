import sys
import os

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from src.stores.appointment_store import AppointmentStore

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application. this module initializes the logger and defines the main function to run the application.
"""

logger = setup_logger()
def run():
    """
    test logger
    """
    from datetime import date, time
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    patient = Patient(1, "John Doe", date(1990, 5, 15), "Flu")
    appointment = Appointment(1, date(2024, 6, 1), time(10, 0), doctor, patient)
    appointment_store = AppointmentStore()
    appointment_store.add_appointment(appointment)
    logger.info("app run")
"""
handle entry point of the application
"""
if __name__ == "__main__":
    run()