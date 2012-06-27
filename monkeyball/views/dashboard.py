from pyramid.view import view_config


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
        ratio = wins / float(losses)

    # Upcoming games

    # Previous Games

    return {
        'wins': wins,
        'losses': losses,
        'ratio': ratio
    }
