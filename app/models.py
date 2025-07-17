from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base

class TelegramMessage(Base):
    __tablename__ = "telegram_messages"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer)
    date = Column(DateTime)
    message = Column(Text)
    sender_name = Column(String)
    channel = Column(String)

class Prepared(Base):
    __tablename__ = "prepared"
    __table_args__ = {"schema": "telegram_db"}

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    channel = Column(String)
    message = Column(Text)

class ImageDetection(Base):
    __tablename__ = "image_detections"
    __table_args__ = {"schema": "telegram_db"}

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    detected_object = Column(String)
    confidence = Column(String)
    message_id = Column(Integer)

class FctImageDetection(Base):
    __tablename__ = "fct_image_detections"
    __table_args__ = {"schema": "telegram_db"}

    id = Column(Integer, primary_key=True)
    object_name = Column(String)
    frequency = Column(Integer)