from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student, StudentStatus

def update_status(db: Session, student_id: int, new_status: StudentStatus):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Example validation: prevent invalid transitions
    if student.status == StudentStatus.withdrawn and new_status == StudentStatus.active:
        raise HTTPException(status_code=400, detail="Cannot activate a withdrawn student")

    student.status = new_status
    db.commit()
    db.refresh(student)
    return student

from services.validation import validate_promotion_prerequisites

def promote_student(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    validate_promotion_prerequisites(student.status)

    # Example promotion logic: increment academic year
    student.academic_status = f"Promoted-{student.academic_status}"
    db.commit()
    db.refresh(student)
    return student
