from pydantic import BaseModel, Field

class TaskIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    desc: str
    completed: bool  

class Task(TaskIn):
    id: int
