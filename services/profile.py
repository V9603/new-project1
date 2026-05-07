from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student

def update_profile(db: Session, student_id: int, updates: dict):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in updates.items():
        if hasattr(student, key):
            setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

def upload_document(db: Session, student_id: int, document_path: str):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # For now, just store path in id_card_details
    student.id_card_details = document_path
    db.commit()
    db.refresh(student)
    return student
