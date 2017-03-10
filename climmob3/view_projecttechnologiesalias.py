import pprint

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from auth import getUserData
from pyramid.security import authenticated_userid, remember

from viewclasses import publicView, privateView


from resources import  ProjectAliasTechnologiesResources, addAliasTechPrjAutoShow
from querys_alias import findTechalias
from querys_project_tecnologies_alias import AliasSearchTechnology, AliasSearchTechnologyInProject, AliasExtraSearchTechnologyInProject, PrjTechBelongsToUser, AddAliasTechnology, deleteAliasTechnologyProject, addTechAliasExtra

@view_config(route_name='prjtechalias', renderer='templates/project/projecttechnologiesalias.html')
class PrjTechAlias(privateView):
    def processView(self):
        ProjectAliasTechnologiesResources.need()

        error_summarydlt = {}
        error_summaryadd = {}
        error_summaryaddextra = {}
        dataworking = {}
        newAliasTechnologyProject = False
        dltAliasTechnologyProject = False
        login = authenticated_userid(self.request)
        user = getUserData(login)
        projectid = self.request.matchdict['projectid']
        technologyid = self.request.matchdict['tech_id']
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
                                delete, message = deleteAliasTechnologyProject(user.login, projectid, technologyid,attr[1])
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

                if 'btn_deleteAlias' in self.request.POST:
                    dataworking['alias_id'] = self.request.POST.get('deletealias','')
                    dataworking['tech_id'] = self.request.POST.get('deletealiastech','')

                    delete, message = deleteAliasTechnologyProject(user.login, projectid, dataworking['tech_id'],dataworking['alias_id'])
                    if not delete:
                        error_summarydlt = {'dberror': message}
                    else:
                        dltAliasTechnologyProject = True
            currentLoc = self.request.POST.get('txt_snippet','')
            if currentLoc == "home":
                headers = remember(self.request, self.user.login)
                loc = self.request.route_url('home')
                return HTTPFound(location=loc, headers=headers)
            else:
                return {'activeUser': self.user,'projecttechnologiesalias':return_projecttecjnologiesalias(technologyid,user.login,projectid)}


global error_summarydlt,error_summaryadd,error_summaryaddextra,dataworking,newAliasTechnologyProject,dltAliasTechnologyProject,login,user,projectid,technologyid,data
error_summarydlt = {}
error_summaryadd = {}
error_summaryaddextra = {}
dataworking = {}
newAliasTechnologyProject = False
dltAliasTechnologyProject = False
login = None
user = None
projectid = None
technologyid = None
data = None

def return_projecttecjnologiesalias(technologyid,user,projectid):
    return {'dataworking': dataworking, 'error_summaryaddextra': error_summaryaddextra,
            'dltAliasTechnologyProject': dltAliasTechnologyProject, 'error_summarydlt': error_summarydlt,
            'newAliasTechnologyProject': newAliasTechnologyProject, 'error_summaryadd': error_summaryadd,
            'AliasTechnology': AliasSearchTechnology(technologyid, user, projectid),
            "AliasTechnologyInProject": AliasSearchTechnologyInProject(technologyid, user, projectid),
            "AliasExtraTechnologyInProject": AliasExtraSearchTechnologyInProject(technologyid, user,projectid),
            "projectid": projectid,"techid": technologyid}