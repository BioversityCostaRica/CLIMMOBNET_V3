import pprint

from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPError
from auth import getUserData
from pyramid.security import authenticated_userid

from climmob3.encdecdata import encodeData
from viewclasses import publicView, privateView

from pyramid.security import forget
from pyramid.security import remember
from pyramid.httpexceptions import HTTPFound

from resources import  dataTables,ColorPickerJs,ProjectJS,EnumeratorJS,FlotChars, siteFlotScript, Select2JS, basicCSS, projectJS, technologyResources, questionproject, \
    addTechAutoShow, updateTechAutoShow, deleteTechAutoShow, technologyaliasResources, addTechAliasAutoShow, \
    updateTechAliasAutoShow, deleteTechAliasAutoShow, addProjectAutoShow, updateProjectAutoShow, deleteProjectAutoShow, \
    ProjectCountriesResources, addCountryAutoShow, updateContactCountryAutoShow, deleteCountryProjectAutoShow, \
    ProjectTechnologiesResources, ProjectAliasTechnologiesResources, addAliasTechPrjAutoShow, \
    ProjectEnumeratorsResources, addEnumeratorAutoShow,updateProjectEnumeratorAutoShow,deleteProjectEnumeratorAutoShow,\
    ProjectQuestionResources,addQuestionAutoShow,updateQuestionAutoShow,QuestionsInProject

import helpers
from dbuserfunctions import addUser, getUserPassword, changeUserPassword, otherUserHasEmail, updateProfile, addToLog, \
    getUserLog, userExists, getUserInfo
from maintenance import getUserTechs, findTechInLibrary, addTechnology, updateTechnology, removeTechnology, \
    show_projects, out_technologies, showProjectTechnologies
from querys_alias import techBelongsToUser, findTechalias, addTechAlias, getTechsAlias, updateAlias, removeAlias
from querys_project import searchproject, addproject, updateProject, deleteProject
from querys_countries import allCountries, CountriesProject, addProjectCountry, ProjectBelongsToUser, \
    updateContactCountry, removeContactCountry
from querys_project_technologies import searchTechnologies, searchTechnologiesInProject, addTechnologyProject, \
    deleteTechnologyProject
from querys_project_tecnologies_alias import AliasSearchTechnology, AliasSearchTechnologyInProject, \
    AliasExtraSearchTechnologyInProject, PrjTechBelongsToUser, AddAliasTechnology, deleteAliasTechnologyProject, \
    addTechAliasExtra
from querys_enumerator import searchEnumerator,addProjectEnumerator,SearchEnumeratorForId,mdfProjectEnumerator,dltProjectEnumerator,SearchPasswordForUser
from querys_questions import UserQuestion,addQuestion,updateQuestion
from querys_projectquestions import Prj_UserQuestion, AddGroup,UserGroups,changeGroupOrder
from utilityfnc import valideForm

import xlwt


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
        if (user == None):
            FlotChars.need()
            siteFlotScript.need()

        return {'activeUser': user, 'helpers': helpers}


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


