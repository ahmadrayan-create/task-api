from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from database import create_db_and_tables, get_session, seed_if_empty
from models import Task

app = FastAPI(
    title="Task API",
    description="SQLite-backed CRUD to-do list",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
  create_db_and_tables()
  seed_if_empty()


@app.get("/")
def root():
  return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


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
    raise HTTPException(status_code=404, detail={"error": "Task not found"})
  return task