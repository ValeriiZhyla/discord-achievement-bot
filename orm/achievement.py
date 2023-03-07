from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from base import Base


class Achievement(Base):
    __tablename__ = "achievement"
    id = Column(Integer, primary_key=True)
    name = Column(String(1000))

    def __init__(self, achievement_id: int, achievement_name: str):
        self.id = achievement_id
        self.name = achievement_name
