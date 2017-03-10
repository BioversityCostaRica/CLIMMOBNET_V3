
from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPError
from auth import getUserData
from pyramid.security import authenticated_userid

from viewclasses import publicView, privateView

from pyramid.security import forget
from pyramid.security import remember
from pyramid.httpexceptions import HTTPFound

from resources import  projectResources,ProjectJS,FlotChars, siteFlotScript, Select2JS, basicCSS, projectJS,ProjectTechnologiesResources, indexJS,CreateProjectJS,settingsResources


import helpers
from dbuserfunctions import addUser, getUserPassword, changeUserPassword, otherUserHasEmail, updateProfile, addToLog, getUserLog, userExists, getUserInfo
from maintenance import show_projects,getLastProject
from querys_countries import ProjectBelongsToUser
from querys_project_technologies import searchTechnologiesInProject
from querys_project_tecnologies_alias import  AliasSearchTechnologyInProject, AliasExtraSearchTechnologyInProject

from utilityfnc import valideForm

from view_projecttechnologies import return_projectTechnologies_view
from view_projectcontries import return_projectcontries_view
from view_projectenumerator import return_projectenumerator_view

@view_config(context=HTTPError, renderer='templates/500.html')
def error_view(request):
    basicCSS.need()
    request.response.status = '500 Error'
    return {}


@notfound_view_config(renderer='templates/404.html')
def notFound_view(request):
    basicCSS.need()
    request.response.status = '404 Not Found'
    return {}


@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    loc = request.route_url('home')
    return HTTPFound(location=loc, headers=headers)


@view_config(route_name='home', renderer='templates/home/index.html')
class home_view(publicView):
    def processView(self):

        login = authenticated_userid(self.request)
        user = getUserData(login)
        dataworking = {}
        dataworking['project_cod'] = None
        indexJS.need()
        settingsResources.need()
        valueSettings = self.request.cookies.get('_SETTINGS_')
        menuSettings = self.request.cookies.get('_MENUSETTINGS_')

        if (user == None):
            FlotChars.need()
            siteFlotScript.need()
        else:
            if 'btn_action' in self.request.POST:
                dataworking['project_cod'] = self.request.POST.get('txt_cod_project','')



            if self.request.cookies.get('_PROJECT_') == None :

                dataworking['project_cod']= getLastProject(login)
            else:

                if self.request.cookies.get('_PROJECT_') == 'createbionew':
                    dataworking['project_cod'] = ""
                else:
                    data = ProjectBelongsToUser(login, self.request.cookies.get('_PROJECT_'))
                    if not data:

                        dataworking['project_cod']= getLastProject(login)
                    else:

                        dataworking['project_cod'] =self.request.cookies.get('_PROJECT_')


            if dataworking['project_cod'] == "":
                ProjectJS.need()
                projectResources.need()
                projectJS.need()
                CreateProjectJS.need()


        ProjectTechnologiesResources.need()

        #print "_________________"+session['project']
        return { 'activeUser': user, 'helpers': helpers,'project_data': show_projects(login),'dataworking':dataworking,
                 'searchTechnologiesInProject':searchTechnologiesInProject(login,dataworking['project_cod']),
                 'AliasTechnologyInProject': AliasSearchTechnologyInProject,
                 'AliasExtraTechnologyInProject': AliasExtraSearchTechnologyInProject,
                 'SearchEnumerator': helpers.searchEnumerator(login,dataworking['project_cod']),
                 'CountriesProject':helpers.CountriesProject(login,dataworking['project_cod']),



                 'var':return_projectTechnologies_view(login, dataworking['project_cod']),
                 'projectCountries': return_projectcontries_view(login,dataworking['project_cod']),
                 'projectenumerator': return_projectenumerator_view(login,dataworking['project_cod']),
                 'Active': valueSettings,
                 'menuActive':menuSettings



               }


@view_config(route_name='login', renderer='templates/home/login.html')
class login_view(publicView):
    def processView(self):
        next = self.request.params.get('next') or self.request.route_url('home')
        login = ''
        did_fail = False
        if 'submit' in self.request.POST:
            login = self.request.POST.get('login', '')
            passwd = self.request.POST.get('passwd', '')
            user = getUserData(login)
            if not user == None and user.check_password(passwd):
                headers = remember(self.request, login)

                response = HTTPFound(location=next, headers=headers)
                response.set_cookie('_LOCALE_', value='es', max_age=31536000)
                #response.set_cookie('_PROJECT_',value=getLastProject(login),max_age=31536000)
                return response



            did_fail = True

        return {'login': login, 'failed_attempt': did_fail, 'next': next}


@view_config(route_name='policy', renderer='templates/home/policy.html')
class policy_view(publicView):
    def processView(self):
        return {}


