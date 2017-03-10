
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from auth import getUserData
from pyramid.security import authenticated_userid, remember

from viewclasses import privateView


from resources import  ProjectCountriesResources, addCountryAutoShow, updateContactCountryAutoShow, deleteCountryProjectAutoShow

from querys_countries import allCountries, CountriesProject, addProjectCountry, ProjectBelongsToUser, updateContactCountry, removeContactCountry


@view_config(route_name='prjcnty', renderer='templates/project/projectcountries.html')
class projectCountries_view(privateView):

    def processView(self):
        global error_summary,dataworking,newcountryproject,contactcountryEdited,projectcountryDelete,login,user,projectid,data

        ProjectCountriesResources.need()
        error_summary = {}
        dataworking   = {}
        newcountryproject = False
        contactcountryEdited = False
        projectcountryDelete = False
        login = authenticated_userid(self.request)
        user = getUserData(login)
        projectid = self.request.matchdict['projectid']
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
                    if cnty_cod !='':
                        if cnty_contact != '':
                            added, message = addProjectCountry(dataworking)
                            if not added:
                                # capture the error
                                error_summary = {'dberror': message}
                            else:
                                # show success message
                                newcountryproject = True
                        else:
                            error_summary = {'contactempty': self._("The contact name can't be empty.")}
                    else:
                        error_summary = {'codempty': self._("You must select a country.")}

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

                    if cnty_cod !='':
                        if cnty_contact != '':
                            upd, message = updateContactCountry(dataworking)

                            if not upd:
                                error_summary = {'dberror': message}
                            else:
                                contactcountryEdited = True
                        else:
                            error_summary = {'contactempty': self._("The contact name can't be empty.")}
                    else:
                        error_summary = {'codempty': self._("You must select a country.")}

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
            currentLoc = self.request.POST.get('txt_snippet','')
            if currentLoc == "home":
                headers = remember(self.request, self.user.login)
                loc = self.request.route_url('home')
                return HTTPFound(location=loc, headers=headers)
            else:
                return {'activeUser': self.user, 'projectCountries': return_projectcontries_view(self.user.login,projectid)}


global error_summary,dataworking,newcountryproject,contactcountryEdited,projectcountryDelete,login,user,projectid,data

error_summary = {}
dataworking   = {}
newcountryproject = False
contactcountryEdited = False
projectcountryDelete = False
login = None
user = None
projectid = None
data = None

def return_projectcontries_view(login,projectid):
    ProjectCountriesResources.need()
    return {'newcountryproject': newcountryproject,
                    'contactcountryEdited': contactcountryEdited, 'projectcountryDelete': projectcountryDelete,
                    'dataworking': dataworking, 'error_summary': error_summary,
                    'Countries': allCountries(projectid, login),
                    'PrjCnty': CountriesProject(login, projectid),'projectid':projectid}