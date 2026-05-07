from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.integration import notify_attendance, assign_fees, record_exam_enrollment, send_notification

router = APIRouter(prefix="/integration", tags=["Integration"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{student_id}/attendance")
def init_attendance(student_id: int, db: Session = Depends(get_db)):
    return notify_attendance(db, student_id)

@router.post("/{student_id}/fees")
def init_fees(student_id: int, db: Session = Depends(get_db)):
    return assign_fees(db, student_id)

@router.post("/{student_id}/exams")
def init_exam(student_id: int, db: Session = Depends(get_db)):
    return record_exam_enrollment(db, student_id)

@router.post("/{student_id}/notify")
def notify_guardians(student_id: int, message: str, db: Session = Depends(get_db)):
    return send_notification(db, student_id, message)

@router.get("/{student_id}/attendance_summary")
def attendance_summary(student_id: int, db: Session = Depends(get_db)):
    # Stub: return fake attendance percentage
    return {"student_id": student_id, "attendance_percentage": 85}

@router.get("/{student_id}/fees_summary")
def fees_summary(student_id: int, db: Session = Depends(get_db)):
    # Stub: return fake fee status
    return {"student_id": student_id, "fees_paid": 12000, "fees_due": 3000}