@view_config(route_name='register', renderer='templates/home/register.html')
class register_view(publicView):
    def processView(self):

        Select2JS.need()
        data = {}
        error_summary = {}

        data["user_name"] = ""
        data["user_fullname"] = ""
        data["user_password"] = ""
        data["user_organization"] = ""
        data["user_email"] = ""
        data["user_cnty"] = ""
        data["user_sector"] = ""
        data["user_policy"] = "no"

        if 'submit' in self.request.POST:
            errors = False
            data["user_name"] = self.request.POST.get('user_name', '')
            data["user_fullname"] = self.request.POST.get('user_fullname', '')
            data["user_organization"] = self.request.POST.get('user_organization', '')
            data["user_email"] = self.request.POST.get('user_email', '')
            data["user_cnty"] = self.request.POST.get('user_cnty', '')
            data["user_sector"] = self.request.POST.get('user_sector', '')
            if not self.request.POST.get('user_policy', 'False') == "False":
                data["user_policy"] = "True"
            else:
                data["user_policy"] = "False"
            data["user_password"] = self.request.POST.get('user_password', '')
            data["user_password2"] = self.request.POST.get('user_password2', '')

            errors, error_summary = valideForm(data)

            if errors:
                return {'data': data, 'helpers': helpers, 'error_summary': error_summary}
            else:
                res, message = addUser(data)
                if res:

                    user = getUserData(data["user_name"])
                    if not user == None and user.check_password(data["user_password"]):
                        addToLog(user.login, 'PRF', self._("Welcome to Climmob"))
                        headers = remember(self.request, data["user_name"])
                        return HTTPFound(location=self.request.route_url('home'), headers=headers)
                    else:
                        error_summary["createError"] = self._("User created but unable to login!")
                else:
                    error_summary["createError"] = self._("Unable to create user",
                                                          default='Unable to create user: ${user}',
                                                          mapping={'user': message})

        return {'data': data, 'helpers': helpers, 'error_summary': error_summary}


@view_config(route_name='profile', renderer='templates/user/profile.html')
class profile_view(privateView):
    def processView(self):

        totacy = len(getUserLog(self.user.login))
        return {'activeUser': self.user, "totacy": totacy, 'helpers': helpers}


@view_config(route_name='userinfo', renderer='templates/user/user_info.html')
class userinfo_view(privateView):
    def processView(self):
        userid = self.request.matchdict['userid']
        if not userExists(userid):
            raise HTTPNotFound()

        totacy = len(getUserLog(userid))
        return {'activeUser': self.user, "totacy": totacy, 'helpers': helpers, 'displayUser': userid,
                'userInfo': getUserInfo(userid)}


@view_config(route_name='editprofile', renderer='templates/user/edit_profile.html')
class editprofile_view(privateView):
    def processView(self):
        data = {}
        error_summary = {}

        totacy = len(getUserLog(self.user.login))

        data["user_fullname"] = self.user.fullName
        data["user_about"] = self.user.about
        data["user_organization"] = self.user.organization
        data["user_email"] = self.user.email
        data["user_cnty"] = self.user.country
        data["user_sector"] = self.user.sector

        passChanged = False
        profileUpdated = False

        if (self.request.method == 'POST'):
            if 'saveprofile' in self.request.POST:
                data["user_fullname"] = self.request.POST.get('user_fullname', '')
                data["user_organization"] = self.request.POST.get('user_organization', '')
                data["user_email"] = self.request.POST.get('user_email', '')
                data["user_cnty"] = self.request.POST.get('user_cnty', '')
                data["user_sector"] = self.request.POST.get('user_sector', '')
                data["user_about"] = self.request.POST.get('user_about', '')
                if data["user_fullname"] != "":
                    if data["user_email"] != "":
                        if data["user_organization"] != "":
                            if not otherUserHasEmail(self.user.login, data["user_email"]):
                                if updateProfile(self.user.login, data):
                                    self.user.email = data["user_email"]
                                    self.user.organization = data["user_organization"]
                                    self.user.fullName = data["user_fullname"]
                                    self.user.country = data["user_cnty"]
                                    self.user.sector = data["user_sector"]
                                    self.user.about = data["user_about"]
                                    self.user.updateGravatarURL()
                                    addToLog(self.user.login, 'PRF', "Updated profile")
                                    totacy = len(getUserLog(self.user.login))
                                    profileUpdated = True
                                else:
                                    error_summary["ChangeProfile"] = self._("Cannot update profile")
                            else:
                                error_summary["ChangeProfile"] = self._("Other user is using the same email adddress")
                        else:
                            error_summary["ChangeProfile"] = self._("Organization cannot be empty")
                    else:
                        error_summary["ChangeProfile"] = self._("Email cannot be empty")
                else:
                    error_summary["ChangeProfile"] = self._("Full name cannot be empty")

            if 'changepass' in self.request.POST:
                if self.request.POST.get('user_password1', '') == getUserPassword(self.user.login):
                    if self.request.POST.get('user_password2', '') != "":
                        if self.request.POST.get('user_password2', '') == self.request.POST.get('user_password3', ''):
                            if changeUserPassword(self.user.login, self.request.POST.get('user_password2', '')):
                                addToLog(self.user.login, 'PRF', "Changed password")
                                totacy = len(getUserLog(self.user.login))
                                passChanged = True
                            else:
                                error_summary["ChangePass"] = self._("Cannot change password")
                        else:
                            error_summary["ChangePass"] = self._("New password and re-type are not equal")
                    else:
                        error_summary["ChangePass"] = self._("New password cannot be empty")
                else:
                    error_summary["ChangePass"] = self._("The current password is not valid")

            return {'activeUser': self.user, 'data': data, 'helpers': helpers, 'error_summary': error_summary,
                    'passChanged': passChanged, 'profileUpdated': profileUpdated, "totacy": totacy}

        return {'activeUser': self.user, 'data': data, 'helpers': helpers, 'error_summary': error_summary,
                'passChanged': passChanged, 'profileUpdated': profileUpdated, "totacy": totacy}


@view_config(route_name='useractivity', renderer='templates/user/activity.html')
class useractivity_view(privateView):
    def processView(self):
        limit = True
        if "all" in self.request.params:
            if self.request.params["all"] == "True":
                limit = False
        activities = getUserLog(self.user.login, limit)
        return {'activeUser': self.user, "activities": activities, "totacy": len(activities)}








