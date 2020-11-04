from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect


class LoginRequiredMiddleware(object):
    """
    Require Login middleware. If enabled, each Django-powered page will require authentication.
    If an anonymous user requests a page, the user is redirected to the login page set by LOGIN_URL.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_path = getattr(settings, 'LOGIN_URL')

        print("init - get_response = ", get_response)
        print("init - login_path = ", self.login_path)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("request.path = ", request.path)
        print("self.login_path = ", self.login_path)
        print("request.user.is_anonymous = ", request.user.is_anonymous)

        if request.path != self.login_path and request.user.is_anonymous:
            return HttpResponseRedirect('%s?next=%s' % (self.login_path, request.path))

        response = self.get_response(request)

        # print("response = ", response)

        # Code to be executed for each request/response after
        # the view is called.

        return response