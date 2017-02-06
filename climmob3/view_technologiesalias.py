
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from viewclasses import publicView, privateView


from resources import  deleteTechAutoShow, technologyaliasResources, addTechAliasAutoShow, updateTechAliasAutoShow
from querys_alias import techBelongsToUser, findTechalias, addTechAlias, getTechsAlias, updateAlias, removeAlias

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