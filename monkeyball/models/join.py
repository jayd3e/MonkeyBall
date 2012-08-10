from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    BigInteger
)
from sqlalchemy.orm import relationship

from monkeyball.models.base import Base


class Join(Base):
    __tablename__ = 'joins'
    game_id = Column(Integer, ForeignKey('games.id'))
    player_id = Column(BigInteger, ForeignKey('players.id'))
    # 0 = left top, 1 = right top, 2 = left bottom, 3 = right bottom
    spot = Column(Integer)

    game = relationship('Game', backref='joins')
    player = relationship('Player', backref='joins')

    def __repr__(self):
        return "<Join('%s')>" % (self.id)
