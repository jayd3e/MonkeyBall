from pyramid.events import subscriber
from pyramid.events import BeforeRender


@subscriber(BeforeRender)
def add_globals(event):
    player = event['request'].player

    if player:
        notifications = player.notifications
        event['notifications'] = notifications
