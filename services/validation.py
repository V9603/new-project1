from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student

def validate_admission_number(db: Session, tenant_id: int, admission_number: str):
    existing = db.query(Student).filter(
        Student.tenant_id == tenant_id,
        Student.admission_number == admission_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Admission number already exists")

def validate_mandatory_fields(student_data: dict, required_fields: list):
    for field in required_fields:
        if not student_data.get(field):
            raise HTTPException(status_code=400, detail=f"Missing mandatory field: {field}")

def validate_guardian_mapping(existing_guardians: list, new_guardian_name: str, contact_number: str):
    for g in existing_guardians:
        if g.name == new_guardian_name and g.contact_number == contact_number:
            raise HTTPException(status_code=400, detail="Duplicate guardian mapping")

def validate_promotion_prerequisites(student_status: str):
    if student_status not in ["active", "enrolled"]:
        raise HTTPException(status_code=400, detail="Student not eligible for promotion")
