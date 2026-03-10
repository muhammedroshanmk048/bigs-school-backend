from typing import List

from fastapi import APIRouter ,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.student_schema import StudentResponse
from app.services.student_service import get_all_students

student_router = APIRouter()

@student_router.get("/students", response_model=List[StudentResponse])
async def get_students(db: AsyncSession = Depends(get_db)):
    return await get_all_students(db)