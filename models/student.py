from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class StudentStatus(str, enum.Enum):
    applicant = "applicant"
    enrolled = "enrolled"
    active = "active"
    transferred = "transferred"
    withdrawn = "withdrawn"
    graduated = "graduated"
    alumni = "alumni"
    suspended = "suspended"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, index=True)
    admission_number = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=False)
    dob = Column(Date)
    gender = Column(String)
    blood_group = Column(String)
    address = Column(String)
    emergency_contact = Column(String)
    admission_date = Column(Date)
    academic_status = Column(String)
    medical_info = Column(String)
    id_card_details = Column(String)
    status = Column(Enum(StudentStatus), default=StudentStatus.applicant)

    guardians = relationship("Guardian", back_populates="student")

guardians = relationship("Guardian", back_populates="student")

medical_info = Column(String)
emergency_contact = Column(String)
id_card_details = Column(String)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    old_status = Column(String)
    new_status = Column(String)
    effective_date = Column(DateTime, default=datetime.datetime.utcnow)

    student = relationship("Student", back_populates="history")

# Add relationship in Student model:
history = relationship("StatusHistory", back_populates="student")

