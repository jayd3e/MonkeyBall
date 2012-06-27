from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Boolean
)
from sqlalchemy.ext.associationproxy import association_proxy

from monkeyball.models.base import Base


class Game(Base):
    __tablename__ = 'games'
    completed = Column(Boolean)
    left_score = Column(Integer)
    right_score = Column(Integer)
    # 0 = singles, 1 = doubles
    game_type = Column(Integer)
    time = Column(DateTime)
    created = Column(DateTime)

    players = association_proxy('joins', 'player')

    def side_of_player(self, player_id):
        for join in self.joins:
            if join.player.id is player_id:
                return join.side

    def __repr__(self):
        return "<Game('%s')>" % (self.id)
