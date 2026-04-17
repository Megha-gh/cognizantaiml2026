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
from src.stores.doctor_stor import DoctorStore
from src.stores.patient_store import PatientStore
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.exceptions.patient_not_found_exception import PatientNotFoundException
from src.exceptions.AppointmentNotFoundException import AppointmentNotFoundException

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application. this module initializes the logger and defines the main function to run the application.
"""

logger = setup_logger()

def doctor_app():
    """
    Doctor CRUD operations
    """
    logger.info("=== DOCTOR CRUD OPERATIONS ===")
    doctor_store = DoctorStore()
    
    # CREATE - Add doctors
    logger.info("--- ADD DOCTORS ---")
    doctor1 = Doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = Doctor(2, "Dr. Johnson", "Neurology")
    doctor3 = Doctor(3, "Dr. Williams", "Orthopedics")
    
    doctor_store.add_doctor(doctor1)
    doctor_store.add_doctor(doctor2)
    doctor_store.add_doctor(doctor3)
    logger.info(f"Added 3 doctors")
    
    # READ - Get all doctors
    logger.info("--- READ ALL DOCTORS ---")
    all_doctors = doctor_store.get_all_doctors()
    for doctor in all_doctors:
        logger.info(f"Doctor: {doctor}")
    
    # READ - Get doctor by ID
    logger.info("--- READ DOCTOR BY ID ---")
    retrieved_doctor = doctor_store.get_doctor_by_id(1)
    logger.info(f"Retrieved: {retrieved_doctor}")
    
    # UPDATE - Update doctor details
    logger.info("--- UPDATE DOCTOR ---")
    updated_doctor = doctor_store.update_doctor(1, "Dr. Smith Jr.", "Cardiothoracic Surgery")
    logger.info(f"Updated: {updated_doctor}")
    
    # DELETE - Delete doctor
    logger.info("--- DELETE DOCTOR ---")
    deleted_doctor = doctor_store.delete_doctor(3)
    logger.info(f"Deleted: {deleted_doctor}")
    logger.info(f"Remaining doctors: {len(doctor_store.get_all_doctors())}")
    
    # ERROR HANDLING - Try to update non-existent doctor
    logger.info("--- ERROR HANDLING ---")
    try:
        doctor_store.update_doctor(999, "Non-existent")
    except DoctorNotFoundException as e:
        logger.error(f"Exception caught: {e}")
    
    return doctor_store

def patient_app():
    """
    Patient CRUD operations
    """
    logger.info("=== PATIENT CRUD OPERATIONS ===")
    patient_store = PatientStore()
    from datetime import date
    
    # CREATE - Add patients
    logger.info("--- ADD PATIENTS ---")
    patient1 = Patient(1, "John Doe", date(1990, 5, 15), "Flu")
    patient2 = Patient(2, "Jane Smith", date(1985, 3, 22), "Migraine")
    patient3 = Patient(3, "Bob Johnson", date(1992, 7, 10), "Hypertension")
    
    patient_store.add_patient(patient1)
    patient_store.add_patient(patient2)
    patient_store.add_patient(patient3)
    logger.info(f"Added 3 patients")
    
    # READ - Get all patients
    logger.info("--- READ ALL PATIENTS ---")
    all_patients = patient_store.get_all_patients()
    for patient in all_patients:
        logger.info(f"Patient: {patient}")
    
    # READ - Get patient by ID
    logger.info("--- READ PATIENT BY ID ---")
    retrieved_patient = patient_store.get_patient_by_id(1)
    logger.info(f"Retrieved: {retrieved_patient}")
    
    # UPDATE - Update patient details
    logger.info("--- UPDATE PATIENT ---")
    updated_patient = patient_store.update_patient(1, "John Doe Jr.", ailment="Cold")
    logger.info(f"Updated: {updated_patient}")
    
    # DELETE - Delete patient
    logger.info("--- DELETE PATIENT ---")
    deleted_patient = patient_store.delete_patient(3)
    logger.info(f"Deleted: {deleted_patient}")
    logger.info(f"Remaining patients: {len(patient_store.get_all_patients())}")
    
    # ERROR HANDLING - Try to update non-existent patient
    logger.info("--- ERROR HANDLING ---")
    try:
        patient_store.update_patient(999, "Non-existent")
    except PatientNotFoundException as e:
        logger.error(f"Exception caught: {e}")
    
    return patient_store

def appointment_app(doctor_store, patient_store):
    """
    Appointment CRUD operations
    """
    logger.info("=== APPOINTMENT CRUD OPERATIONS ===")
    appointment_store = AppointmentStore()
    from datetime import date, time
    
    # Get doctors and patients for appointments
    doctors = doctor_store.get_all_doctors()
    patients = patient_store.get_all_patients()
    
    if not doctors or not patients:
        logger.warning("Not enough doctors or patients for appointments")
        return appointment_store
    
    # CREATE - Add appointments
    logger.info("--- ADD APPOINTMENTS ---")
    appointment1 = Appointment(1, date(2024, 6, 1), time(10, 0), doctors[0], patients[0])
    appointment2 = Appointment(2, date(2024, 6, 5), time(14, 30), doctors[1], patients[1])
    appointment3 = Appointment(3, date(2024, 6, 10), time(9, 0), doctors[0], patients[1])
    
    appointment_store.add_appointment(appointment1)
    appointment_store.add_appointment(appointment2)
    appointment_store.add_appointment(appointment3)
    logger.info(f"Added 3 appointments")
    
    # READ - Get all appointments
    logger.info("--- READ ALL APPOINTMENTS ---")
    all_appointments = appointment_store.get_all_appointments()
    for appointment in all_appointments:
        logger.info(f"Appointment: {appointment}")
    
    # READ - Get appointment by ID
    logger.info("--- READ APPOINTMENT BY ID ---")
    retrieved_appointment = appointment_store.get_appointment_by_id(1)
    logger.info(f"Retrieved: {retrieved_appointment}")
    
    # UPDATE - Update appointment details
    logger.info("--- UPDATE APPOINTMENT ---")
    updated_appointment = appointment_store.update_appointment(1, appointment_time=time(11, 0))
    logger.info(f"Updated: {updated_appointment}")
    
    # DELETE - Delete appointment
    logger.info("--- DELETE APPOINTMENT ---")
    deleted_appointment = appointment_store.delete_appointment(3)
    logger.info(f"Deleted: {deleted_appointment}")
    logger.info(f"Remaining appointments: {len(appointment_store.get_all_appointments())}")
    
    # ERROR HANDLING - Try to update non-existent appointment
    logger.info("--- ERROR HANDLING ---")
    try:
        appointment_store.update_appointment(999, appointment_time=time(12, 0))
    except AppointmentNotFoundException as e:
        logger.error(f"Exception caught: {e}")
    
    return appointment_store

def run():
    """
    Main function that executes all CRUD operations
    """
    logger.info("Starting Healthcare Application")
    
    # Run doctor operations
    doctor_store = doctor_app()
    
    # Run patient operations
    patient_store = patient_app()
    
    # Run appointment operations
    appointment_store = appointment_app(doctor_store, patient_store)
    
    logger.info("Healthcare Application completed successfully")

"""
handle entry point of the application
"""
if __name__ == "__main__":
    run()

