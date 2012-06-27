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

    def get_printed_time(self):
        m = "AM"
        hour = self.time.hour
        if hour > 12:
            hour = hour % 12
            m = "PM"

        return hour, self.time.minute, m

    def separate_players(self):
        lefts = []
        rights = []
        for join in self.joins:
            if join.side == 0:
                lefts.append({
                    'id': join.player.id,
                    'name': join.player.name,
                    'pending': 0
                })
            else:
                rights.append({
                    'id': join.player.id,
                    'name': join.player.name,
                    'pending': 0
                })

        notification_item = self.game_invite_notification
        for notification in notification_item.notifications:
            if notification.side == 0:
                lefts.append({
                    'id': notification.player.id,
                    'name': notification.player.name,
                    'pending': 1
                })
            else:
                rights.append({
                    'id': notification.player.id,
                    'name': notification.player.name,
                    'pending': 1
                })

        return lefts, rights

    def __repr__(self):
        return "<Game('%s')>" % (self.id)
