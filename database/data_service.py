import csv
from datetime import datetime
from sqlalchemy import inspect

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Patient, Base

# Create an Engine and Session
# engine = create_engine('sqlite:///test_database/test_database.db')
engine = create_engine(f'')
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """
    Initialize the database by creating the tables based on the models.
    """
    Base.metadata.create_all(bind=engine)


def drop_patient_table():
    """
    Drop the patient table from the database.
    """
    Base.metadata.tables['patients'].drop(engine)
    print("Patient table dropped successfully.")


def insert_data_from_csv(csv_filepath):
    """
    Insert data from a CSV file into the database.
    If the patients table does not exist, it will be created before inserting the data.
    """
    inspector = inspect(engine)
    if 'patients' not in inspector.get_table_names():  # Check if the patients table exists
        init_db()  # If not, initialize the database to create the table

    session = SessionLocal()
    with open(csv_filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['DateOfBirth'] = datetime.strptime(row['DateOfBirth'], '%Y-%m-%d').date()
            patient = Patient(**row)
            session.add(patient)
        session.commit()
    session.close()

