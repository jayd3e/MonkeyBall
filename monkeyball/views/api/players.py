from pyramid.view import view_config
from monkeyball.models.player import Player


@view_config(route_name='api_players',
             renderer='json',
             request_param='s')
def search_players(request):
    db = request.db

    s = request.params['s']
    players = db.query(Player).filter(Player.name.ilike('%' + s + '%'))

    players_json = []
    for player in players:
        if player.id != request.player.id:
            players_json.append({
                'id': player.id,
                'name': player.name
            })

    return players_json
