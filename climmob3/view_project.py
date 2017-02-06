from pyramid.security import authenticated_userid
from pyramid.view import view_config

from auth import getUserData
from viewclasses import privateView

from resources import  projectResources,dataTables,ProjectJS, projectJS, addProjectAutoShow, updateProjectAutoShow, deleteProjectAutoShow

import helpers
from maintenance import  show_projects
from querys_project import searchproject, addproject, updateProject, deleteProject
from querys_projectquestions import AddGroup, AddGroupAssessment,QuestionsByDefault

@view_config(route_name='project', renderer='templates/project/project.html')
class project_view(privateView):
    def processView(self):

        ProjectJS.need()
        projectResources.need()
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
                new_numobs = self.request.POST.get('newproject_numobs','')
                new_numcom = self.request.POST.get('newproject_numcom','')
                new_lat = self.request.POST.get('newproject_lat','')
                new_lon = self.request.POST.get('newproject_lon','')

                # add the object
                dataworking['user_name'] = self.user.login
                dataworking['project_cod'] = new_code
                dataworking['project_name'] = new_name
                dataworking['project_abstract'] = new_description
                dataworking['project_tags'] = new_otro
                dataworking['project_pi'] = new_investigator
                dataworking['project_piemail'] = new_mail_address
                dataworking['project_numobs'] = new_numobs
                dataworking['project_numcom'] = new_numcom
                dataworking['project_lat'] = new_lat
                dataworking['project_lon'] = new_lon

                if new_code != '':

                    exitsproject = searchproject(dataworking)

                    if not exitsproject:

                        # add the project
                        added, message = addproject(dataworking)
                        if not added:
                            # capture the error
                            error_summary = {'dberror': message}
                        else:
                            # show success message
                            #newproject = True
                            dataworking['section_name'] = self._('Base')
                            dataworking['section_content']= self._('Basic unit ClimMob')
                            dataworking['section_color'] = '#4643E8'
                            creategroup,message =AddGroup(dataworking)
                            if not creategroup:
                                error_summary = {'dberror': message}

                            creategroup,message =AddGroupAssessment(dataworking)
                            if not creategroup:
                                error_summary = {'dberror': message}
                            else:
                                dataworking['section_user'] = self.user.login
                                dataworking['section_project'] = new_code
                                dataworking['section_id'] = '1'
                                dataworking['question_id'] = ""
                                exit, message = QuestionsByDefault(dataworking)

                                if not exit:
                                    error_summary = {'dberror': message}
                                else:
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
                upd_numobs = self.request.POST.get('updproject_numobs','')
                upd_numcom = self.request.POST.get('updproject_numcom','')
                upd_lat = self.request.POST.get('updproject_lat','')
                upd_lon = self.request.POST.get('updproject_lon','')

                dataworking['user_name'] = self.user.login
                dataworking['project_cod'] = upd_code
                dataworking['project_name'] = upd_name
                dataworking['project_abstract'] = upd_description
                dataworking['project_tags'] = upd_otro
                dataworking['project_pi'] = upd_investigator
                dataworking['project_piemail'] = upd_mail_address
                dataworking['project_numobs'] = upd_numobs
                dataworking['project_numcom'] = upd_numcom
                dataworking['project_lat'] = upd_lat
                dataworking['project_lon'] = upd_lon

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

            if 'btn_odktomysql' in self.request.POST:
                dataworking['xx'] = self.request.POST.get('txtmio','')
                path = self.request.registry.settings['odk.repository']+dataworking['xx'].replace(" ", "_")+"/"
                dbuser = self.request.registry.settings['mysql.user']
                dbpassword = self.request.registry.settings['mysql.password']

                os.system("cd "+path+"DB/REG; ~/odktools/ODKToMySQL/odktomysql -x "+path+"ODK/registry.xlsx -v question_14 -t maintable -p reg ")

                PrepareDataBase(dataworking['xx'],dbuser,dbpassword,path)
                #os.system("cd "+path+"DB/ASS; ~/odktools/ODKToMySQL/odktomysql -x "+path+"ODK/assessment.xlsx -v xxxxxx -t maintable -p ass ")
                print "TOMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

        return {'activeUser': self.user, 'project_data': show_projects(user.login), 'dataworking': dataworking,
                'error_summary': error_summary, 'newproject': newproject, 'projectEdited': projectEdited,
                'projectDelete': projectDelete, 'helper': helpers}