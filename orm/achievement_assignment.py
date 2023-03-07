from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from base import Base


class Achievement(Base):
    __tablename__ = "assignment"
    achievement_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)

    def __init__(self, achievement_id: int, user_id: int):
        self.achievement_id = achievement_id
        self.user_id = user_id
