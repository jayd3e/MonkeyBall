from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from monkeyball.models.game import Game
from monkeyball.models.join import Join
from monkeyball.models.notification import GameInviteNotification
from monkeyball.models.notification import Notification


@view_config(route_name='game',
             renderer='monkeyball:templates/game/lobby.mako')
def lobby(request):
    db = request.db
    game_id = request.matchdict['id']
    game = db.query(Game).filter_by(id=game_id).first()

    if request.POST.get('finalize'):
        game.completed = True
        game.left_score = request.POST.get('left_score')
        game.right_score = request.POST.get('right_score')
        game.time = datetime.now()

    players = game.ordered_players

    # Times
    hour, min, m = game.get_printed_time()

    db.flush()
    return {
        "game": game,
        "hour": hour,
        "m": m,
        "players": players
    }


@view_config(route_name='game_create',
             renderer='monkeyball:templates/game/create.mako')
def create(request):
    db = request.db

    if request.POST.get('submit'):
        top_left = request.POST.get('top_left_id')
        top_right = request.POST.get('top_right_id')
        bottom_left = request.POST.get('bottom_left_id')
        bottom_right = request.POST.get('bottom_right_id')

        time = datetime.today()

        minute = int(request.POST.get('min'))
        hour = int(request.POST.get('hour'))
        if request.POST.get('m') == "PM":
            hour += 12

        time = time.replace(hour=hour, minute=minute)
        game = Game(completed=False,
                    left_score=0,
                    right_score=0,
                    game_type=request.POST.get('game_type'),
                    time=time,
                    created=datetime.now())
        db.add(game)

        group_invite_notification = GameInviteNotification(player_id=request.player.id,
                                                           game=game,
                                                           discriminator="game_invite",
                                                           created=datetime.now())
        db.add(group_invite_notification)

        player_ids = [top_left, top_right, bottom_left, bottom_right]
        for i in range(4):
            send_notification(request,
                              group_invite_notification,
                              player_ids[i],
                              game,
                              i)
        db.flush()
        return HTTPFound('/game/%s' % game.id)
    elif request.POST.get('cancel'):
        return HTTPFound('/')

    # Current time
    m = "AM"
    hour = datetime.now().hour
    min = datetime.now().minute
    if hour > 12:
        hour = hour % 12
        m = "PM"

    return {
        'hour': hour,
        'min': min,
        'm': m
    }


def send_notification(request, notification_item, player_id, game, spot):
    # player_id is equal to current player's id
    if int(player_id) == request.player.id:
        join = Join(player_id=int(player_id),
                    game=game,
                    spot=spot)
        request.db.add(join)
    # player_id is equal to the ringer id
    elif int(player_id) == 0:
        join = Join(player_id=int(player_id),
                    game=game,
                    spot=spot)
        request.db.add(join)
    else:
        notification = Notification(player_id=int(player_id),
                                    notification_item=notification_item,
                                    spot=spot)
        request.db.add(notification)


@view_config(route_name='game_join')
def join(request):
    db = request.db
    id = request.matchdict['id']

    game_invite_notification = db.query(GameInviteNotification).filter_by(game_id=id).first()
    notification = db.query(Notification).filter_by(player_id=request.player.id,
                                                    notification_item_id=game_invite_notification.id).first()

    join = Join(player_id=int(notification.player.id),
                game_id=game_invite_notification.game.id,
                spot=notification.spot)
    db.add(join)

    db.delete(notification)
    db.flush()
    return HTTPFound('/game/' + id)
