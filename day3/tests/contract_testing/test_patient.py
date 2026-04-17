"""
test for patient contract
"""
import sys
import os
import pytest
import csv

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.patient import Patient

"""
test for patient object created
"""

@pytest.fixture
def initialize_patient():
    """
    initialize patient object
    """
    patient = Patient(
        id=1,
        name="Amit Kumar",
        dob="1979-05-12",
        ailment="Hypertension"
    )
    return patient


def read_patient_data_from_csv(file_path):
    """
    read patient data from csv file
    """
    patient_data = []
    with open('tests/patient.csv', mode='r', newline="", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            patient_data.append(
                (
                    int(row['id']),
                    row['name'],
                    row['dob'],
                    row['ailment']
                )
            )
    return patient_data


def test_patient_creation(initialize_patient):
    """
    test patient object creation
    """
    patient = initialize_patient
    assert patient.id == 1
    assert patient.name == "Amit Kumar"
    assert patient.dob == "1979-05-12"
    assert patient.ailment == "Hypertension"


@pytest.mark.parametrize(
    "id, name, dob, ailment",
    [
        (2, "Sneha Nair", "1993-08-21", "Diabetes"),
        (3, "Rahul Verma", "1997-02-15", "Asthma"),
        (4, "Anjali Singh", "1990-11-03", "Allergy"),
    ]
)
def test_parameterized_patient_creation(id, name, dob, ailment):
    """
    test patient object creation with different parameters
    """
    patient = Patient(
        id=id,
        name=name,
        dob=dob,
        ailment=ailment
    )
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment


@pytest.mark.parametrize(
    "id, name, dob, ailment",
    read_patient_data_from_csv('patients_simple.csv')
)
def test_parameterized_patient_creation_from_csv(id, name, dob, ailment):
    """
    test patient object creation using csv data
    """
    patient = Patient(
        id=id,
        name=name,
        dob=dob,
        ailment=ailment
    )
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment
