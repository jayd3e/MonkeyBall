from pyramid.view import view_config


@view_config(route_name='api_queueme',
             renderer='json')
def queueme(request):
    db = request.db
    player = request.player
