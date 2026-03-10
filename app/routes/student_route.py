from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.database import get_db
from app.schemas.student_schema import (
    StudentResponse
)

from app.services.student_service import (
    get_all_students
)

student_router = APIRouter()


@student_router.get("/students", response_model=List[StudentResponse])
async def get_students(
    search: Optional[str] = Query(None),
    sort_by: str = Query("roll_no"),
    limit: int = Query(10),
    offset: int = Query(0),
    db: AsyncSession = Depends(get_db)
):

    return await get_all_students(db, search, sort_by, limit, offset)