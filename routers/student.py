from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.student import Student, StudentStatus
from schemas.student import StudentCreate, StudentOut

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admission", response_model=StudentOut)
def create_student_admission(student: StudentCreate, db: Session = Depends(get_db)):
    # Prevent duplicate admission number per tenant
    existing = db.query(Student).filter(
        Student.tenant_id == student.tenant_id,
        Student.admission_number == student.admission_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Admission number already exists")

    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.put("/{student_id}/approve")
def approve_admission(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.status = StudentStatus.enrolled
    db.commit()
    return {"message": "Admission approved"}

from services.validation import validate_admission_number, validate_mandatory_fields

@router.post("/admission", response_model=StudentOut)
def create_student_admission(student: StudentCreate, db: Session = Depends(get_db)):
    # Validate admission number uniqueness
    validate_admission_number(db, student.tenant_id, student.admission_number)

    # Validate mandatory fields
    required_fields = ["full_name", "dob", "gender", "admission_date"]
    validate_mandatory_fields(student.dict(), required_fields)

    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
