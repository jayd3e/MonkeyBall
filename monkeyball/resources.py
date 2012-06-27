from pyramid.security import Allow, Authenticated


class Site(object):
    __acl__ = [(Allow, Authenticated, 'logged_in')]

    def __init__(self, request):
        pass
