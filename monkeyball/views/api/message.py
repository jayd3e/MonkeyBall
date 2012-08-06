from pyramid.view import view_config
from monkeyball.models.message import Message


@view_config(route_name='api_messages',
             renderer='json',
             request_param='game_id')
def messages(request):
    db = request.db
    game_id = request.GET['game_id']

    messages = db.query(Message).filter_by(game_id=game_id).all()

    messages_json = []
    for message in messages:
        messages_json.append({
            'id': message.id,
            'game_id': message.game_id,
            'player_id': message.player.id,
            'player_name': message.player.name,
            'body': message.body
        })

    return messages_json


@view_config(route_name='api_messages',
             renderer='json',
             request_method='POST',
             request_param='game_id')
def create_message(request):
    db = request.db
    payload = request.json_body
    game_id = request.GET['game_id']

    message = Message(game_id=game_id,
                      player=request.player,
                      body=payload['body'])
    db.add(message)
    db.flush()
    return {
        'id': message.id,
        'game_id': message.game_id,
        'player_id': message.player.id,
        'player_name': message.player.name,
        'body': message.body
    }
