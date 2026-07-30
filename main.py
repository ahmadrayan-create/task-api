from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="Simple in-memory CRUD to-do list",
    version="1.0.0"
)

from typing import List, Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

# In-memory "database"
tasks: List[Task] = [
    Task(id=1, title="Learn FastAPI", done=False),
    Task(id=2, title="Build CRUD API", done=False),
    Task(id=3, title="Push to GitHub", done=True),
]

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}


class TaskCreate(BaseModel):
    title: str

@app.post("/tasks", status_code=201, response_model=Task)
def create_task(task_in: TaskCreate):
    if not task_in.title or not task_in.title.strip():
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="title is required and cannot be empty")

    new_id = max((t.id for t in tasks), default=0) + 1
    new_task = Task(id=new_id, title=task_in.title.strip(), done=False)
    tasks.append(new_task)
    return new_task