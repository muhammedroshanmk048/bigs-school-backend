from fastapi import FastAPI
from app.database import Base, engine
from app.routes.student_route import student_router
from app.models import student
from app.models import class_model
from app.models import division
from app.models import academic_year
from app.models import student_enrollment

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized")

@app.get("/")
def home():
    return {"message": "BIGS School API running"}

app.include_router(student_router)