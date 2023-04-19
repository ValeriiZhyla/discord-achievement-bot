from base import Session, engine, Base
from datetime import datetime

from user import User
from achievement import Achievement
from knowledge_base_thread import KnowledgeBaseThread

Base.metadata.create_all(engine)
session = Session()

# achievements
first_post = Achievement(1001, "First post")
founder = Achievement(1002, "Founder")


# users
orator = User(42, "Orator")
orator.achievements.append(first_post)
orator.achievements.append(founder)


john_doe = User(69, "John Doe")


# Knowledge base
thread1 = KnowledgeBaseThread(1, datetime(2023, 3, 7), "How to breath", orator)

# persist
session.add(orator)
session.add(john_doe)
session.add(first_post)
session.add(founder)
session.add(thread1)

# commit
session.commit()
session.close()

