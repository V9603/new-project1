from sqlalchemy.orm import Session
from models.student import Student, StatusHistory
from fastapi import HTTPException

def fetch_academic_history(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    history = db.query(StatusHistory).filter(StatusHistory.student_id == student_id).all()
    return {
        "student": student.full_name,
        "admission_number": student.admission_number,
        "current_status": student.status,
        "history": [
            {"old": h.old_status, "new": h.new_status, "date": h.effective_date}
            for h in history
        ]
    }

def generate_summary(db: Session):
    total_students = db.query(Student).count()
    active_students = db.query(Student).filter(Student.status == "active").count()
    alumni_students = db.query(Student).filter(Student.status == "alumni").count()

    return {
        "total_students": total_students,
        "active_students": active_students,
        "alumni_students": alumni_students
    }
