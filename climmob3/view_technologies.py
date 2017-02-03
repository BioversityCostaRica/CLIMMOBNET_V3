

from pyramid.view import view_config
from viewclasses import privateView
import helpers

from maintenance import getUserTechs, findTechInLibrary, addTechnology, updateTechnology, removeTechnology, showProjectTechnologies
from resources import  technologyResources, addTechAutoShow, updateTechAutoShow, deleteTechAliasAutoShow

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