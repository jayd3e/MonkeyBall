from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from monkeyball.models.base import Base


class Join(Base):
    __tablename__ = 'joins'
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(Integer, ForeignKey('players.id'))

    game = relationship('Game', backref='joins')
    player = relationship('Player', backref='joins')

    def __repr__(self):
        return "<Join('%s')>" % (self.id)