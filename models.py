from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    id: int
    name: str
    code: str
    description: str
    credits: int
    department: str
    prerequisites: List[str]
    faculty_id: int

class Faculty(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department: str
    specialization: List[str]
    office: str
    office_hours: str