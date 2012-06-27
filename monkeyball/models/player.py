from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.ext.association_proxy import association_proxy

from clusterflunk.models.base import Base


class Player(Base):
    __tablename__ = 'players'
    username = Column(String)

    games = association_proxy('joins', 'game')

    def __repr__(self):
        return "<Player('%s')>" % (self.id)
