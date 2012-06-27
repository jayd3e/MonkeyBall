from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from monkeyball.models.base import Base


class Message(Base):
    __tablename__ = 'messages'
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    body = Column(String(300))

    game = relationship('Game', backref="messages")
    player = relationship('Player', backref='messages')

    def __repr__(self):
        return "<Message('%s')>" % (self.id)
