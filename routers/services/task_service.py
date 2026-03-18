from sqlalchemy.orm import Session
from app import models

def create_task(db: Session, title: str, user_id: int):
    task = models.Task(title=title, user_id=user_id)
    db.add(task)
    db.commit()
    return task

def get_tasks(db: Session):
    return db.query(models.Task).all()
