from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.profile import update_profile, upload_document

router = APIRouter(prefix="/profile", tags=["Profile"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put("/{student_id}/update")
def update_student_profile(student_id: int, updates: dict, db: Session = Depends(get_db)):
    return update_profile(db, student_id, updates)

@router.put("/{student_id}/document")
def upload_student_document(student_id: int, document_path: str, db: Session = Depends(get_db)):
    return upload_document(db, student_id, document_path)
