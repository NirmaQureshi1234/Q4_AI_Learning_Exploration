from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, UserRead, TaskCreate, TaskRead, TaskUpdate
from app.storage import USERS, TASKS
from datetime import date

app = FastAPI()

user_id_counter = 1
task_id_counter = 1


@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = UserRead(id=user_id_counter, **user.dict())
    USERS[user_id_counter] = user_data
    user_id_counter += 1
    return user_data


@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]


@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    if task.due_date < date.today():
        raise HTTPException(status_code=400, detail="Due date must be today or in the future")
    new_task = TaskRead(id=task_id_counter, status="pending", **task.dict())
    TASKS[task_id_counter] = new_task
    task_id_counter += 1
    return new_task


@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]


@app.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, update: TaskUpdate):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    if update.status not in ["pending", "in_progress", "done"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    task = TASKS[task_id]
    updated_task = task.copy(update={"status": update.status})
    TASKS[task_id] = updated_task
    return updated_task


@app.get("/users/{user_id}/tasks", response_model=list[TaskRead])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task.user_id == user_id]
