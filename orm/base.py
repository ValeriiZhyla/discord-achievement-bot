from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config
from sqlalchemy.ext.declarative import declarative_base

# Establish database connection
engine = create_engine(f'postgresql://{config.DB_HOST}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()