@view_config(route_name='technologies', renderer='templates/project/technologies.html')
class maintenance_products(privateView):
    def processView(self):
        technologyResources.need()
        error_summary = {}

        newTech = False
        techEdited = False
        techDeleted = False
        data = {}

        if (self.request.method == 'POST'):
            if 'btn_add_pro' in self.request.POST:
                techName = self.request.POST.get('txt_add_pro', '')
                data["techName"] = techName;

                existInGenLibrary = findTechInLibrary('bioversity', techName)
                if techName != "":
                    if existInGenLibrary == False:

                        existInPersLibrary = findTechInLibrary(self.user.login, techName)
                        if existInPersLibrary == False:
                            print "Hay que agregarlo"
                            added, message = addTechnology(self.user.login, techName)
                            if not added:
                                error_summary = {'dberror': message}
                            else:
                                newTech = True
                        else:
                            error_summary = {
                                'exists': self._("This technology already exists in your personal library")}
                    else:
                        error_summary = {'exists': self._("This technology already exists in the generic library")}
                else:
                    error_summary = {'nameempty': self._('The name of the tecnology cannot be empy')}
                if len(error_summary) > 0:
                    addTechAutoShow.need()

            if 'btn_update_pro' in self.request.POST:

                techName = self.request.POST.get('txt_update_name', '')
                techID = self.request.POST.get('txt_update_id', '')

                data["techName"] = techName;
                data["techID"] = techID;

                existInGenLibrary = findTechInLibrary('bioversity', techName)
                if techName != "":
                    if existInGenLibrary == False:
                        existInGenLibrary = findTechInLibrary(self.user.login, techName)
                        if existInGenLibrary == False:
                            updated, message = updateTechnology(self.user.login, techID, techName)
                            if not updated == True:
                                error_summary = {'dberror': message}
                                addTechAutoShow.need()
                            else:
                                techEdited = True
                        else:
                            error_summary = {
                                'exists': self._("This technology already exists in your personal library")}
                    else:
                        error_summary = {'exists': self._("This technology already exists in the generic library")}
                else:
                    error_summary = {'nameempty': self._("The name of the tecnology cannot be empy")}

                if len(error_summary) > 0:
                    updateTechAutoShow.need()

            if 'btn_delete_pro' in self.request.POST:
                techID = self.request.POST.get('txt_delete_id', '')
                data["techID"] = techID;
                removed, message = removeTechnology(self.user.login, techID)
                if not removed:
                    error_summary = {'dberror': message}
                else:
                    techDeleted = True
                if len(error_summary) > 0:
                    deleteTechAliasAutoShow.need()

        return {'data': data, 'newTech': newTech, 'techEdited': techEdited, 'techDeleted': techDeleted,
                'error_summary': error_summary, 'activeUser': self.user, 'userTechs': getUserTechs(self.user.login),
                'genTechs': getUserTechs('bioversity'), 'PrjTechnologies': showProjectTechnologies(self.user.login),
                'helpers': helpers}


@view_config(route_name='techalias', renderer='templates/project/technologiesalias.html')
class techalias(privateView):
    def processView(self):
        technologyaliasResources.need()

        techid = self.request.matchdict['techid']
        error_summary = {}
        newTechalias = False
        techEditedalias = False
        techDeletedalias = False
        data = {}
        dataworking = {}
        # We verified that the technology of the URL belongs to the user session
        data = techBelongsToUser(self.user.login, techid)
        if not data:
            data = techBelongsToUser('bioversity', techid)
            if not data:
                raise HTTPNotFound()
            else:
                return {'data': data,  'activeUser': self.user, 'TechAlias': getTechsAlias(techid),'maintenanceavailable': False}
        else:
            # button click
            if (self.request.method == 'POST'):
                # if da click the button to add alias
                if 'btn_add_alias' in self.request.POST:
                    # get the field value
                    techaliasName = self.request.POST.get('txt_add_alias', '')
                    # verify that it is not empty
                    if techaliasName != "":
                        # add the object
                        dataworking["tech_id"] = techid
                        dataworking["alias_name"] = techaliasName;
                        # verify that there is no
                        existAlias = findTechalias(dataworking)
                        if existAlias == False:

                            # add the alias
                            added, message = addTechAlias(dataworking)
                            if not added:
                                # capture the error
                                error_summary = {'dberror': message}
                            else:
                                # show success message
                                newTechalias = True
                        else:
                            # error
                            error_summary = {'exists': self._("This alias already exists in the technology")}
                    else:
                        # error
                        error_summary = {'nameempty': self._("The name of the alias cannot be empy")}
                    # window display error adding
                    if len(error_summary) > 0:
                        addTechAliasAutoShow.need()

                if 'btn_update_alias' in self.request.POST:
                    # get the field value
                    techaliasid = self.request.POST.get('txt_update_id', '')
                    techaliasnewname = self.request.POST.get('txt_update_name', '')

                    if techaliasnewname != '':
                        # add the object
                        dataworking['tech_id'] = techid
                        dataworking['alias_name'] = techaliasnewname
                        dataworking['alias_id'] = techaliasid
                        # verify that there is no
                        existAlias = findTechalias(dataworking)
                        if existAlias == False:
                            # update alias
                            update, message = updateAlias(dataworking)
                            if not update:
                                # capture the error
                                error_summary = {'dberror': message}
                            else:
                                # show success message
                                techEditedalias = True
                        else:
                            # error
                            error_summary = {'exists': self._("This alias already exists in the technology")}
                    else:
                        # error
                        error_summary = {'nameempty': self._("The name of the alias cannot be empy")}

                    # window display error update
                    if len(error_summary) > 0:
                        updateTechAliasAutoShow.need()

                if 'btn_delete_alias' in self.request.POST:
                    alias_id = self.request.POST.get('txt_delete_id', '')

                    dataworking['alias_id'] = alias_id
                    removed, message = removeAlias(dataworking)
                    if not removed:
                        error_summary = {'dberror': message}
                    else:
                        techDeletedalias = True

                    if len(error_summary) > 0:
                        deleteTechAutoShow.need()

            return {'data': data, 'dataworking': dataworking, 'newTechalias': newTechalias,
                    'techEditedalias': techEditedalias, 'techDeletedalias': techDeletedalias,
                    'error_summary': error_summary, 'activeUser': self.user, 'TechAlias': getTechsAlias(techid),'maintenanceavailable': True}


