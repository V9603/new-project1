from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.guardian import Guardian
from models.student import Student
from schemas.student import GuardianCreate, GuardianOut
from typing import List


router = APIRouter(prefix="/guardians", tags=["Guardians"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/link/{student_id}", response_model=GuardianOut)
def link_guardian(student_id: int, guardian: GuardianCreate, db: Session = Depends(get_db)):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    existing = db.query(Guardian).filter(
        Guardian.student_id == student_id,
        Guardian.name == guardian.name,
        Guardian.contact_number == guardian.contact_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Guardian already linked")

    new_guardian = Guardian(**guardian.dict(), student_id=student_id)
    db.add(new_guardian)
    db.commit()
    db.refresh(new_guardian)
    return new_guardian


from services.validation import validate_guardian_mapping

@router.post("/link/{student_id}", response_model=GuardianOut)
def link_guardian(student_id: int, guardian: GuardianCreate, db: Session = Depends(get_db)):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    validate_guardian_mapping(student.guardians, guardian.name, guardian.contact_number)

    new_guardian = Guardian(**guardian.dict(), student_id=student_id)
    db.add(new_guardian)
    db.commit()
    db.refresh(new_guardian)
    return new_guardian
