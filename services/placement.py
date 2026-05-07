from sqlalchemy.orm import Session
from models.student import Student
from fastapi import HTTPException

def assign_class_section(db: Session, student_id: int, class_name: str, section_name: str):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Example validation: prevent invalid class assignment
    if not class_name or not section_name:
        raise HTTPException(status_code=400, detail="Class and Section required")

    student.academic_status = f"{class_name}-{section_name}"
    db.commit()
    db.refresh(student)
    return student

def generate_roll_number(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Simple roll number logic: admission_number + suffix
    student.id_card_details = f"ROLL-{student.admission_number}"
    db.commit()
    db.refresh(student)
    return student
