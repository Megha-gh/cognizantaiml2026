import sys
import os
from datetime import date, time, timedelta
from faker import Faker

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

logger = setup_logger("healthcare.log")
fake = Faker()

# Specializations for doctors
SPECIALIZATIONS = ["Cardiology", "Neurology", "Orthopedics", "Dermatology", "Pediatrics", "Ophthalmology"]

# Common ailments
AILMENTS = ["Flu", "Migraine", "Hypertension", "Diabetes", "Asthma", "Cold", "Fever", "Arthritis"]

def doctor_app():
    """
    Doctor CRUD operations using Faker to generate test data
    """
    logger.info("=== DOCTOR CRUD OPERATIONS ===")
    doctor_store = DoctorStore()
    
    # CREATE - Add doctors with Faker-generated data
    logger.info("--- ADD DOCTORS (Using Faker) ---")
    doctors_list = []
    for i in range(1, 4):
        doctor_name = f"Dr. {fake.last_name()}"
        specialization = fake.random_element(SPECIALIZATIONS)
        doctor = Doctor(i, doctor_name, specialization)
        doctors_list.append(doctor)
        doctor_store.add_doctor(doctor)
        logger.info(f"Added: {doctor}")
    
    logger.info(f"Added {len(doctors_list)} doctors")
    
    # READ - Get all doctors
    logger.info("--- READ ALL DOCTORS ---")
    all_doctors = doctor_store.get_all_doctors()
    for doctor in all_doctors:
        logger.info(f"Doctor: {doctor}")
    
    # READ - Get doctor by ID
    logger.info("--- READ DOCTOR BY ID ---")
    retrieved_doctor = doctor_store.get_doctor_by_id(1)
    logger.info(f"Retrieved: {retrieved_doctor}")
    
    # UPDATE - Update doctor details with Faker data
    logger.info("--- UPDATE DOCTOR ---")
    new_name = f"Dr. {fake.last_name()}"
    new_specialization = fake.random_element(SPECIALIZATIONS)
    updated_doctor = doctor_store.update_doctor(1, new_name, new_specialization)
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
    Patient CRUD operations using Faker to generate test data
    """
    logger.info("=== PATIENT CRUD OPERATIONS ===")
    patient_store = PatientStore()
    
    # CREATE - Add patients with Faker-generated data
    logger.info("--- ADD PATIENTS (Using Faker) ---")
    patients_list = []
    for i in range(1, 4):
        patient_name = fake.name()
        patient_dob = fake.date_of_birth(minimum_age=18, maximum_age=80)
        ailment = fake.random_element(AILMENTS)
        patient = Patient(i, patient_name, patient_dob, ailment)
        patients_list.append(patient)
        patient_store.add_patient(patient)
        logger.info(f"Added: {patient}")
    
    logger.info(f"Added {len(patients_list)} patients")
    
    # READ - Get all patients
    logger.info("--- READ ALL PATIENTS ---")
    all_patients = patient_store.get_all_patients()
    for patient in all_patients:
        logger.info(f"Patient: {patient}")
    
    # READ - Get patient by ID
    logger.info("--- READ PATIENT BY ID ---")
    retrieved_patient = patient_store.get_patient_by_id(1)
    logger.info(f"Retrieved: {retrieved_patient}")
    
    # UPDATE - Update patient details with Faker data
    logger.info("--- UPDATE PATIENT ---")
    new_name = fake.name()
    new_ailment = fake.random_element(AILMENTS)
    updated_patient = patient_store.update_patient(1, new_name, ailment=new_ailment)
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
    Appointment CRUD operations using Faker to generate test data
    """
    logger.info("=== APPOINTMENT CRUD OPERATIONS ===")
    appointment_store = AppointmentStore()
    
    # Get doctors and patients for appointments
    doctors = doctor_store.get_all_doctors()
    patients = patient_store.get_all_patients()
    
    if not doctors or not patients:
        logger.warning("Not enough doctors or patients for appointments")
        return appointment_store
    
    # CREATE - Add appointments with Faker-generated dates and times
    logger.info("--- ADD APPOINTMENTS (Using Faker) ---")
    appointments_list = []
    for i in range(1, 4):
        # Generate appointment date within next 30 days
        appointment_date = fake.date_between(start_date='today', end_date='+30d')
        # Generate appointment time (between 09:00 and 17:00)
        appointment_hour = fake.random_int(min=9, max=17)
        appointment_minute = fake.random_element([0, 15, 30, 45])
        appointment_time = time(appointment_hour, appointment_minute)
        
        doctor = fake.random_element(doctors)
        patient = fake.random_element(patients)
        
        appointment = Appointment(i, appointment_date, appointment_time, doctor, patient)
        appointments_list.append(appointment)
        appointment_store.add_appointment(appointment)
        logger.info(f"Added: {appointment}")
    
    logger.info(f"Added {len(appointments_list)} appointments")
    
    # READ - Get all appointments
    logger.info("--- READ ALL APPOINTMENTS ---")
    all_appointments = appointment_store.get_all_appointments()
    for appointment in all_appointments:
        logger.info(f"Appointment: {appointment}")
    
    # READ - Get appointment by ID
    logger.info("--- READ APPOINTMENT BY ID ---")
    retrieved_appointment = appointment_store.get_appointment_by_id(1)
    logger.info(f"Retrieved: {retrieved_appointment}")
    
    # UPDATE - Update appointment details with Faker data
    logger.info("--- UPDATE APPOINTMENT ---")
    new_time = time(fake.random_int(min=9, max=17), fake.random_element([0, 15, 30, 45]))
    updated_appointment = appointment_store.update_appointment(1, appointment_time=new_time)
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
    Main function that executes all CRUD operations with Faker-generated data
    """
    logger.info("Starting Healthcare Application with Faker-generated data")
    
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

