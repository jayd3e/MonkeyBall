from velruse import login_url
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget
)
from monkeyball.models.player import Player


@view_config(route_name='login',
             renderer='monkeyball:templates/auth/login.mako',
             permission='__no_permission_required__')
def login_view(request):
    return {
        'login_url': login_url(request, 'facebook')
    }


@view_config(context='velruse.AuthenticationComplete',
             permission='__no_permission_required__')
def login_complete_view(request):
    db = request.db
    profile = request.context.profile

    userid = None
    for account in profile['accounts']:
        if account['domain'] == 'facebook.com':
            userid = int(account['userid'])
            break

    if userid is not None:
        player = db.query(Player).filter_by(id=userid).first()
        if player is None:
            player = Player(id=userid,
                            name=profile['displayName'])
            db.add(player)

        db.flush()
        remember(request, player.id)
        return HTTPFound(location="/")


@view_config(context='velruse.AuthenticationDenied',
             renderer='monkeyball:templates/dashboard.mako')
def login_denied_view(request):
    return {
        'result': 'denied',
    }


@view_config(route_name='logout',
             permission='__no_permission_required__')
def logout(request):
    forget(request)
    return HTTPFound(location='/')
