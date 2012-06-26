from pyramid.view import view_config


@view_config(route_name='index',
             renderer='monkeyball:templates/dashboard.mako')
def dashboard(request):
    return {}
