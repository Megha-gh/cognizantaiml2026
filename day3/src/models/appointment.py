"""
create appointment
"""
from datetime import date,time
from .doctor import Doctor
from .patient import Patient
class Appointment:
    def __init__(self, id: int, date: date, time: time, doctor: Doctor, patient: Patient):
        self.appointment_id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(id={self.appointment_id}, patient='{self.patient}', doctor='{self.doctor}', date='{self.date}', time='{self.time}')"