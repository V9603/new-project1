from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.dashboard import get_dashboard_stats, get_chart_data

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stats")
def dashboard_stats(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)

@router.get("/charts")
def dashboard_charts(db: Session = Depends(get_db)):
    return get_chart_data(db)

from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/stats")
def get_stats():
    return {
        "total_students": 120,
        "active_students": 100,
        "alumni_students": 15,
        "withdrawn_students": 5,
    }

@router.get("/charts")
def get_charts():
    return {
        "status_distribution": {
            "Active": 100,
            "Alumni": 15,
            "Withdrawn": 5,
        }
    }
