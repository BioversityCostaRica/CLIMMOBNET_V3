from models import DBSession
from models import Country
from models import Sector
from dbuserfunctions import getStats
import urllib, hashlib

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

def getCountryInPos(array,pos):
    return array[pos]

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