@view_config(route_name='project', renderer='templates/project/project.html')
class project_view(privateView):
    def processView(self):
        ProjectJS.need()
        projectJS.need()
        dataTables.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)

        error_summary = {}
        datacountries = {}
        newproject = False
        projectEdited = False
        projectDelete = False

        dataworking = {}
        if (self.request.method == 'POST'):
            if 'btn_addNewProject' in self.request.POST:
                # get the field value
                new_code = self.request.POST.get('newproject_code', '')
                new_name = self.request.POST.get('newproject_name', '')
                new_description = self.request.POST.get('newpeoject_description', '')
                new_otro = self.request.POST.get('newproject_tag', '')
                new_investigator = self.request.POST.get('newproject_principal_investigator', '')
                new_mail_address = self.request.POST.get('newproject_mail_address', '')

                # add the object
                dataworking['user_name'] = self.user.login
                dataworking['project_cod'] = new_code
                dataworking['project_name'] = new_name
                dataworking['project_abstract'] = new_description
                dataworking['project_tags'] = new_otro
                dataworking['project_pi'] = new_investigator
                dataworking['project_piemail'] = new_mail_address

                if new_code != '':

                    exitsproject = searchproject(dataworking)

                    if not exitsproject:
                        print 'no exite'
                        # add the project
                        added, message = addproject(dataworking)
                        if not added:
                            # capture the error
                            error_summary = {'dberror': message}
                        else:
                            # show success message
                            newproject = True
                    else:
                        error_summary = {'exitsproject': self._("A project already exists with this code.")}

                else:
                    # error
                    error_summary = {'codempty': self._("The project code can't be empty")}

                # window display error add
                if len(error_summary) > 0:
                    addProjectAutoShow.need()

            if 'btn_modifyProject' in self.request.POST:

                upd_code = self.request.POST.get('updproject_code', '')
                upd_name = self.request.POST.get('updproject_name', '')
                upd_description = self.request.POST.get('updproject_description', '')
                upd_otro = self.request.POST.get('updproject_tag', '')
                upd_investigator = self.request.POST.get('updproject_principal_investigator', '')
                upd_mail_address = self.request.POST.get('updproject_mail_address', '')

                dataworking['user_name'] = self.user.login
                dataworking['project_cod'] = upd_code
                dataworking['project_name'] = upd_name
                dataworking['project_abstract'] = upd_description
                dataworking['project_tags'] = upd_otro
                dataworking['project_pi'] = upd_investigator
                dataworking['project_piemail'] = upd_mail_address

                update, message = updateProject(dataworking)

                if not update:
                    # capture error
                    error_summary = {'dberror': message}
                else:
                    projectEdited = True

                # window display error add
                if len(error_summary) > 0:
                    updateProjectAutoShow.need()

            if 'btn_deleteProject' in self.request.POST:
                project_cod = self.request.POST.get('project_code', '')

                dataworking['user_name'] = self.user.login
                dataworking['project_cod'] = project_cod

                delete, message = deleteProject(dataworking)

                if not delete:
                    error_summary = {'dberror': message}
                else:
                    projectDelete = True

                # window display error add
                if len(error_summary) > 0:
                    deleteProjectAutoShow.need()


        return {'activeUser': self.user, 'project_data': show_projects(user.login), 'dataworking': dataworking,
                'error_summary': error_summary, 'newproject': newproject, 'projectEdited': projectEdited,
                'projectDelete': projectDelete, 'helper': helpers}


