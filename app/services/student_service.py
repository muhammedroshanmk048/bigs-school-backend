from fastapi import HTTPException

from app.repositories.student_repo import get_all_students_from_db


async def get_all_students(db, search, sort_by, limit, offset):

    rows = await get_all_students_from_db(db, search, sort_by, limit, offset)

    if not rows:
        raise HTTPException(status_code=404, detail="No students found")

    response = []

    for student, enrollment, class_obj, division in rows:

        response.append({
            "id": student.id,
            "name": student.name,
            "roll_no": enrollment.roll_no,
            "class_name": class_obj.name,
            "division_name": division.name
        })
    return response