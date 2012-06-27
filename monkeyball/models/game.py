from sqlalchemy import (
    Column,
    DateTime,
    Integer
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.association_proxy import association_proxy

from clusterflunk.models.base import Base


class Game(Base):
    __tablename__ = 'games'
    # 0 = complete, 1 = scheduled
    completed = Column(Integer)
    left_score = Column(Integer)
    right_score = Column(Integer)
    # 0 = singles, 1 = doubles
    game_type = Column(Integer)
    time = Column(DateTime)
    created = Column(DateTime)

    messages = relationship('Message')
    players = association_proxy('joins', 'player')

    def __repr__(self):
        return "<Game('%s')>" % (self.id)
