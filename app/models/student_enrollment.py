from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func, text
from app.database import Base

class StudentEnrollment(Base):
    __tablename__ = "student_enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    division_id = Column(Integer, ForeignKey("divisions.id"))
    academic_year_id = Column(Integer, ForeignKey("academic_years.id"))
    roll_no = Column(Integer)
    is_active = Column(Boolean,server_default=text("true"))
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),onupdate=func.now())