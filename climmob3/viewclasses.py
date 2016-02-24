from resources import commonCSS, commonJS, siteScript
from pyramid.security import authenticated_userid
from auth import getUserData
from pyramid.httpexceptions import HTTPFound

class publicView(object):
    def __init__(self, request):
        self.request = request
        self._ = self.request.translate

    def __call__(self):
        commonCSS.need()
        commonJS.need()
        siteScript.need()
        return self.processView()

    def processView(self):
        return {}


class privateView(object):
    def __init__(self, request):
        self.request = request
        self.user = None
        self._ = self.request.translate

    def __call__(self):
        commonCSS.need()
        commonJS.need()
        siteScript.need()

        login = authenticated_userid(self.request)
        self.user = getUserData(login)
        if (self.user == None):
            return HTTPFound(location=self.request.route_url('login'))

        return self.processView()

    def processView(self):
        return {}