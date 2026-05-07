from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Guardian(Base):
    __tablename__ = "guardians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    relation_type = Column(String)  # father, mother, etc.
    priority = Column(Integer, default=1)
    contact_number = Column(String)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="guardians")