@view_config(route_name='prjcnty', renderer='templates/project/projectcountries.html')
class projectCountries_view(privateView):
    def processView(self):
        ProjectCountriesResources.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)
        projectid = self.request.matchdict['projectid']
        error_summary = {}
        newcountryproject = False
        contactcountryEdited = False
        projectcountryDelete = False
        dataworking = {}

        data = ProjectBelongsToUser(user.login, projectid)
        if not data:
            raise HTTPNotFound()
        else:

            if (self.request.method == 'POST'):

                if 'btn_add_country' in self.request.POST:

                    cnty_cod = self.request.POST.get('txt_cnty_cod', '')
                    cnty_contact = self.request.POST.get('txt_add_cnty', '')

                    dataworking['cnty_cod'] = cnty_cod
                    dataworking['cnty_contact'] = cnty_contact
                    dataworking['project_cod'] = projectid
                    dataworking['user_name'] = self.user.login
                    if cnty_contact != '':
                        added, message = addProjectCountry(dataworking)
                        if not added:
                            # capture the error
                            error_summary = {'dberror': message}
                        else:
                            # show success message
                            newcountryproject = True
                    else:
                        error_summary = {'contactempty': self._("The contact name can't be empty")}

                    # window display error add
                    if len(error_summary) > 0:
                        addCountryAutoShow.need()

                if 'btn_modifyContactCountry' in self.request.POST:
                    cnty_cod = self.request.POST.get('upd_cnty_cod', '')
                    cnty_contact = self.request.POST.get('txt_upd_cnty_contact', '')

                    dataworking['cnty_cod'] = cnty_cod
                    dataworking['cnty_contact'] = cnty_contact
                    dataworking['project_cod'] = projectid
                    dataworking['user_name'] = self.user.login

                    if cnty_contact != '':
                        upd, message = updateContactCountry(dataworking)

                        if not upd:
                            error_summary = {'dberror': message}
                        else:
                            contactcountryEdited = True
                    else:
                        error_summary = {'contactempty': self._("The contact name can't be empty")}

                    if len(error_summary) > 0:
                        updateContactCountryAutoShow.need()
                if 'btn_deleteContactCountry' in self.request.POST:
                    cnty_cod = self.request.POST.get('delete_cnty_cod', '')

                    dataworking['cnty_cod'] = cnty_cod
                    dataworking['project_cod'] = projectid
                    dataworking['user_name'] = self.user.login

                    delete, message = removeContactCountry(dataworking)

                    if not delete:
                        error_summary = {'dberror': message}
                    else:
                        projectcountryDelete = True

                    if len(error_summary) > 0:
                        deleteCountryProjectAutoShow.need()

            return {'activeUser': self.user, 'newcountryproject': newcountryproject,
                    'contactcountryEdited': contactcountryEdited, 'projectcountryDelete': projectcountryDelete,
                    'dataworking': dataworking, 'error_summary': error_summary,
                    'Countries': allCountries(projectid, self.user.login),
                    'PrjCnty': CountriesProject(self.user.login, projectid)}


@view_config(route_name='prjtech', renderer='templates/project/projecttechnologies.html')
class projectTechnologies_view(privateView):
    def processView(self):
        ProjectTechnologiesResources.need()

        error_summarydlt = {}
        error_summaryadd = {}
        projectid = self.request.matchdict['projectid']
        newTechnologyProject = False
        dltTechnologyProject = False

        data = ProjectBelongsToUser(self.user.login, projectid)
        if not data:
            raise HTTPNotFound()
        else:

            if (self.request.method == 'POST'):

                if 'btn_save_technologies' in self.request.POST:
                    included_technologies = self.request.POST.get('txt_technologies_included', '')
                    excluded_technologies = self.request.POST.get('txt_technologies_excluded', '')

                    if included_technologies != '':

                        part = included_technologies.split(',')

                        for element in part:
                            attr = element.split('_')
                            # attr - 0 - element
                            # attr - 1 - id
                            # attr - 2 - status
                            if attr[2] == 'new':
                                add, message = addTechnologyProject(self.user.login, projectid, attr[1])
                                if not add:
                                    error_summaryadd = {'dberror': message}
                                else:
                                    newTechnologyProject = True
                    else:
                        newTechnologyProject = 'Empty'

                    if excluded_technologies != '':

                        part = excluded_technologies.split(',')

                        for element in part:
                            attr = element.split('_')
                            # attr - 0 - element
                            # attr - 1 - id
                            # attr - 2 - status
                            if attr[2] == 'exist':
                                delete, message = deleteTechnologyProject(self.user.login, projectid, attr[1])
                                if not delete:
                                    error_summarydlt = {'dberror': message}
                                else:
                                    dltTechnologyProject = True
                    else:
                        dltTechnologyProject = 'Empty'

            return {'activeUser': self.user, 'error_summaryadd': error_summaryadd, 'error_summarydlt': error_summarydlt,
                    'dltTechnologyProject': dltTechnologyProject, 'newTechnologyProject': newTechnologyProject,
                    'TechnologiesUser': searchTechnologies(self.user.login, projectid),
                    'TechnologiesInProject': searchTechnologiesInProject(self.user.login, projectid)}


