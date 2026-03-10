from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.student import Student

async def get_all_students_from_db(db : AsyncSession):
    result = await db.execute(select(Student))
    students = result.scalars().all()
    return students
