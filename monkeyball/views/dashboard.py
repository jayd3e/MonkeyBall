from datetime import datetime
from pyramid.view import view_config
from monkeyball.models.game import Game
from sqlalchemy.sql.expression import desc


def get_leaderboard():
    pass


@view_config(route_name='index',
             renderer='monkeyball:templates/dashboard.mako')
def dashboard(request):
    player = request.player
    db = request.db

    wins = 0
    losses = 0
    ratio = 0

    # Wins/Losses
    for game in player.games:
        # Boolean representing a left win
        left = None

        if game.left_score > game.right_score:
            left = True
        else:
            left = False

        if (left is True and game.side_of_player(player.id) == 0) or \
           (left is False and game.side_of_player(player.id) == 1):
            wins += 1
        else:
            losses += 1

    # Ratio
    if losses != 0:
        ratio = round(wins / float(losses), 2)

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

    leaders = get_leaderboard()

    return {
        'wins': wins,
        'losses': losses,
        'ratio': ratio,
        'upcoming_games': upcoming_games,
        'previous_games': previous_games,
        'leaders': leaders
    }
