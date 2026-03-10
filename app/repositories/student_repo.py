from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.student import Student
from app.models.student_enrollment import StudentEnrollment
from app.models.class_model import Class
from app.models.division import Division


async def get_all_students_from_db(db, search, sort_by, limit, offset):

    query = (
        select(Student, StudentEnrollment, Class, Division)
        .join(StudentEnrollment, Student.id == StudentEnrollment.student_id)
        .join(Class, Class.id == StudentEnrollment.class_id)
        .join(Division, Division.id == StudentEnrollment.division_id)
    )

    if search:
        query = query.where(Student.name.ilike(f"%{search}%"))

    if sort_by == "name":
        query = query.order_by(Student.name)
    else:
        query = query.order_by(StudentEnrollment.roll_no)

    query = query.limit(limit).offset(offset)

    result = await db.execute(query)

    return result.all()