from models import DBSession
from models import Country, Prjcnty,Technology,Prjtech,Enumerator
from models import Sector
from dbuserfunctions import getStats
from sqlalchemy import func
import urllib, hashlib
import pprint
def getCountryList():
    countries = []
    mySession = DBSession()
    results = mySession.query(Country).all()
    for result in results:
        try:
            name = unicode(result.cnty_name.decode('cp1252').encode('utf-8'))
            countries.append({"code":result.cnty_cod,"name":name})
        except:
            countries.append({"code":result.cnty_cod,"name":"Unknown"})
    mySession.close()
    return countries

<<<<<<< HEAD
def getCountry(country,array):
    cnty_contact=''
    for datos in array:
        if datos['cnty_cod'] == country:
            cnty_contact = datos['cnty_contact']

    if cnty_contact:
        return cnty_contact
    else:
        return False

def CountriesProject(user,projectid):

    mySession = DBSession()
    results = mySession.query(Prjcnty, Country).filter(Prjcnty.user_name== user).filter(Prjcnty.project_cod ==projectid).filter(Prjcnty.cnty_cod == Country.cnty_cod)
    my_countries = ''


    for result in results:
        my_countries +=result[0].cnty_cod+'[-]'+ result[1].cnty_name+' - '+result[0].cnty_contact+'~'
        #my_countries +=cnty['Prjcnty'].cnty_cod+'[-]'+cnty['Prjcnty'].cnty_contact+'~'

    mySession.close()
    return my_countries

def searchTechnologiesInProject(user,project_id):
    mySession = DBSession()
    result = mySession.query(Technology.tech_name).filter(Prjtech.tech_id == Technology.tech_id).filter(Prjtech.user_name == user).filter(Prjtech.project_cod == project_id).all()
    mySession.close()
    tech_in_project = ''
    for tech in result:
        tech_in_project += tech.tech_name+'~'

    return tech_in_project

def searchEnumerator(user,projectid):
    mySession = DBSession()
    active = mySession.query(func.count(Enumerator.user_name).label('actives')).filter(Enumerator.user_name == user).filter(Enumerator.project_cod == projectid).filter(Enumerator.enum_active==1).all()
    inactive = mySession.query(func.count(Enumerator.user_name).label('inactives')).filter(Enumerator.user_name == user).filter(Enumerator.project_cod == projectid).filter(Enumerator.enum_active==0).all()
    mySession.close()


    return str(active[0].actives)+'~'+str(inactive[0].inactives)

def get_Busy_Technology(id_technology, array):
    assigned_project = False

    for data in array:
        if data[0] == id_technology:
            assigned_project = True

    return assigned_project
=======
def getCountryInPos(array,pos):
    return array[pos]
>>>>>>> fixes

def getSectorList():
    sectors = []
    mySession = DBSession()
    results = mySession.query(Sector).all()
    for result in results:
        sectors.append({"code":str(result.sector_cod),"name":result.sector_name})
    mySession.close()
    return sectors

def getFeedTypes():
    feedTypes = []
    feedTypes.append({"type":"P","name":"By Product"})
    feedTypes.append({"type":"S","name":"Grass"})
    feedTypes.append({"type":"G","name":"Grain"})
    feedTypes.append({"type":"L","name":"Legume"})
    feedTypes.append({"type":"B","name":"Browse"})
    return feedTypes

def getPortalStats(currUser = None):
    return getStats(currUser)

def getGravatarFromEmail(size,email):
    default = "identicon"
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    return gravatar_url

def getModelOutVars():
    outvars = {}

    outvars["outvar1"] = "Animal weight (kg)"
    outvars["outvar2"] = "Forage"
    outvars["outvar3"] = "Sumplement 1"
    outvars["outvar4"] = "Sumplement 1 amount (kg)"
    outvars["outvar5"] = "Sumplement 2"
    outvars["outvar6"] = "Sumplement 2 amount (kg)"
    outvars["outvar7"] = "Sumplement 3"
    outvars["outvar8"] = "Sumplement 3 amount (kg)"
    outvars["outvar9"] = "Sumplement 4"
    outvars["outvar10"] = "Sumplement 4 amount (kg)"
    outvars["outvar11"] = "dry matter intake (kg/d)"
    outvars["outvar12"] = "forage dmi (kg/d)"
    outvars["outvar13"] = "supplement dmi (kg/d)"
    outvars["outvar14"] = "% supplement eaten"
    outvars["outvar15"] = "faecal dm produced (kg/d)"
    outvars["outvar16"] = "faecal n (g/kg dm)"
    outvars["outvar17"] = "faecal fndf (g/kg dm)"
    outvars["outvar18"] = "faecal indf (g/kg dm)"
    outvars["outvar19"] = "urinary n (g/d)"
    outvars["outvar20"] = "methane produced (l/d)"
    outvars["outvar21"] = "rumen ph (average)"
    outvars["outvar22"] = "rumen ph max"
    outvars["outvar23"] = "rumen ph min"
    outvars["outvar24"] = "rumen ph day ph < 6.2"
    outvars["outvar25"] = "rumen nh3 (average)"
    outvars["outvar26"] = "rumen nh3 max"
    outvars["outvar27"] = "rumen nh3 min"
    outvars["outvar28"] = "rumen nh3 day nh3 limiting"
    outvars["outvar29"] = "me supply (mj/kg dm)"
    outvars["outvar30"] = "me supply (mj/d)"
    outvars["outvar31"] = "me supply (mj/d) from vfa (mj/d)"
    outvars["outvar32"] = "me supply (mj/d) from digested microbes (mj/d)"
    outvars["outvar33"] = "me supply (mj/d) from abs cho (mj/d)"
    outvars["outvar34"] = "me supply (mj/d) from abs fat (mj/d)"
    outvars["outvar35"] = "me supply (mj/d) from abs feed protein (mj/d)"
    outvars["outvar36"] = "me supply above maintenance (mj/d)"
    outvars["outvar37"] = "mp supply (g/d)"
    outvars["outvar38"] = "mp supply from digested microbes (g/d)"
    outvars["outvar39"] = "mp supply from abs feed protein (g/d)"
    outvars["outvar40"] = "supply above maintenance (g/d)"
    outvars["outvar41"] = "potential milk from me (l/d)"
    outvars["outvar42"] = "potential milk from mp (l/d)"
    outvars["outvar43"] = "body weight change (kg/d)"

    return outvars