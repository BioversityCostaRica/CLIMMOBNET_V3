
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from auth import getUserData
from pyramid.security import authenticated_userid, remember

from viewclasses import privateView


from resources import  EnumeratorJS,ProjectEnumeratorsResources, addEnumeratorAutoShow,updateProjectEnumeratorAutoShow,deleteProjectEnumeratorAutoShow
from querys_countries import ProjectBelongsToUser
from querys_enumerator import searchEnumerator,addProjectEnumerator,SearchEnumeratorForId,mdfProjectEnumerator,dltProjectEnumerator,SearchPasswordForUser


@view_config(route_name='prjenumerator', renderer='templates/project/projectenumerator.html')
class PrjEnumerator(privateView):
    def processView(self):
        global error_summaryenumerator,dataworking,newenumerator,mdfenumerator,dltenumerator,login,user,projectid

        ProjectEnumeratorsResources.need()
        EnumeratorJS.need()
        error_summaryenumerator = {}
        dataworking = {}
        newenumerator = False
        mdfenumerator = False
        dltenumerator = False
        login = authenticated_userid(self.request)
        user = getUserData(login)
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

            currentLoc = self.request.POST.get('txt_snippet','')
            if currentLoc == "home":
                headers = remember(self.request, self.user.login)
                loc = self.request.route_url('home')
                return HTTPFound(location=loc, headers=headers)
            else:
                return {'activeUser': self.user,'projectenumerator': return_projectenumerator_view(self.user.login,projectid) }


global error_summaryenumerator,dataworking,newenumerator,mdfenumerator,dltenumerator,login,user,projectid

error_summaryenumerator = {}
dataworking = {}
newenumerator = False
mdfenumerator = False
dltenumerator = False
login = None
user = None
projectid = None

def return_projectenumerator_view(user,projectid):
    data = {}
    data['user_name'] = user
    data['project_cod'] = projectid
    ProjectEnumeratorsResources.need()
    EnumeratorJS.need()

    return {'dataworking':dataworking,'dltenumerator':dltenumerator,
            'mdfenumerator':mdfenumerator, 'newenumerator':newenumerator, 'error_summaryenumerator': error_summaryenumerator,
            'searchEnumerator': searchEnumerator(data),'projectid':data['project_cod']}