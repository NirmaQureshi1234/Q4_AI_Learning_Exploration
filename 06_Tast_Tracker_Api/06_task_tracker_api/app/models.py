from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class Task(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    due_date: date
    status: str
