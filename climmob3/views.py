
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

from resources import FlotChars, siteFlotScript, Select2JS, basicCSS, projectResources, technologyResources

import helpers
from dbuserfunctions import addUser,getUserPassword, changeUserPassword, otherUserHasEmail, updateProfile, addToLog, getUserLog, userExists, getUserInfo
from maintenance import informacion_de_productos, buscar_producto_en_biblioteca, agregar_producto, actualizar_producto, eliminar_producto, show_projects, out_technologies

from utilityfnc import valideForm




@view_config(context=HTTPError,renderer='templates/500.html')
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

        return {'activeUser': user,'helpers': helpers}

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
                response.set_cookie('_LOCALE_',value='es',max_age=31536000)
                return  response
            did_fail = True

        return {'login': login,'failed_attempt': did_fail,'next': next}

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
            if not self.request.POST.get('user_policy','False') == "False":
                data["user_policy"] = "True"
            else:
                data["user_policy"] = "False"
            data["user_password"] = self.request.POST.get('user_password', '')
            data["user_password2"] = self.request.POST.get('user_password2', '')

            errors,error_summary = valideForm(data)

            if errors:
                return {'data': data,'helpers': helpers,'error_summary': error_summary}
            else:
                res,message = addUser(data)
                if res:

                    user = getUserData(data["user_name"])
                    if not user == None and user.check_password(data["user_password"]):
                        addToLog(user.login,'PRF',self._("Welcome to Climmob"))
                        headers = remember(self.request, data["user_name"])
                        return HTTPFound(location=self.request.route_url('home'), headers=headers)
                    else:
                        error_summary["createError"] = self._("User created but unable to login!")
                else:
                    error_summary["createError"] = self._("Unable to create user", default='Unable to create user: ${user}', mapping={'user':message})

        return {'data': data,'helpers': helpers,'error_summary': error_summary}



@view_config(route_name='profile', renderer='templates/user/profile.html')
class profile_view(privateView):
    def processView(self):
        totacy = len(getUserLog(self.user.login))
        return {'activeUser': self.user,"totacy":totacy,'helpers': helpers}


@view_config(route_name='userinfo', renderer='templates/user/user_info.html')
class userinfo_view(privateView):
    def processView(self):
        userid = self.request.matchdict['userid']
        if not userExists(userid):
            raise HTTPNotFound()

        totacy = len(getUserLog(userid))
        return {'activeUser': self.user,"totacy":totacy,'helpers': helpers,'displayUser':userid,'userInfo':getUserInfo(userid)}


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
                            if not otherUserHasEmail(self.user.login,data["user_email"]):
                                if updateProfile(self.user.login,data):
                                    self.user.email = data["user_email"]
                                    self.user.organization = data["user_organization"]
                                    self.user.fullName = data["user_fullname"]
                                    self.user.country = data["user_cnty"]
                                    self.user.sector = data["user_sector"]
                                    self.user.about = data["user_about"]
                                    self.user.updateGravatarURL()
                                    addToLog(self.user.login,'PRF',"Updated profile")
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
                            if changeUserPassword(self.user.login,self.request.POST.get('user_password2', '')):
                                addToLog(self.user.login,'PRF',"Changed password")
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

            return {'activeUser': self.user,'data': data,'helpers': helpers,'error_summary': error_summary,'passChanged':passChanged,'profileUpdated':profileUpdated,"totacy":totacy}

        return {'activeUser': self.user,'data': data,'helpers': helpers,'error_summary': error_summary,'passChanged':passChanged,'profileUpdated':profileUpdated,"totacy":totacy}


@view_config(route_name='useractivity', renderer='templates/user/activity.html')
class useractivity_view(privateView):
     def processView(self):
        limit = True
        if "all" in self.request.params:
            if self.request.params["all"] == "True":
                limit = False
        activities = getUserLog(self.user.login,limit)
        return {'activeUser': self.user,"activities":activities,"totacy":len(activities)}


