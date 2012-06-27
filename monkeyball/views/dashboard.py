from datetime import datetime
from pyramid.view import view_config
from sqlalchemy.sql.expression import desc
from retools.cache import CacheRegion
from retools.cache import cache_region
from monkeyball.models.game import Game
from monkeyball.models.player import Player


CacheRegion.add_region("short_term", expires=300)


@cache_region('short_term')
def get_leaderboard(request):
    db = request.db

    players = []
    results = db.query(Player).all()
    for player in results:
        player.wins, player.losses, player.ratio = player.wins_losses()
        players.append(player)

    players.sort(key=lambda x: x.wins, reverse=True)
    return players


@view_config(route_name='queue',
             renderer='monkeyball:templates/dashboard.mako')
@view_config(route_name='index',
             renderer='monkeyball:templates/dashboard.mako')
def dashboard(request):
    player = request.player
    db = request.db

    wins, losses, ratio = player.wins_losses()

    # Upcoming games
    upcoming_games = []
    results = db.query(Game).filter(Game.time > datetime.now()).order_by(desc(Game.time)).limit(4)
    for game in results:
        game.hour, game.min, game.m = game.get_printed_time()
        game.lefts, game.rights = game.separate_players()
        upcoming_games.append(game)

    # Previous Games
    previous_games = []
    results = db.query(Game).filter(Game.time < datetime.now()).order_by(desc(Game.time)).limit(4)
    for game in results:
        game.hour, game.min, game.m = game.get_printed_time()
        game.lefts, game.rights = game.separate_players()
        previous_games.append(game)

    leaders = get_leaderboard(request)

    return {
        'wins': wins,
        'losses': losses,
        'ratio': ratio,
        'upcoming_games': upcoming_games,
        'previous_games': previous_games,
        'leaders': leaders
    }
