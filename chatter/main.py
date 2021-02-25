"""
`main.py` is the main file.
"""

# Load dotenv before anything
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from chatter import tasks_api
from chatter import db


app = FastAPI(name="Chatter")
db.init(app)  # Initialize database code

@app.get("/")
async def read_root():
    return {"message": "Chatter"}

app.include_router(tasks_api.router, prefix="/tasks")
