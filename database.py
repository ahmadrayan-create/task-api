from sqlmodel import Session, SQLModel, create_engine, select
from models import Task

sqlite_file_name = "tasks.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def seed_if_empty():
    with Session(engine) as session:
        existing = session.exec(select(Task)).first()
        if not existing:
            session.add(Task(title="Buy milk", done=False))
            session.add(Task(title="Study FastAPI", done=False))
            session.add(Task(title="Ship assignment", done=True))
            session.commit()

def get_session():
    with Session(engine) as session:
        yield session