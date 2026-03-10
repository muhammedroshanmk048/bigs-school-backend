from sqlalchemy import Boolean, Column, DateTime, Integer, String, func, text
from app.database import Base


class AcademicYear(Base):
    __tablename__ = "academic_years"

    id = Column(Integer, primary_key=True)
    year_name = Column(String)
    is_active = Column(Boolean,server_default=text("true"))
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),onupdate=func.now())