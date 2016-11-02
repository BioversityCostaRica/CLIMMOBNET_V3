import transaction
from sqlalchemy import func
from models import DBSession,Project, Prjcnty, User

def getCountObs(request):
    mySession = DBSession()
    #result = mySession.query(Project.project_name).filter(Project.user_name == request).count()
    result = mySession.query(func.sum(Project.project_numobs)).filter(Project.user_name == request).scalar()
    mySession.close()
    if (result==None):
        result="0"
    return result

def get_Count1(request):#get num of projects
    mySession = DBSession()
    result = mySession.query(Project.project_name).filter(Project.user_name == request).count()
    mySession.close()
    return result


def getProjectCount(request):#get list of project
    mySession = DBSession()
    result = mySession.query(Project.project_cod,Project.project_name, Project.project_numobs, Project.project_active).filter(Project.user_name ==request).order_by(Project.project_active.desc())
    mySession.close()
    return result


def getUserCountry(request):#get country list for selected user
    mySession = DBSession()
    result = mySession.query(Prjcnty.cnty_cod).filter(Prjcnty.user_name ==request).group_by(Prjcnty.cnty_cod)
    mySession.close()
    country=[]
    for i in result:
        country.append(i.cnty_cod)
    country = list(set(country))
    #country = ["CR", "AR"]
    dic = {"002": {"015": ["DZ", "EG", "EH", "LY", "MA", "SD", "SS", "TN"],
                   "011": ["BF", "BJ", "CI", "CV", "GH", "GM", "GN", "GW", "LR", "ML", "MR", "NE", "NG", "SH", "SL",
                           "SN", "TG"], "017": ["AO", "CD", "ZR", "CF", "CG", "CM", "GA", "GQ", "ST", "TD"],
                   "014": ["BI", "DJ", "ER", "ET", "KE", "KM", "MG", "MU", "MW", "MZ", "RE", "RW", "SC", "SO", "TZ",
                           "UG", "YT", "ZM", "ZW"], "018": ["BW", "LS", "NA", "SZ", "ZA"]}, "150": {
        "154": ["GG", "JE", "AX", "DK", "EE", "FI", "FO", "GB", "IE", "IM", "IS", "LT", "LV", "NO", "SE", "SJ"],
        "155": ["AT", "BE", "CH", "DE", "DD", "FR", "FX", "LI", "LU", "MC", "NL"],
        "151": ["BG", "BY", "CZ", "HU", "MD", "PL", "RO", "RU", "SU", "SK", "UA"],
        "039": ["AD", "AL", "BA", "ES", "GI", "GR", "HR", "IT", "ME", "MK", "MT", "CS", "RS", "PT", "SI", "SM", "VA",
                "YU"]}, "019": {"021": ["BM", "CA", "GL", "PM", "US"],
                                "029": ["AG", "AI", "AN", "AW", "BB", "BL", "BS", "CU", "DM", "DO", "GD", "GP", "HT",
                                        "JM", "KN", "KY", "LC", "MF", "MQ", "MS", "PR", "TC", "TT", "VC", "VG", "VI"],
                                "013": ["BZ", "CR", "GT", "HN", "MX", "NI", "PA", "SV"],
                                "005": ["AR", "BO", "BR", "CL", "CO", "EC", "FK", "GF", "GY", "PE", "PY", "SR", "UY",
                                        "VE"]},
           "142": {"143": ["TM", "TJ", "KG", "KZ", "UZ"], "030": ["CN", "HK", "JP", "KP", "KR", "MN", "MO", "TW"],
                   "034": ["AF", "BD", "BT", "IN", "IR", "LK", "MV", "NP", "PK"],
                   "035": ["BN", "ID", "KH", "LA", "MM", "BU", "MY", "PH", "SG", "TH", "TL", "TP", "VN"],
                   "145": ["AE", "AM", "AZ", "BH", "CY", "GE", "IL", "IQ", "JO", "KW", "LB", "OM", "PS", "QA", "SA",
                           "NT", "SY", "TR", "YE", "YD"]},
           "009": {"053": ["AU", "NF", "NZ"], "054": ["FJ", "NC", "PG", "SB", "VU"],
                   "057": ["FM", "GU", "KI", "MH", "MP", "NR", "PW"],
                   "061": ["AS", "CK", "NU", "PF", "PN", "TK", "TO", "TV", "WF", "WS"]}, }
    ret = ""
    region = []
    for i in dic:
        for k in dic[i]:
            for c in country:
                if c in dic[i][k]:
                    region.append(k)
    region = list(set(region))
    if len(region) > 1:
        region2 = []
        for i in dic:
            for c in dic[i]:
                if c in region:
                    region2.append(i)
        if len(list(set(region2))) == 1:
            ret = list(set(region2))[0]
        else:
            ret = "world"
    else:
        try:
            ret = region[0]
        except:
            ret= "world"
    country = ";".join(country)
    ret = ret+";"+country

    return ret

def get_CountI():#get user, projects, experiments counts for home page
    res=[]
    mySession = DBSession()
    result = mySession.query(User.user_name).count()
    res.append(str(int(result)))
    result = mySession.query(Project.project_name).count()
    res.append(str(int(result)))
    result = mySession.query(func.sum(Project.project_numobs)).scalar()
    res.append(str(int(result)))

    result = mySession.query(Prjcnty.cnty_cod).group_by(Prjcnty.cnty_cod).all()
    res.append(str(len(result)))


    mySession.close()
    return res

