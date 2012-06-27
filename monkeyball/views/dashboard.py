from pyramid.view import view_config


@view_config(route_name='index',
             renderer='monkeyball:templates/dashboard.mako')
def dashboard(request):
    player = request.player
    db = request.db

    wins = 0
    losses = 0
    ratio = 0

    return {
        'wins': wins,
        'losses': losses,
        'ratio': ratio
    }
