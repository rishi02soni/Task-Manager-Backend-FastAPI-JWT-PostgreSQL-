from fastapi import FastAPI
from app.routers import user, task

app = FastAPI(title="Task Manager API")

// 
app.include_router(user.router)
app.include_router(task.router)
