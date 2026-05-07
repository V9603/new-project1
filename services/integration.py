from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student

def notify_attendance(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # Stub: integrate with attendance module
    return {"message": f"Attendance initialized for {student.full_name}"}

def assign_fees(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # Stub: integrate with fees module
    return {"message": f"Fees assigned for {student.full_name}"}

def record_exam_enrollment(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # Stub: integrate with exams module
    return {"message": f"Exam enrollment created for {student.full_name}"}

def send_notification(db: Session, student_id: int, message: str):
    student = db.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # Stub: integrate with communication module
    return {"message": f"Notification sent to guardians of {student.full_name}: {message}"}
