from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.status import update_status
from models.student import StudentStatus

router = APIRouter(prefix="/status", tags=["Status"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put("/{student_id}/change")
def change_status(student_id: int, new_status: StudentStatus, db: Session = Depends(get_db)):
    return update_status(db, student_id, new_status)

@router.put("/{student_id}/promote")
def promote(student_id: int, db: Session = Depends(get_db)):
    from services.status import promote_student
    return promote_student(db, student_id)
