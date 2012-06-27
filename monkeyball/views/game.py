from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from monkeyball.models.game import Game
from monkeyball.models.join import Join


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

    lefts = []
    rights = []
    for join in game.joins:
        if join.side == 0:
            lefts.append({
                'id': join.player.id,
                'name': join.player.name
            })
        else:
            rights.append({
                'id': join.player.id,
                'name': join.player.name
            })

    # Times
    m = "AM"
    hour = game.time.hour
    if hour > 12:
        hour = hour % 12
        m = "PM"

    # Figure out game type to change lobby style
    if game.game_type == 0:
        game_type = " singles"
    else:
        game_type = " doubles"

    db.flush()
    return {
        "game": game,
        "hour": hour,
        "m": m,
        "game_type": game_type,
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

        hour = int(request.POST.get('hour'))
        if request.POST.get('m') == "PM":
            hour += 12

        time = time.replace(hour=hour)
        game = Game(completed=False,
                    left_score=0,
                    right_score=0,
                    game_type=request.POST.get('game_type'),
                    time=time,
                    created=datetime.now())
        db.add(game)

        for left in lefts:
            join = Join(player_id=int(left),
                        game=game,
                        side=0)
            db.add(join)

        for right in rights:
            join = Join(player_id=int(left),
                        game=game,
                        side=1)
            db.add(join)

        db.flush()
        return HTTPFound('/game/%s' % game.id)
    elif request.POST.get('cancel'):
        return HTTPFound('/')

    m = 0
    hour = datetime.now().hour
    min = datetime.now().minute
    if hour > 12:
        hour = hour % 12
        m = 1

    return {
        'hour': hour,
        'min': min,
        'm': m
    }
