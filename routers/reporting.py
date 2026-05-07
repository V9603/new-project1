from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.reporting import fetch_academic_history, generate_summary

router = APIRouter(prefix="/reporting", tags=["Reporting"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{student_id}/history")
def student_history(student_id: int, db: Session = Depends(get_db)):
    return fetch_academic_history(db, student_id)

@router.get("/summary")
def student_summary(db: Session = Depends(get_db)):
    return generate_summary(db)
