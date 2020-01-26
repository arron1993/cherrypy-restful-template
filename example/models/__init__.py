from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = './example.db'

engine = create_engine(f'sqlite:///{DB_PATH}')

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)
