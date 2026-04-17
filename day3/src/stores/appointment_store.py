"""
create appointment crud (create, retrieve, update, delete) operations
"""
import sys
import os
from datetime import date, time

#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.patient import Patient
from src.models.doctor import Doctor
from src.exceptions.AppointmentNotFoundException import AppointmentNotFoundException
from conf.logger_conf import setup_logger

logger = setup_logger("appointment_store.log")

class AppointmentStore:
    def __init__(self):
        self.appointments = []
    
    def add_appointment(self, appointment):
        """Add a new appointment to the store"""
        logger.info(f"Adding appointment: {appointment}")
        self.appointments.append(appointment)
        return appointment
    
    def get_all_appointments(self):
        """Retrieve all appointments"""
        logger.info("Retrieving all appointments")
        return self.appointments
    
    def get_appointment_by_id(self, appointment_id: int):
        """Retrieve an appointment by ID, raises exception if not found"""
        logger.info(f"Retrieving appointment with ID: {appointment_id}")
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        raise AppointmentNotFoundException(f"Appointment with ID {appointment_id} not found")
    
    def update_appointment(self, appointment_id: int, patient: Patient = None, doctor: Doctor = None, appointment_date: date = None, appointment_time: time = None):
        """Update appointment details, raises exception if not found"""
        logger.info(f"Updating appointment with ID: {appointment_id}")
        appointment = self.get_appointment_by_id(appointment_id)  # This will raise exception if not found
        if patient:
            appointment.patient = patient
        if doctor:
            appointment.doctor = doctor
        if appointment_date:
            appointment.date = appointment_date
        if appointment_time:
            appointment.time = appointment_time
        logger.info(f"Appointment updated: {appointment}")
        return appointment
    
    def delete_appointment(self, appointment_id: int):
        """Delete an appointment by ID, raises exception if not found"""
        logger.info(f"Deleting appointment with ID: {appointment_id}")
        appointment = self.get_appointment_by_id(appointment_id)  # This will raise exception if not found
        self.appointments.remove(appointment)
        logger.info(f"Appointment deleted: {appointment}")
        return appointment