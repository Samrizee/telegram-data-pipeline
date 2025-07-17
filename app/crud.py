from sqlalchemy.orm import Session
from . import models

def get_top_objects(db: Session, limit: int = 10):
    return db.query(models.FctImageDetection).order_by(models.FctImageDetection.frequency.desc()).limit(limit).all()

def get_channel_activity(db: Session, channel_name: str):
    return db.query(models.Prepared).filter(models.Prepared.channel == channel_name).all()

def search_messages(db: Session, query: str):
    return db.query(models.Prepared).filter(models.Prepared.message.ilike(f"%{query}%")).all()
