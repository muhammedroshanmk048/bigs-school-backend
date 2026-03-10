from pydantic import BaseModel


class StudentResponse(BaseModel):

    id: int
    name: str
    roll_no: int
    class_name: str
    division_name: str

    class Config:
        from_attributes = True