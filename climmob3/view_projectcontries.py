
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from auth import getUserData
from pyramid.security import authenticated_userid

from viewclasses import privateView


from resources import  ProjectCountriesResources, addCountryAutoShow, updateContactCountryAutoShow, deleteCountryProjectAutoShow

from querys_countries import allCountries, CountriesProject, addProjectCountry, ProjectBelongsToUser, updateContactCountry, removeContactCountry


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

            return {'activeUser': self.user, 'newcountryproject': newcountryproject,
                    'contactcountryEdited': contactcountryEdited, 'projectcountryDelete': projectcountryDelete,
                    'dataworking': dataworking, 'error_summary': error_summary,
                    'Countries': allCountries(projectid, self.user.login),
                    'PrjCnty': CountriesProject(self.user.login, projectid)}
