from pydantic import BaseModel
from datetime import datetime

class TelegramMessageSchema(BaseModel):
    id: int
    message_id: int
    date: datetime
    message: str
    sender_name: str
    channel: str

    class Config:
        from_attributes = True

class PreparedSchema(BaseModel):
    id: int
    date: datetime
    channel: str
    message: str

    class Config:
        from_attributes = True

class ImageDetectionSchema(BaseModel):
    id: int
    date: datetime
    detected_object: str
    confidence: str
    message_id: int

    class Config:
        from_attributes = True

class FctImageDetectionSchema(BaseModel):
    id: int
    object_name: str
    frequency: int

    class Config:
        from_attributes = True
