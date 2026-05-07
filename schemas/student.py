from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from models.student import StudentStatus

class GuardianBase(BaseModel):
    name: str
    relation_type: str
    priority: int
    contact_number: str

class GuardianCreate(GuardianBase):
    pass

class GuardianOut(GuardianBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    tenant_id: int
    admission_number: str
    full_name: str
    dob: date
    gender: str
    blood_group: Optional[str]
    address: Optional[str]
    emergency_contact: Optional[str]
    admission_date: date
    academic_status: Optional[str]
    medical_info: Optional[str]
    id_card_details: Optional[str]

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    status: StudentStatus
    guardians: List[GuardianOut] = []
    class Config:
        orm_mode = True
