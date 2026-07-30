from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select

from database import create_db_and_tables, get_session, seed_if_empty
from models import Task

app = FastAPI(
    title="Task API",
    description="SQLite-backed CRUD to-do list",
    version="2.0.0",
)


@app.on_event("startup")
def on_startup():
  create_db_and_tables()
  seed_if_empty()


@app.get("/")
def root():
  return {"name": "Task API", "version": "2.0", "endpoints": ["/tasks"]}


@app.get("/health")
def health():
  return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def get_tasks(session: Session = Depends(get_session)):
  return session.exec(select(Task)).all()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, session: Session = Depends(get_session)):
  task = session.get(Task, task_id)
  if not task:
    raise HTTPException(
        status_code=404, detail={"error": f"Task {task_id} not found"}
    )
  return task


class TaskCreate(BaseModel):
  title: str


@app.post("/tasks", status_code=201, response_model=Task)
def create_task(task_in: TaskCreate, session: Session = Depends(get_session)):
  if not task_in.title or not task_in.title.strip():
    raise HTTPException(status_code=400, detail="title cannot be empty")

  db_task = Task(title=task_in.title.strip(), done=False)
  session.add(db_task)
  session.commit()
  session.refresh(db_task)
  return db_task


class TaskUpdate(BaseModel):
  title: Optional[str] = None
  done: Optional[bool] = None


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int, task_in: TaskUpdate, session: Session = Depends(get_session)
):
  db_task = session.get(Task, task_id)
  if not db_task:
    raise HTTPException(
        status_code=404, detail={"error": f"Task {task_id} not found"}
    )

  if task_in.title is not None:
    if not task_in.title.strip():
      raise HTTPException(status_code=400, detail="title cannot be empty")
    db_task.title = task_in.title.strip()

  if task_in.done is not None:
    db_task.done = task_in.done

  session.add(db_task)
  session.commit()
  session.refresh(db_task)
  return db_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
  db_task = session.get(Task, task_id)
  if not db_task:
    raise HTTPException(
        status_code=404, detail={"error": f"Task {task_id} not found"}
    )

  session.delete(db_task)
  session.commit()
  return None