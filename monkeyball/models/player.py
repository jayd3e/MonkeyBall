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
    notifications = association_proxy('notification', 'notification_item')

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

            if ((left is True and game.spot_of_player(self.id) in [0, 2]) or \
               (left is False and game.spot_of_player(self.id) in [1, 3])) and \
                game.completed == True:
                wins += 1
            elif game.completed == True:
                losses += 1

        if losses != 0:
            ratio = round(wins / float(losses), 2)

        return wins, losses, ratio

    def __repr__(self):
        return "<Player('%s')>" % (self.id)
