from typing import Optional
from pydantic import BaseModel, constr, EmailStr
from datetime import date

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str]
    due_date: date

class TaskUpdate(BaseModel):
    status: str

class TaskRead(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    due_date: date
    status: str
