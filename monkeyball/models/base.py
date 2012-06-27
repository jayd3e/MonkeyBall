from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=Base)


def initializeBase(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
