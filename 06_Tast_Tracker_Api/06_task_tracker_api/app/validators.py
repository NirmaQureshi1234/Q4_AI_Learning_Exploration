from pydantic import validator
from datetime import date
from app.models import Task

class TaskWithValidation(Task):
    @validator("due_date")
    def check_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date must be today or in the future")
        return value
