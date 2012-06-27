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

    def wins_losses(self):
        wins = 0
        losses = 0
        ratio = 0

        for game in self.games:
            # Boolean representing a left win
            left = None

            if game.left_score > game.right_score:
                left = True
            else:
                left = False

            if (left is True and game.side_of_player(self.id) == 0) or \
               (left is False and game.side_of_player(self.id) == 1):
                wins += 1
            else:
                losses += 1

        if losses != 0:
            ratio = round(wins / float(losses), 2)

        return wins, losses, ratio

    def __repr__(self):
        return "<Player('%s')>" % (self.id)