@view_config(route_name='prjtechalias', renderer='templates/project/projecttechnologiesalias.html')
class PrjTechAlias(privateView):
    def processView(self):
        ProjectAliasTechnologiesResources.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)

        projectid = self.request.matchdict['projectid']
        technologyid = self.request.matchdict['tech_id']
        error_summarydlt = {}
        error_summaryadd = {}
        error_summaryaddextra = {}
        newAliasTechnologyProject = False
        dltAliasTechnologyProject = False
        dataworking = {}

        data = PrjTechBelongsToUser(user.login, projectid, technologyid)
        if not data:
            raise HTTPNotFound()
        else:

            if (self.request.method == 'POST'):

                if 'btn_save_technologies_alias' in self.request.POST:
                    included_technologies_alias = self.request.POST.get('txt_technologiesalias_included', '')
                    excluded_technologies_alias = self.request.POST.get('txt_technologiesalias_excluded', '')

                    print included_technologies_alias
                    print ""
                    print excluded_technologies_alias

                    if included_technologies_alias != '':

                        part = included_technologies_alias.split(',')

                        for element in part:
                            attr = element.split('_')
                            # attr - 0 - element
                            # attr - 1 - id
                            # attr - 2 - status
                            if attr[2] == 'new':
                                dataworking['user_name'] = user.login
                                dataworking['project_cod'] = projectid
                                dataworking['tech_id'] = technologyid
                                dataworking['alias_id'] = attr[1]

                                add, message = AddAliasTechnology(dataworking)
                                if not add:
                                    error_summaryadd = {'dberror': message}
                                else:
                                    newAliasTechnologyProject = True
                    else:
                        newAliasTechnologyProject = 'Empty'

                    if excluded_technologies_alias != '':

                        part = excluded_technologies_alias.split(',')

                        for element in part:
                            attr = element.split('_')
                            # attr - 0 - element
                            # attr - 1 - id
                            # attr - 2 - status
                            if attr[2] == 'exist':
                                delete, message = deleteAliasTechnologyProject(user.login, projectid, technologyid,
                                                                               attr[1])
                                if not delete:
                                    error_summarydlt = {'dberror': message}
                                else:
                                    dltAliasTechnologyProject = True
                    else:
                        dltAliasTechnologyProject = 'Empty'

                if 'btn_add_alias' in self.request.POST:

                    alias_name = self.request.POST.get('txt_add_alias', '')

                    if alias_name != "":
                        # add the object
                        dataworking['user_name'] = user.login
                        dataworking['project_cod'] = projectid
                        dataworking['tech_id'] = technologyid
                        dataworking['alias_name'] = alias_name
                        # verify that there is no
                        existAlias = findTechalias(dataworking)
                        if existAlias == False:

                            # add the alias
                            added, message = addTechAliasExtra(dataworking)
                            if not added:
                                # capture the error
                                error_summaryaddextra = {'dberror': message}
                            else:
                                # show success message
                                newTechalias = True
                        else:
                            # error
                            error_summaryaddextra = {'exists': self._("This alias already exists in the technology")}
                    else:
                        # error
                        error_summaryaddextra = {'nameempty': self._("The name of the alias cannot be empy")}
                    # window display error adding
                    if len(error_summaryaddextra) > 0:
                        addAliasTechPrjAutoShow.need()

                    print alias_name

            return {'activeUser': self.user, 'dataworking': dataworking, 'error_summaryaddextra': error_summaryaddextra,
                    'dltAliasTechnologyProject': dltAliasTechnologyProject, 'error_summarydlt': error_summarydlt,
                    'newAliasTechnologyProject': newAliasTechnologyProject, 'error_summaryadd': error_summaryadd,
                    'AliasTechnology': AliasSearchTechnology(technologyid, user.login, projectid),
                    "AliasTechnologyInProject": AliasSearchTechnologyInProject(technologyid, user.login, projectid),
                    "AliasExtraTechnologyInProject": AliasExtraSearchTechnologyInProject(technologyid, user.login,
                                                                                         projectid)}


