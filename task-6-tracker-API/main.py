from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Dict, List
from datetime import date
from typing import Annotated

app = FastAPI()

# Global in-memory data stores
USERS: Dict[int, "UserRead"] = {}
TASKS: Dict[int, "Task"] = {}

# Pydantic Models
class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class Task(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    status: str
    due_date: date

    @validator('due_date')
    def due_date_cannot_be_in_past(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past.")
        return v

# API Endpoints

# Create a user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(USERS) + 1
    new_user = UserRead(id=user_id, **user.dict())
    USERS[user_id] = new_user
    return new_user

# Get a user by ID
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    task.id = len(TASKS) + 1
    TASKS[task.id] = task
    return task

# Get a task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]

# Update task status
@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    if status not in ["pending", "in-progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
    TASKS[task_id].status = status
    return TASKS[task_id]

# Get all tasks for a user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task.user_id == user_id]




