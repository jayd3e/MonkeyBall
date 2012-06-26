# Exceptions views.  Such as views that deal with server overload and
# NotFound pages.
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPForbidden
from pyramid.view import view_config


@view_config(context=HTTPNotFound,
             permission='__no_permission_required__',
             renderer='monkeyball:templates/exceptions/not_found.mako')
def not_found(request):
    title = 'Page Not Found'
    return {'title': title}


@view_config(context=HTTPForbidden,
             permission='__no_permission_required__')
def forbidden(request):
    return HTTPFound(location='/login')