@view_config(route_name='prjenumerator', renderer='templates/project/projectenumerator.html')
class PrjEnumerator(privateView):
    def processView(self):
        ProjectEnumeratorsResources.need()
        EnumeratorJS.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)

        error_summaryenumerator = {}
        dataworking = {}
        newenumerator = False
        mdfenumerator = False
        dltenumerator = False
        projectid = self.request.matchdict['projectid']

        data = ProjectBelongsToUser(user.login, projectid)
        if not data:
            raise HTTPNotFound()
        else:
            dataworking['user_name'] = user.login
            dataworking['project_cod'] = projectid

            if (self.request.method == 'POST'):

                if 'btn_add_enumerator' in self.request.POST:
                    enumerator_name = self.request.POST.get('txt_add_enumerator_name', '')
                    enumerator_password = self.request.POST.get('txt_add_enumerator_password', '')
                    enumerator_user_name = self.request.POST.get('txt_add_enumerator_user_name','')
                    #enumerator_status = self.request.POST.get('ckb_modify_status','')

                    dataworking['enumerator_password'] = enumerator_password
                    dataworking['enumerator_name'] = enumerator_name
                    dataworking['enum_id'] = enumerator_user_name
                    #dataworking['enum_active'] = enumerator_status

                    if enumerator_user_name !='':

                        if enumerator_name != '':

                            if enumerator_password != '':

                                existeEnumerator = SearchEnumeratorForId(dataworking)

                                if not existeEnumerator:
                                    added, message = addProjectEnumerator(dataworking)
                                    if not added:
                                        error_summaryenumerator = {'dberror': message}
                                    else:
                                        newenumerator = True
                                else:
                                    error_summaryenumerator = {'exists': self._("This user name is busy.")}
                            else:
                                error_summaryenumerator = {'passwordempty': self._("The password of the enumerator cannot be empty.")}
                        else:
                            error_summaryenumerator = {'nameempty': self._("The name of the enumerator cannot be empty.")}
                    else:
                        error_summaryenumerator = {'userempty': self._("The user namne cannot be empty.")}

                    if error_summaryenumerator > 0:
                        addEnumeratorAutoShow.need()

                if 'btn_modify_enumerator' in self.request.POST:

                    enumerator_user_name =self.request.POST.get('txt_modify_user_name','')
                    enumerator_name = self.request.POST.get('txt_modify_name', '')
                    enumerator_status = self.request.POST.get('ckb_modify_status','')
                    enumerator_password = self.request.POST.get('txt_modify_password', '')
                    enumerator_new_password = self.request.POST.get('txt_modify_password_new','')

                    dataworking['enum_id'] = enumerator_user_name
                    dataworking['enumerator_name'] = enumerator_name

                    if enumerator_status == 'on':
                        dataworking['enum_active'] = 1
                    else:
                        dataworking['enum_active'] = 0

                    dataworking['enumerator_password'] = enumerator_password
                    dataworking['enumerator_new_password'] = enumerator_new_password




                    if enumerator_name != '':
                        if enumerator_password != '' or enumerator_new_password!='':
                            print "------------> Algoooo esta lleno"
                            if enumerator_password !='' :

                                if enumerator_new_password.strip() !='':

                                    existEnumeratorWithThisPassword = SearchPasswordForUser(dataworking,enumerator_password)

                                    if existEnumeratorWithThisPassword:
                                        print "Debe de..........------------>"
                                        dataworking['enumerator_password'] = enumerator_new_password
                                        mdf, message = mdfProjectEnumerator(dataworking)
                                        if not mdf:
                                            error_summaryenumerator = {'dberror': message}
                                        else:
                                            mdfenumerator = True
                                    else:
                                        error_summaryenumerator = {'IncorrectPassword': self._("Password is incorrect.")}
                                else:
                                    error_summaryenumerator = {'newpasswordempty': self._("The new password cannot be empty.")}
                            else:
                                error_summaryenumerator = {'passwordempty': self._("The password of the enumerator cannot be empty.")}
                        else:
                            print "------------------>solo cambiar nombre o estado..."
                            mdf, message = mdfProjectEnumerator(dataworking)
                            if not mdf:
                                error_summaryenumerator = {'dberror': message}
                            else:
                                mdfenumerator = True
                    else:
                        error_summaryenumerator = {'nameempty': self._("The name of the enumerator cannot be empty.")}




                    if error_summaryenumerator > 0:
                        updateProjectEnumeratorAutoShow.need()

                if 'btn_delete_enumerator' in self.request.POST:

                    enumerator_id = self.request.POST.get('txt_delete_user_name','')
                    dataworking['enum_id'] = enumerator_id

                    dlt, message = dltProjectEnumerator(dataworking)

                    if not dlt:
                        error_summaryenumerator = {'dberror': message}
                    else:
                        dltenumerator = True

                    if error_summaryenumerator > 0:
                        deleteProjectEnumeratorAutoShow.need()

            return {'activeUser': self.user, 'dataworking':dataworking,'dltenumerator':dltenumerator, 'mdfenumerator':mdfenumerator, 'newenumerator':newenumerator, 'error_summaryenumerator': error_summaryenumerator,'searchEnumerator': searchEnumerator(dataworking)}

