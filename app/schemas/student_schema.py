from pydantic import BaseModel

class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: str

    class Config:
        from_attributes = True