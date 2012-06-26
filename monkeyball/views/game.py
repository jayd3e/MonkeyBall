from pyramid.view import view_config


@view_config(route_name='game',
             renderer='monkeyball:templates/game/lobby.mako')
def lobby(request):
    return {}


@view_config(route_name='game_create',
             renderer='monkeyball:templates/game/create.mako')
def create(request):
    return {}


@view_config(route_name='queueing',
             renderer='monkeyball:templates/game/queueing.mako')
def queueing(request):
    return {}
