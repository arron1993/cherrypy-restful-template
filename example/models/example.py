from sqlalchemy import Column, Integer, String, UniqueConstraint

from example.models import Base


class Example(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    name = Column(String)
