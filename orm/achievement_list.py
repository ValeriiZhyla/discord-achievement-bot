from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from base import Base


class Achievement(Base):
    __tablename__ = "achievement"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    created_at = Column(DateTime())
    thread_name = Column(String(1000))
    owner_name = Column(String(200))

    def __init__(self, thread_id: int, owner_id: int, created_at: datetime, thread_name: str, owner_name: str):
        self.id = thread_id
        self.owner_id = owner_id
        self.created_at = created_at
        self.thread_name = thread_name
        self.owner_name = owner_name