@view_config(route_name='questions', renderer='templates/project/questions.html')
class questions_view(privateView):
    def processView(self):
        ProjectQuestionResources.need()
        EnumeratorJS.need()
        error_summary={}
        dataworking ={}
        newquestion=False
        editquestion=False

        if (self.request.method == 'POST'):

                if 'btn_add_question' in self.request.POST:
                    dataworking['question_notes']      = self.request.POST.get('txt_notes','')
                    dataworking['question_desc']       = self.request.POST.get('txt_description','')
                    dataworking['question_unit']       = self.request.POST.get('txt_indication','')
                    dataworking['question_dtype']      = self.request.POST.get('cmbtype','')
                    dataworking['question_oth']        = self.request.POST.get('ckb_acceptother','')
                    dataworking['question_cmp']        = ""
                    dataworking['question_reqinreg']   = self.request.POST.get('ckb_registrationrequired','')
                    dataworking['question_reqinasses'] = self.request.POST.get('ckb_assessmentrequired','')
                    dataworking['question_optperprj']  = ""
                    dataworking['user_name']           = self.user.login

                    if dataworking['question_reqinreg']== 'on':
                        dataworking['question_reqinreg'] = 1
                    else:
                        dataworking['question_reqinreg'] = 0

                    if dataworking['question_reqinasses']== 'on':
                        dataworking['question_reqinasses'] = 1
                    else:
                        dataworking['question_reqinasses'] = 0

                    if dataworking['question_oth']== 'on':
                        dataworking['question_oth'] = 1
                    else:
                        dataworking['question_oth'] = 0

                    add, message = addQuestion(dataworking)

                    if not add:
                        error_summary = {'dberror': message}
                    else:
                        newquestion = True

                    if error_summary>0:
                        addQuestionAutoShow.need()

                if 'btn_modify_question' in self.request.POST:
                    dataworking['question_id']         = self.request.POST.get('modify_txt_id','')
                    dataworking['question_notes']      = self.request.POST.get('modify_txt_notes','')
                    dataworking['question_desc']       = self.request.POST.get('modify_txt_description','')
                    dataworking['question_unit']       = self.request.POST.get('modify_txt_indication','')
                    dataworking['question_dtype']      = self.request.POST.get('modify_cmbtype','')
                    dataworking['question_oth']        = self.request.POST.get('modify_ckb_acceptother','')
                    dataworking['question_cmp']        = ""
                    dataworking['question_reqinreg']   = self.request.POST.get('modify_ckb_registrationrequired','')
                    dataworking['question_reqinasses'] = self.request.POST.get('modify_ckb_assessmentrequired','')
                    dataworking['question_optperprj']  = ""
                    dataworking['user_name']           = self.user.login

                    if dataworking['question_reqinreg']== 'on':
                        dataworking['question_reqinreg'] = 1
                    else:
                        dataworking['question_reqinreg'] = 0

                    if dataworking['question_reqinasses']== 'on':
                        dataworking['question_reqinasses'] = 1
                    else:
                        dataworking['question_reqinasses'] = 0

                    if dataworking['question_oth']== 'on':
                        dataworking['question_oth'] = 1
                    else:
                        dataworking['question_oth'] = 0

                    mdf, message =updateQuestion(dataworking)

                    if not mdf:
                        error_summary = {'dberror': message}
                    else:
                        editquestion = True

                    if error_summary>0:
                        updateQuestionAutoShow.need()

        return {'activeUser':self.user,'error_summary':error_summary,'newquestion':newquestion,'editquestion': editquestion,'dataworking':dataworking,'UserQuestion':UserQuestion(self.user.login)}

