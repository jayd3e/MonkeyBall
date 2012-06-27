from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    BigInteger,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from monkeyball.models.base import Base


class Notification(Base):
    __tablename__ = 'notifications'

    player_id = Column(BigInteger, ForeignKey('players.id'))
    notification_item_id = Column(Integer, ForeignKey('notification_items.id'))
    side = Column(Integer)

    player = relationship('Player', backref='notification')
    notification_item = relationship('NotificationItem', backref="notifications")

    def __repr__(self):
        return "<Notification('%s')>" % (self.id)


class NotificationItem(Base):
    __tablename__ = 'notification_items'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

    def __repr__(self):
        return "<NotificationItem('%s')>" % (self.id)


class GameInviteNotification(NotificationItem):
    __tablename__ = 'game_invite_notifications'

    id = Column(Integer, ForeignKey('notification_items.id'), primary_key=True)
    player_id = Column(BigInteger, ForeignKey('players.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    __mapper_args__ = {'polymorphic_identity': 'game_invite'}

    inviter = relationship('Player')
    game = relationship('Game', backref=backref("game_invite_notification", uselist=False))

    def __repr__(self):
        return "<GameInviteNotification('%s')>" % (self.id)


class GameStartNotification(NotificationItem):
    __tablename__ = 'game_start_notifications'

    id = Column(Integer, ForeignKey('notification_items.id'), primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    __mapper_args__ = {'polymorphic_identity': 'game_start'}

    game = relationship('Game')

    def __repr__(self):
        return "<GameStartNotification('%s')>" % (self.id)
