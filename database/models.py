from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'
    PatientID = Column(String, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    DateOfBirth = Column(Date)
    Gender = Column(String)
    Address = Column(String)
    ContactNumber = Column(String)
    Email = Column(String)
    MedicalHistory = Column(Text)
    Allergies = Column(Text)
    Medications = Column(Text)
    InsuranceDetails = Column(Text)
    EmergencyContact = Column(Text)
