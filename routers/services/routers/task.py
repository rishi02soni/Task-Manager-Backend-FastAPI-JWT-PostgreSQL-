from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task.title, user_id=1)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)
