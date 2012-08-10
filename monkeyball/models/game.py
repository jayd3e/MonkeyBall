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

    def spot_of_player(self, player_id):
        for join in self.joins:
            if join.player.id is player_id:
                return join.spot

    def get_printed_time(self):
        m = "AM"
        hour = self.time.hour
        if hour > 12:
            hour = hour % 12
            m = "PM"

        return hour, self.time.minute, m

    @property
    def ordered_players(self):
        players = [None, None, None, None]
        for join in self.joins:
            join.player.accepted = True
            players[join.spot] = join.player

        for player in players:
            if player is None:
                for notification in self.game_invite_notification.notifications:
                    notification.player.accepted = False
                    players[notification.spot] = notification.player
        return players

    def __repr__(self):
        return "<Game('%s')>" % (self.id)
