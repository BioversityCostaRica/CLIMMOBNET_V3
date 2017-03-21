from models import DBSession,User as userModel,Country,Sector, Project
from encdecdata import decodeData

import urllib, hashlib


#User class Used to store information about the user
class User(object):
    def __init__(self, login, password, fullName, organization, email,country, sector, about ,groups=None):

        default = "identicon"
        size = 45
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

        self.login = login
        self.password = password
        self.groups = groups or []
        self.fullName = fullName
        self.organization = organization
        self.email = email
        self.country = country
        self.sector = str(sector)
        self.gravatarURL = gravatar_url
        if about is None:
            self.about = ""
        else:
            self.about = about

    def check_password(self, passwd):
        return checkLogin(self.login,passwd)

    def getGravatarUrl(self,size):
        default = "identicon"
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        return gravatar_url
    def getCntyName(self):
        return getCountryName(self.country)
    def getSectName(self):
        return getSectorName(self.sector)
    def getAPIKey(self):
        key = ""
        mySession = DBSession()
        result = mySession.query(userModel).filter_by(user_name = self.login).first()
        if not result is None:
            key = result.user_apikey
        mySession.close()
        return key
    def updateGravatarURL(self):
        default = "identicon"
        size = 45
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        self.gravatarURL = gravatar_url

# #We need to change this so the users are loaded from the database
# def add_user(login,fullName, organization, email,country, sector,about, **kw):
#     config.USERS[login] = User(login,"",fullName,organization,email,country,sector,about, **kw)
#     return config.USERS[login]
#
# #Root authorization we only have two set of groups. AuthUsers allowed to edit and admin
# class Root(object):
#     __acl__ = [
#         (Allow, 'g:authusers', 'edit'),
#         (Allow, 'g:admin', ALL_PERMISSIONS),
#     ]
#
#     def __init__(self, request):
#         self.request = request
#
# def groupfinder(userid, request):
#     user = config.USERS.get(userid)
#     if user:
#         return ['g:%s' % g for g in user.groups]

def getUserData(user):
    res = None
    mySession = DBSession()
    result = mySession.query(userModel).filter_by(user_name = user).filter_by(user_active = 1).first()
    if not result is None:
        res = User(result.user_name,"",result.user_fullname,result.user_organization,result.user_email,result.user_cnty,result.user_sector,result.user_about)
    mySession.close()
    return res




def checkLogin(user,password):
    mySession = DBSession()
    result = mySession.query(userModel).filter_by(user_name = user).filter_by(user_active = 1).first()
    if result is None:
        mySession.close()
        return False
    else:
        cpass = decodeData(result.user_password)
        if cpass == password:
            mySession.close()
            return True
        else:
            mySession.close()
            return False

def getCountryName(cnty_cod):
    res = ""
    mySession = DBSession()
    result = mySession.query(Country).filter_by(cnty_cod = cnty_cod).first()
    if not result is None:
        res = result.cnty_name
    mySession.close()
    return res

def getSectorName(sector_cod):
    res = ""
    mySession = DBSession()
    result = mySession.query(Sector).filter_by(sector_cod = sector_cod).first()
    if not result is None:
        res = result.sector_name
    mySession.close()
    return res

