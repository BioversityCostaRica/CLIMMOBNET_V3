from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group


library = Library('climmob3', 'resources')

basicCSSArray = []
basicCSSArray.append(Resource(library, 'flatlab/css/bootstrap.min.css'))
basicCSSArray.append(Resource(library, 'flatlab/css/bootstrap-reset.css'))
basicCSSArray.append(Resource(library, 'flatlab/assets/font-awesome/css/font-awesome.css'))
basicCSSArray.append(Resource(library, 'flatlab/css/style.css'))
basicCSSArray.append(Resource(library, 'flatlab/css/style-responsive.css'))
basicCSSArray.append(Resource(library, 'flatlab/css/tasks.css'))
basicCSS = Group(basicCSSArray)

commonCSSArray = []
commonCSSArray.append(Resource(library, 'flatlab/css/slidebars.css',depends=[basicCSS]))
commonCSSArray.append(Resource(library, 'site.css',depends=[basicCSS]))
commonCSS = Group(commonCSSArray)

#Main JQuery library. Required by the rest
JQuery = Resource(library, 'flatlab/js/jquery.js',bottom=True)

#CommonJS is the set of common required JavaScript for the site
commonJSArray = []
commonJSArray.append(Resource(library, 'flatlab/js/bootstrap.min.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/jquery.dcjqaccordion.2.7.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/jquery.scrollTo.min.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/slidebars.min.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/jquery.nicescroll.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/respond.min.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/tasks.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/jquery-ui-1.9.2.custom.min.js',depends=[JQuery],bottom=True))
commonJSArray.append(Resource(library, 'flatlab/js/jquery.stepy.js', depends=[JQuery],bottom=True))
commonJS = Group(commonJSArray)


#SiteScript is custom scripts for this site to work. Depends on slidebar and nicescroll
siteScript = Resource(library, 'common-scripts.js',depends=[commonJSArray[3],commonJSArray[4]],bottom=True)

#Main FlotChart JavaScript.
JQueryFlot = Resource(library, 'flatlab/assets/flot/jquery.flot.js',depends=[JQuery],bottom=True)

#FlotCharts additional JavaScripts that depend on jquery.flot.js
flotJSArray = []
flotJSArray.append(Resource(library, 'flatlab/assets/flot/jquery.flot.resize.js',depends=[JQueryFlot],bottom=True))
flotJSArray.append(Resource(library, 'flatlab/assets/flot/jquery.flot.pie.js',depends=[JQueryFlot],bottom=True))
flotJSArray.append(Resource(library, 'flatlab/assets/flot/jquery.flot.stack.js',depends=[JQueryFlot],bottom=True))
flotJSArray.append(Resource(library, 'flatlab/assets/flot/jquery.flot.crosshair.js',depends=[JQueryFlot],bottom=True))
FlotChars = Group(flotJSArray)

siteFlotScript = Resource(library, 'flot-chart.js',depends=[JQueryFlot],bottom=True)

#Select2 Requirements
Selec2Array = []
Selec2Array.append(Resource(library, 'select2/select2.css'))
Selec2Array.append(Resource(library, 'select2/select2.min.js',depends=[JQuery],bottom=True))
Select2JS = Group(Selec2Array)

#Datatables requirements
JQueryDataTable = Resource(library, 'flatlab/assets/advanced-datatable/media/js/jquery.dataTables.js',depends=[JQuery],bottom=True)

dataTableArray = []

dataTableArray.append(Resource(library, 'flatlab/assets/advanced-datatable/media/css/demo_page.css'))
dataTableArray.append(Resource(library, 'flatlab/assets/advanced-datatable/media/css/demo_table.css'))
dataTableArray.append(Resource(library, 'flatlab/assets/data-tables/DT_bootstrap.css'))
dataTableArray.append(Resource(library, 'flatlab/assets/data-tables/DT_bootstrap.js',depends=[JQueryDataTable],bottom=True))
dataTableArray.append(Resource(library, 'site-datatables.js',depends=[JQueryDataTable],bottom=True))

dataTables = Group(dataTableArray)

bsSwitch = Resource(library, 'flatlab/js/bootstrap-switch.js',depends=[JQuery],bottom=True)
siteSwitch = Resource(library, 'site-switch.js',depends=[bsSwitch],bottom=True)


highlightArray = []
highlightArray.append(Resource(library, 'highlight/styles/default.css'))
highlightArray.append(Resource(library, 'highlight/highlight.pack.js'))

highlightJS = Group(highlightArray)


modalArray = []
modalArray.append(Resource(library, 'flatlab/js/gritter.js',depends=[JQuery],bottom=True))
modalArray.append(Resource(library, 'flatlab/js/pulstate.js',depends=[JQuery],bottom=True))

modalJS = Group(modalArray)

#Project resource files
projectResourcesArray = []
projectResourcesArray.append(Resource(library, 'flatlabtagmanager-master/tagmanager.js',depends=[JQuery],bottom=True))
projectResourcesArray.append(Resource(library, 'flatlabtagmanager-master/tagmanager.css', depends=[JQuery],bottom=True))
projectResourcesArray.append(Resource(library, 'project.js',depends=[JQuery],bottom=True))

addProjectAutoShow = Resource(library, 'addProjectAutoShow.js', depends=[JQuery], bottom=True)
updateProjectAutoShow = Resource(library,'updateProjectAutoShow.js',depends=[JQuery], bottom=True)
deleteProjectAutoShow = Resource(library,'deleteProjectAutoShow.js',depends=[JQuery], bottom=True)

projectJS = Group(projectResourcesArray)

#Technology resource files
technologyResources = Resource(library, 'technologies.js', depends=[JQuery],bottom=True)
addTechAutoShow = Resource(library, 'addTechnologyAutoShow.js', depends=[JQuery],bottom=True)
updateTechAutoShow = Resource(library, 'updateTechnologyAutoShow.js', depends=[JQuery],bottom=True)
deleteTechAutoShow = Resource(library, 'deleteTechnologyAutoShow.js', depends=[JQuery],bottom=True)

#Techonology Alias resource files
technologyaliasResources = Resource(library,'technologiesalias.js', depends=[JQuery],bottom=True)
addTechAliasAutoShow = Resource(library, 'addTechnologyAliasAutoShow.js', depends=[JQuery],bottom=True)
updateTechAliasAutoShow = Resource(library,'updateTechnologyAliasAutoShow.js', depends=[JQuery],bottom=True)
deleteTechAliasAutoShow = Resource(library,'deleteTechnologyAliasAutoShow.js', depends=[JQuery],bottom=True)

#Project countries
ProjectCountriesResources = Resource(library,'projectcountries.js', depends=[JQuery], bottom=True)
addCountryAutoShow = Resource(library,'addCountryAutoShow.js', depends=[JQuery],bottom=True)
updateContactCountryAutoShow = Resource(library, 'updateContactCountryAutoShow.js', depends=[JQuery], bottom=True)
deleteCountryProjectAutoShow = Resource(library, 'deleteCountryProjectAutoShow.js', depends=[JQuery], bottom=True)

#Project technologies
ProjectTechnologiesResources = Resource(library,'projecttechnologies.js', depends=[JQuery], bottom=True);

#questionproject resource files
questionproject = Resource(library,'questionproject.js', depends=[JQuery], bottom=True)

def pserve():
    """A script aware of static resource"""
    import pyramid.scripts.pserve
    import pyramid_fanstatic
    import os

    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname, 'resources')
    pyramid.scripts.pserve.add_file_callback(
                pyramid_fanstatic.file_callback(dirname))
    pyramid.scripts.pserve.main()
