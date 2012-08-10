import redis
import json
from datetime import datetime
from pyramid.view import view_config
from pyramid.events import ApplicationCreated
from pyramid.events import subscriber
from apscheduler.scheduler import Scheduler
from sqlalchemy import engine_from_config
from sqlalchemy.sql.expression import desc
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
        if queued_player['name'] == player.name and queued_player['found_game_id'] != '':
            return {
                'status': 'success',
                'game_id': queued_player['found_game_id'],
                'game_spot': queued_player['found_game_spot']
            }
        elif queued_player['name'] == player.name:
            break
    else:
        r.lpush(key, json.dumps({
            'id': player.id,
            'name': player.name,
            'found_game_id': '',
            'found_game_spot': ''
        }, sort_keys=True))

    return {
        'status': 'failed'
    }


@view_config(route_name='api_queueme_activate',
             renderer='json')
def queueme_activate(request):
    db = request.db
    player = request.player
    r = redis.Redis()

    game_id = request.GET.get('game_id', None)
    game_spot = request.GET.get('game_spot', None)

    status = 'failed'
    game = db.query(Game).filter_by(id=game_id).first()
    for join in game.joins:
        if join.spot == int(game_spot) and join.player.id == 0L:
            join.player_id = player.id

            r.lrem(key, 0, json.dumps({
                'id': player.id,
                'name': player.name,
                'found_game_id': game_id,
                'found_game_spot': game_spot
            }, sort_keys=True))

            status = 'success'

    db.flush()
    return {
        'status': status,
        'game_id': game_id
    }


@subscriber(ApplicationCreated)
def start_scheduler(event):
    sched = Scheduler()
    sched.start()

    manage_queue(event.app.registry.settings)
    # sched.add_interval_job(manage_queue,
    #                        kwargs={'settings': event.app.registry.settings},
    #                        seconds=2)


def manage_queue(settings=None):
    r = redis.Redis()
    players = r.lrange(key, 0, -1)

    engine = engine_from_config(settings, 'sqlalchemy.')
    maker = sessionmaker(bind=engine, autocommit=True)
    db = maker()

    games = db.query(Game).filter(Game.time > datetime.now()).order_by(desc(Game.time)).all()

    found_joins = []
    for game in games:
        for join in game.joins:
            if join.player.id == 0:
                found_joins.append(join)

    i = 0
    for player in players:
        player = json.loads(player)
        if player['found_game_id'] == '':
            try:
                found_join = found_joins.pop()
                r.lset(key, i, json.dumps({
                    'id': player['id'],
                    'name': player['name'],
                    'found_game_id': found_join.game.id,
                    'found_game_spot': found_join.spot
                }, sort_keys=True))
            except IndexError:
                pass
        i += 1
