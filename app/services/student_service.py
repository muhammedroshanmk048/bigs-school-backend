from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.student_repo import get_all_students_from_db

async def get_all_students(db : AsyncSession):
    rows = await get_all_students_from_db(db)
    if not rows:
        raise HTTPException(status_code=404, detail="No students found")
    return rows