from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.placement import assign_class_section, generate_roll_number

router = APIRouter(prefix="/placement", tags=["Placement"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put("/{student_id}/assign")
def assign_class(student_id: int, class_name: str, section_name: str, db: Session = Depends(get_db)):
    return assign_class_section(db, student_id, class_name, section_name)

@router.put("/{student_id}/roll")
def roll_number(student_id: int, db: Session = Depends(get_db)):
    return generate_roll_number(db, student_id)
