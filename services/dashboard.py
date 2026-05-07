from sqlalchemy.orm import Session
from models.student import Student
from fastapi import HTTPException

def get_dashboard_stats(db: Session):
    total_students = db.query(Student).count()
    active_students = db.query(Student).filter(Student.status == "active").count()
    alumni_students = db.query(Student).filter(Student.status == "alumni").count()
    withdrawn_students = db.query(Student).filter(Student.status == "withdrawn").count()

    return {
        "total_students": total_students,
        "active_students": active_students,
        "alumni_students": alumni_students,
        "withdrawn_students": withdrawn_students
    }

def get_chart_data(db: Session):
    # Example: group by status for pie chart
    statuses = db.query(Student.status).all()
    status_counts = {}
    for s in statuses:
        status_counts[s[0]] = status_counts.get(s[0], 0) + 1

    return {"status_distribution": status_counts}
