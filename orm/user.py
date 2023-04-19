from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from base import Base

assignments = Table(
    'assignment', Base.metadata,
    Column('achievement_id', Integer, ForeignKey("achievement.id"), primary_key=True),
    Column('user_id', Integer, ForeignKey("user.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    user_name = Column(String(1000))
    achievements = relationship("Achievement", secondary=assignments)
    # TODO

    def __init__(self, user_id: int, user_name: str):
        self.id = user_id
        self.user_name = user_name