@view_config(route_name='prjquestion', renderer='templates/project/projectquestions.html')
class questionsInProject(privateView):
    def processView(self):
        QuestionsInProject.need()
        ColorPickerJs.need()
        projectid = self.request.matchdict['projectid']
        dataworking = {}

        if(self.request.method == 'POST'):

            dataworking['user_name']=self.user.login
            dataworking['project_cod']= projectid

            if 'btn_add_group' in self.request.POST:
                dataworking['section_name'] = self.request.POST.get('txt_group_name','')
                dataworking['section_content'] = self.request.POST.get('txt_group_desc','')
                dataworking['section_color'] = '#449d44'

                if dataworking['section_name'] !='':
                    if dataworking['section_content'] !='':
                        addgroup,message = AddGroup(dataworking)

                        if not addgroup:
                            print "error en la base "+message
                        else:
                            print "agrego bien"
                    else:
                        print "falta informacion"
                else:
                    print "falta informacion"

            if 'btnsaveordergroup' in self.request.POST:
                groups = self.request.POST.get('txt_groups','')

                part = groups.split(',')
                cont=0
                for element in part:
                    cont = cont+1
                    attr = element.split('_')
                    color = self.request.POST.get('txtcolor_'+attr[1],'')
                    print "------>"+color
                    cgo,message = changeGroupOrder(attr[1],color,cont,self.user.login, projectid)
                    if not cgo:
                        print "error en la base "+message
                    else:
                        print "edito orden bien"



        return {'activeUser':self.user,'UserGroups':UserGroups(self.user.login,projectid), 'Questions':Prj_UserQuestion(self.user.login)}

@view_config(route_name='questionsproject', renderer='templates/project/questionsproject.html')
class questionsproject_view(privateView):
    def processView(self):
        questionproject.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)

        book = xlwt.Workbook()

        sheet1 = book.add_sheet("survey")
        sheet1.write(0, 0, 'type')
        sheet1.write(0, 1, 'name')
        sheet1.write(0, 2, 'label')
        sheet1.write(0, 3, 'hint')
        sheet1.write(0, 4, 'constraint')
        sheet1.write(0, 5, 'constraint_message')
        sheet1.write(0, 6, 'required')
        sheet1.write(0, 7, 'required_message')
        sheet1.write(0, 8, 'appearance')
        sheet1.write(0, 9, 'default')
        sheet1.write(0, 10, 'relevant')
        sheet1.write(0, 11, 'repeat_count')
        sheet1.write(0, 12, 'read_only')
        sheet1.write(0, 13, 'choice_filter')
        sheet1.write(0, 14, 'calculation')

        sheet2 = book.add_sheet("choices")
        sheet2.write(0, 0, 'list_name')
        sheet2.write(0, 1, 'name')
        sheet2.write(0, 2, 'label')

        sheet3 = book.add_sheet("settings")
        sheet3.write(0, 0, 'form_title')
        sheet3.write(0, 1, 'form_id')
        sheet3.write(0, 2, 'instance_name')

        book.save("prueba3.xls")

        return {'activeUser': self.user}
