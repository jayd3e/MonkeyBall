from sqlalchemy import (
    Column,
    String,
    BigInteger
)
from sqlalchemy.ext.associationproxy import association_proxy

from monkeyball.models.base import Base


class Player(Base):
    __tablename__ = 'players'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)

    games = association_proxy('joins', 'game')

    def __repr__(self):
        return "<Player('%s')>" % (self.id)
