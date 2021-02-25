import os
from databases import Database
from fastapi.applications import FastAPI
import sqlalchemy


database = Database(os.getenv("DATABASE_URL_FASTAPI"))
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=100)),
    sqlalchemy.Column("desc", sqlalchemy.Text),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

def init(app: FastAPI):
    """Initialization function for database code"""

    engine = sqlalchemy.create_engine(
        os.getenv("DATABASE_URL_FASTAPI"), connect_args={"check_same_thread": False}
    )
    metadata.create_all(engine)

    @app.on_event("startup")
    async def connect_to_db():
        await database.connect()

    @app.on_event("shutdown")
    async def disconnect_from_db():
        await database.disconnect()