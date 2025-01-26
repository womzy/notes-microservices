from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://username:password@postgres:5432/mydatabase"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

class NoteIn(BaseModel):
    text: str

class NoteOut(NoteIn):
    id: int

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
@app.post("/notes/", response_model=NoteOut)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}

@app.get("/notes/", response_model=List[NoteOut])
async def read_notes():
    query = notes.select()
    results = await database.fetch_all(query)
    return results


