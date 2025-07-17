from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

app = FastAPI()

@app.get("/api/reports/top-objects", response_model=list[schemas.FctImageDetectionSchema])
def top_objects(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_top_objects(db, limit)

@app.get("/api/channels/{channel_name}/activity", response_model=list[schemas.PreparedSchema])
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    return crud.get_channel_activity(db, channel_name)

@app.get("/api/search/messages", response_model=list[schemas.PreparedSchema])
def search(query: str, db: Session = Depends(get_db)):
    return crud.search_messages(db, query)
