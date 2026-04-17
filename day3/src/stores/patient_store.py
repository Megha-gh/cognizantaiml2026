"""
create patient crud (create, retrieve, update, delete) operations
"""
import sys
import os
from datetime import date

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.patient import Patient
from src.exceptions.patient_not_found_exception import PatientNotFoundException
from conf.logger_conf import setup_logger

logger = setup_logger("patient_store.log")

class PatientStore:
    def __init__(self):
        self.patients = []
    
    def add_patient(self, patient: Patient):
        """Add a new patient to the store"""
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)
        return patient
    
    def get_all_patients(self):
        """Retrieve all patients"""
        logger.info("Retrieving all patients")
        return self.patients
    
    def get_patient_by_id(self, patient_id: int) -> Patient:
        """Retrieve a patient by ID, raises exception if not found"""
        logger.info(f"Retrieving patient with ID: {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with ID {patient_id} not found")
    
    def update_patient(self, patient_id: int, name: str = None, dob: date = None, ailment: str = None):
        """Update patient details, raises exception if not found"""
        logger.info(f"Updating patient with ID: {patient_id}")
        patient = self.get_patient_by_id(patient_id)  # This will raise exception if not found
        if name:
            patient.name = name
        if dob:
            patient.dob = dob
        if ailment:
            patient.ailment = ailment
        logger.info(f"Patient updated: {patient}")
        return patient
    
    def delete_patient(self, patient_id: int):
        """Delete a patient by ID, raises exception if not found"""
        logger.info(f"Deleting patient with ID: {patient_id}")
        patient = self.get_patient_by_id(patient_id)  # This will raise exception if not found
        self.patients.remove(patient)
        logger.info(f"Patient deleted: {patient}")
        return patient