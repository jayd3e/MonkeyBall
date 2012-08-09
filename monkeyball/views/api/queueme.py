import redis
import json
from pyramid.view import view_config
from pyramid.events import ApplicationCreated
from pyramid.events import subscriber
from apscheduler.scheduler import Scheduler
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from monkeyball.models.game import Game

key = 'monkeyball:queued:players'


@view_config(route_name='api_queueme',
             renderer='json')
def queueme(request):
    player = request.player
    r = redis.Redis()

    queued_players = r.lrange(key, 0, -1)
    for queued_player in queued_players:
        queued_player = json.loads(queued_player)
        if queued_player['name'] == player.name:
            break
    else:
        r.lpush(key, json.dumps({
            'id': player.id,
            'name': player.name,
            'found_game_id': ''
        }, sort_keys=True))


@view_config(route_name='api_queueme_activate',
             renderer='json')
def queueme_activate(request):
    db = request.db
    player = request.player
    r = redis.Redis()

    r.lrem(key, 0, json.dumps({
        'id': player.id,
        'name': player.name,
        'found_game_id': ''
    }, sort_keys=True))


@subscriber(ApplicationCreated)
def start_scheduler(event):
    sched = Scheduler()
    sched.start()

    sched.add_interval_job(manage_queue,
                           kwargs={'settings': event.app.registry.settings},
                           seconds=2)


def manage_queue(settings=None):
    r = redis.Redis()
    players = r.lrange(key, 0, -1)
    print(players)

    engine = engine_from_config(settings, 'sqlalchemy.')
    maker = sessionmaker(bind=engine, autocommit=True)
    db = maker()

    games = db.query(Game).filter_by()
