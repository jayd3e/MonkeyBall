from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.ext.associationproxy import association_proxy

from monkeyball.models.base import Base


class Player(Base):
    __tablename__ = 'players'
    username = Column(String)

    games = association_proxy('joins', 'game')

    def __repr__(self):
        return "<Player('%s')>" % (self.id)