@view_config(route_name='technologies', renderer='templates/project/technologies.html')
class maintenance_products(privateView):
    def processView(self):
        technologyResources.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)

        if (user == None):
            FlotChars.need()
            siteFlotScript.need()

        if 'btn_agregar_pro' in self.request.POST:

            nombre_de_producto = self.request.POST.get('txt_add_pro','')
            existe_en_biblioteca = buscar_producto_en_biblioteca('bioversity',nombre_de_producto)

            if nombre_de_producto != "":
                if existe_en_biblioteca == False:

                    existe_en_biblioteca_personal = buscar_producto_en_biblioteca(user.login, nombre_de_producto)

                    if existe_en_biblioteca_personal == False:
                        print "Hay que agregarlo"
                        salida= agregar_producto(user.login, nombre_de_producto)
                    else:
                        print "Error ya existe en biblioteca personal"
                else:
                    print "Error ya existe en biblioteca"
            else:
                print "Debe de escribir el nombre del producto"



        if 'btn_actualiza_producto' in self.request.POST:

            nombre_de_producto = self.request.POST.get('txt_update_name','')
            id_producto = self.request.POST.get('txt_update_id','')
            existe_en_biblioteca = buscar_producto_en_biblioteca('bioversity',nombre_de_producto)

            if nombre_de_producto != "":
                if existe_en_biblioteca == False:

                    existe_en_biblioteca_personal = buscar_producto_en_biblioteca(user.login, nombre_de_producto)

                    if existe_en_biblioteca_personal == False:

                        resultado_actualizar = actualizar_producto(id_producto, nombre_de_producto)

                        if resultado_actualizar == True:
                            print "" \
                                  "bien actualizado" \
                                  ""
                        else:
                            print "" \
                                  "no lo actualizo" \
                                  ""
                    else:
                        print ""
                        print nombre_de_producto
                        print "Error ya existe en biblioteca personal (actu)"
                        print ""
                else:
                    print ""
                    print "Error ya existe en biblioteca (actu)"
                    print ""
            else:
                print ""
                print "Debe de escribir el nombre del producto ha actualizar"
                print ""


        if 'btn_eliminar_producto' in self.request.POST:

            id_eliminar = self.request.POST.get('txt_delete_id','')
            resultado_eliminar= eliminar_producto(id_eliminar)

            if resultado_eliminar == True:
                print "" \
                      "Eliminado con exito" \
                      ""
            else:
                print "" \
                      "No se pudo eliminar" \
                          ""



        return {'activeUser': user, 'datos_de_productos': informacion_de_productos(user.login), 'datos_de_productos_climmob': informacion_de_productos('bioversity') }

@view_config(route_name='project', renderer='templates/project/project.html')
class project_view(privateView):
    def processView(self):
        projectResources.need()
        login = authenticated_userid(self.request)
        user = getUserData(login)
        project_data = show_projects(user.login)
        tecnologies_data = out_technologies(user.login)

        if 'btn_addNewProject' in self.request.POST:
            new_code = self.request.POST.get('newproject_code','')
            new_name = self.request.POST.get('newproject_name','')
            new_description = self.request.POST.get('newpeoject_description','')
            new_otro = self.request.POST.get('newproject_otro2','')
            new_investigator = self.request.POST.get('newproject_principal_investigator','')
            new_mail_address = self.request.POST.get('newproject_mail_address','')
            new_country = self.request.POST.get('newproject_country','')
            new_technology = self.request.POST.get('newproject_technology','')
            new_languaje = self.request.POST.get('newproject_languaje','')

            print "estamos bien en el click de agregar "+new_code+' '+new_name+ ' '+new_description+' '+new_otro+' '+new_investigator+' '+new_mail_address+' '+new_country+' '+new_technology+ ' '+new_languaje

        if 'btn_modifyProject' in self.request.POST:
            upd_code = self.request.POST.get('updproject_code','')
            upd_name = self.request.POST.get('updproject_name','')
            upd_description = self.request.POST.get('updproject_description','')
            upd_otro = self.request.POST.get('updproject_otro2','')
            upd_investigator = self.request.POST.get('updproject_principal_investigator','')
            upd_mail_address = self.request.POST.get('updproject_mail_address','')
            upd_country = self.request.POST.get('updproject_country','')
            upd_technology = self.request.POST.get('updproject_technology','')
            upd_languaje = self.request.POST.get('updproject_languaje','')

            print "estamos bien en el click actualizar "+upd_code+' '+upd_name+' '+upd_description+' '+upd_otro+' '+upd_investigator+' '+upd_mail_address+' '+upd_country+' '+upd_technology+' '+upd_languaje

        return {'activeUser': self.user,'project_data':project_data, 'tecnologies_data': tecnologies_data}