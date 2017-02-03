from pyramid.security import forget, remember
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from viewclasses import privateView

from resources import ProjectTechnologiesResources
from querys_countries import ProjectBelongsToUser
from querys_project_technologies import searchTechnologies, searchTechnologiesInProject, addTechnologyProject, deleteTechnologyProject


@view_config(route_name='prjtech', renderer='templates/project/projecttechnologies.html')

class projectTechnologies_view(privateView):



    def processView(self):
        global newTechnologyProject, error_summarydlt,error_summaryadd,projectid,newTechnologyProject,dltTechnologyProject, activeUser, activelogin

        ProjectTechnologiesResources.need()

        error_summarydlt = {}
        error_summaryadd = {}
        projectid = self.request.matchdict['projectid']
        newTechnologyProject = False
        dltTechnologyProject = False
        activeUser = self.user
        activelogin = self.user.login

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


            currentLoc = self.request.POST.get('txt_snippet','')
            if currentLoc == "home":
                headers = remember(self.request, self.user.login)
                loc = self.request.route_url('home')
                return HTTPFound(location=loc, headers=headers)
            else:
                return {'activeUser': activeUser, 'var':return_projectTechnologies_view(self.user.login, projectid)}
            #return {'activeUser': self.user, 'error_summaryadd': error_summaryadd, 'error_summarydlt': error_summarydlt,
            #        'dltTechnologyProject': dltTechnologyProject, 'newTechnologyProject': newTechnologyProject,
            #        'TechnologiesUser': searchTechnologies(self.user.login, projectid),
            #        'TechnologiesInProject': searchTechnologiesInProject(self.user.login, projectid)}

global newTechnologyProject, error_summarydlt,error_summaryadd,projectid,newTechnologyProject,dltTechnologyProject,activeUser, activelogin

activeUser = {}
newTechnologyProject = False
error_summarydlt = {}
error_summaryadd = {}
projectid = None
newTechnologyProject = False
dltTechnologyProject = False
activelogin = None

def return_projectTechnologies_view(user, project):
    activelogin = user
    projectid = project
    global newTechnologyProject, error_summarydlt,error_summaryadd,projectid,newTechnologyProject,dltTechnologyProject,activeUser, activelogin
    return {'error_summaryadd': error_summaryadd, 'error_summarydlt': error_summarydlt,
                    'dltTechnologyProject': dltTechnologyProject, 'newTechnologyProject': newTechnologyProject,
                    'TechnologiesUser': searchTechnologies(activelogin, projectid),
                    'TechnologiesInProject': searchTechnologiesInProject(activelogin, projectid),'projectid':projectid}