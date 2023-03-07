from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from base import Base
from orm.user import User


class KnowledgeBaseThread(Base):
    __tablename__ = "knowledge_base_thread"
    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    created_at = Column(DateTime())
    owner = relationship("User", backref="knowledge_base_thread")

    def __init__(self, thread_id: int, created_at: datetime, thread_name: str, owner: User):
        self.id = thread_id
        self.created_at = created_at
        self.name = thread_name
        self.owner = owner
