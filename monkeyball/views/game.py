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

    lefts, rights = game.separate_players()

    # Times
    hour, min, m = game.get_printed_time()

    db.flush()
    return {
        "game": game,
        "hour": hour,
        "m": m,
        "lefts": lefts,
        "rights": rights
    }


@view_config(route_name='game_create',
             renderer='monkeyball:templates/game/create.mako')
def create(request):
    db = request.db

    if request.POST.get('submit'):
        lefts = request.POST.getall('left_id')
        rights = request.POST.getall('right_id')

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

        for left in lefts:
            notification = Notification(player_id=int(left),
                                        notification_item=group_invite_notification,
                                        side=0)
            db.add(notification)

        for right in rights:
            notification = Notification(player_id=int(right),
                                        notification_item=group_invite_notification,
                                        side=1)
            db.add(notification)

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

@view_config(route_name='game_join')
def create(request):
    db = request.db
    id = request.matchdict['id']

    game_invite_notification = db.query(GameInviteNotification).filter_by(game_id=id)
    notification = db.query(Notification).filter_by(player_id=request.player.id,
                                                    notification_item_id=game_invite_notification.id)

    join = Join(player_id=int(notification.player.id),
                game_id=notification.game.id,
                side=notification.side)
    db.add(join)

    db.delete(notification)
    db.flush()
    return HTTPFound('/game/' + id)
