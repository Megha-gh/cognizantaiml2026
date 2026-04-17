"""
create doctor crud (create, retrieve, update, delete) operations
"""
import sys
import os

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.doctor import Doctor
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from conf.logger_conf import setup_logger

logger = setup_logger("doctor_store.log")

class DoctorStore:
    def __init__(self):
        self.doctors = []
    
    def add_doctor(self, doctor: Doctor):
        """Add a new doctor to the store"""
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)
        return doctor
    
    def get_all_doctors(self):
        """Retrieve all doctors"""
        logger.info("Retrieving all doctors")
        return self.doctors
    
    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        """Retrieve a doctor by ID, raises exception if not found"""
        logger.info(f"Retrieving doctor with ID: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with ID {doctor_id} not found")
    
    def update_doctor(self, doctor_id: int, name: str = None, specialization: str = None):
        """Update doctor details, raises exception if not found"""
        logger.info(f"Updating doctor with ID: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)  # This will raise exception if not found
        if name:
            doctor.name = name
        if specialization:
            doctor.specialization = specialization
        logger.info(f"Doctor updated: {doctor}")
        return doctor
    
    def delete_doctor(self, doctor_id: int):
        """Delete a doctor by ID, raises exception if not found"""
        logger.info(f"Deleting doctor with ID: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)  # This will raise exception if not found
        self.doctors.remove(doctor)
        logger.info(f"Doctor deleted: {doctor}")
        return doctor