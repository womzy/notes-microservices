from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# In-memory storage for tasks (for simplicity)
tasks_db = {}

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    tasks_db[task_id] = task.dict()
    return tasks_db[task_id]

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return [Task(**task) for task in tasks_db.values()]

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task(**task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task.dict()
    return tasks_db[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task deleted successfully"}
