from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from base import Base


class Achievement(Base):
    __tablename__ = "knowledge_base_threads"
    id = Column(Integer, primary_key=True)
    achievement_name = Column(String(1000))

    def __init__(self, achievement_id: int, achievement_name: str):
        self.id = achievement_id
        self.achievement_name = achievement_name
