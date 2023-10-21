import json
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from data_service import SessionLocal
from models import Patient
from fuzzywuzzy import fuzz


def insert_patient_data(patient_data):
    """
    Insert new patient data into the database.
    """
    session = SessionLocal()
    new_patient = Patient(**patient_data)
    session.add(new_patient)
    session.commit()
    session.close()


def get_patient_by_id(patient_id):
    """
    Retrieve patient data by PatientID.
    """
    session = SessionLocal()
    patient = session.query(Patient).filter(Patient.PatientID == patient_id).first()
    session.close()
    return patient


def get_patient_by_name(name, threshold=60):
    """
    Retrieve patient data by name with fuzzy matching.
    """
    session = SessionLocal()
    patients = session.query(Patient).all()
    if name is None:
        return []
    print(f"Total patients in DB: {len(patients)}")  # Check if patients are being retrieved

    matched_patients = []
    for patient in patients:
        full_name = f"{patient.FirstName} {patient.LastName}"
        similarity_ratio = fuzz.ratio(full_name.lower(), name.lower())

        print(
            f"Comparing '{full_name}' with '{name}'. Similarity ratio: {similarity_ratio}")  # Check the similarity ratio

        if similarity_ratio >= threshold:
            matched_patients.append(patient)

    session.close()
    return matched_patients[0]


def save_patient_from_json(patient_data):
    """
    Saves a new patient from json data.
    """
    session = SessionLocal()
    new_patient = Patient(
        PatientID=patient_data['PatientID'],
        FirstName=patient_data['FirstName'],
        LastName=patient_data['LastName'],
        DateOfBirth=datetime.strptime(patient_data['DateOfBirth'], '%Y-%m-%d').date(),
        Gender=patient_data['Gender'],
        Address=patient_data['Address'],
        ContactNumber=patient_data['ContactNumber'],
        Email=patient_data['Email'],
        MedicalHistory=patient_data['MedicalHistory'],
        Allergies=patient_data['Allergies'],
        Medications=patient_data['Medications'],
        InsuranceDetails=json.dumps(patient_data['InsuranceDetails']),
        EmergencyContact=json.dumps(patient_data['EmergencyContact']),
    )
    try:
        session.merge(new_patient)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print(f"An error occurred: {e}")
    except Exception as e:
        session.rollback()
        print(f"An unexpected error occurred: {e}")
    finally:
        session.close()

