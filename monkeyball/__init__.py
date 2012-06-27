from pyramid.config import Configurator
from monkeyball.resources import Site

# Models
from monkeyball.models.base import Base
from monkeyball.models.game import Game
from monkeyball.models.join import Join
from monkeyball.models.message import Message
from monkeyball.models.player import Player


def main(global_config, **settings):
    '''Main config function'''
    config = Configurator(settings=settings,
                          root_factory=Site)

    config.add_static_view(name='static', path='monkeyball:static')

    #Routes
    config.add_route('index', '/')
    config.add_route('game_create', '/game/create')
    config.add_route('game', '/game/{id}')

    config.scan('monkeyball')
    return config.make_wsgi_app()
