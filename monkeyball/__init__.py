from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from monkeyball.resources import Site
from monkeyball.security import groupfinder
from monkeyball.request import MonkeyBallRequest

# Models
from monkeyball.models.base import initializeBase
from monkeyball.models.base import Base
from monkeyball.models.game import Game
from monkeyball.models.join import Join
from monkeyball.models.message import Message
from monkeyball.models.player import Player
from monkeyball.models.notification import Notification
from monkeyball.models.notification import NotificationItem
from monkeyball.models.notification import GameInviteNotification
from monkeyball.models.notification import GameStartNotification

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


def main(global_config, **settings):
    '''Main config function'''
    engine = engine_from_config(settings, 'sqlalchemy.')
    initializeBase(engine)
    # NOTE: A transaction is created by default in postgres, so I have added the
    # 'autocommit' kwarg so that I don't have to deal with transactions for
    # the moment.  Remove it once I have pyramid_tm & zope.sqlalchemy implemented.
    maker = sessionmaker(bind=engine, autocommit=True)
    settings['db.sessionmaker'] = maker

    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    session_factory = UnencryptedCookieSessionFactoryConfig('1h209asf093nf930fni23f0fb29401', cookie_max_age=3600)
    config = Configurator(settings=settings,
                          root_factory=Site,
                          request_factory=MonkeyBallRequest,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          session_factory=session_factory)

    # Security
    config.set_default_permission('logged_in')

    # Static view
    config.add_static_view(name='static', path='monkeyball:static')

    # Facebook integration
    config.include('velruse.providers.facebook')
    config.add_facebook_login_from_settings(prefix='facebook.')

    # Routes
    config.add_route('index', '/')
    config.add_route('queue', '/queue')
    config.add_route('game_create', '/game/create')
    config.add_route('game_join', '/game/join/{id}')
    config.add_route('game', '/game/{id}')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # Api
    config.add_route('api_players', '/api/players')
    config.add_route('api_queueme', '/api/queueme')
    config.add_route('api_messages', '/api/messages')

    config.scan('monkeyball')
    return config.make_wsgi_app()
