import uuid

import transaction

from models import DBSession, Techalia, Technology, Prjtech, Prjalia
from sqlalchemy import or_, func


def PrjTechBelongsToUser(user, projectid, technologyid):
    mySession = DBSession()
    result = mySession.query(Prjtech).filter(Prjtech.tech_id == technologyid).filter(Prjtech.project_cod == projectid).filter(Prjtech.user_name == user).all()
    if not result:
        return False
    else:
        return True

def AliasSearchTechnology(technology, user, projectid):
    res=[]
    mySession = DBSession()
    subquery = mySession.query(Prjalia.alias_used).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_name =='')
    result = mySession.query(Technology,Techalia).filter(Techalia.tech_id == Technology.tech_id).filter(Technology.tech_id == technology).filter(Techalia.alias_id.notin_(subquery)).all()
    for technology in result:
        res.append({"tech_id":technology[0].tech_id,"tech_name":technology[0].tech_name.decode('latin1'),'user_name':technology[0].user_name,"tech_idAlias":technology[1].tech_id,"alias_id":technology[1].alias_id,"alias_name":technology[1].alias_name.decode('latin1')})

    mySession.close()
    return res

def AliasSearchTechnologyInProject(technology, user, projectid):
    res=[]
    mySession = DBSession
    result = mySession.query(Prjalia,Techalia).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_used==Techalia.alias_id)
    for technology in result:
        res.append({"user_name":technology[0].user_name,"project_cod":technology[0].project_cod,'tech_idPrj':technology[0].tech_id,'alias_idPrj':technology[0].alias_id,'alias_namePrj':technology[0].alias_name.decode('latin1'),'tech_used':technology[0].tech_used,'alias_used':technology[0].alias_used,"tech_idTec":technology[1].tech_id,"alias_idTec":technology[1].alias_id,"alias_nameTec":technology[1].alias_name.decode('latin1')})

    mySession.close()
    return res

def AliasExtraSearchTechnologyInProject(technology, user, projectid):
    res=[]
    mySession = DBSession
    result = mySession.query(Prjalia).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_name!='')

    for alias in result:
        res.append({"user_name":alias.user_name,"project_cod":alias.project_cod,'tech_id':alias.tech_id,'alias_id':alias.alias_id,'alias_name':alias.alias_name.decode('latin1'),'tech_used':alias.tech_used,'alias_used':alias.alias_used})

    mySession.close()
    return res

def AddAliasTechnology(data):
    mySession= DBSession()
    max_id = mySession.query(func.ifnull(func.max(Prjalia.alias_id),0).label("id_max")).one()


    newAliasTechnology = Prjalia(user_name= data['user_name'], project_cod= data['project_cod'], tech_id= data['tech_id'], tech_used= data['tech_id'], alias_used=data['alias_id'],alias_id=max_id.id_max+1, alias_name= "")
    try:
        transaction.begin()
        mySession.add(newAliasTechnology)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def addTechAliasExtra(data):
    mySession= DBSession()
    max_id = mySession.query(func.ifnull(func.max(Prjalia.alias_id),0).label("id_max")).one()


    newAliasTechnology = Prjalia(user_name= data['user_name'], project_cod= data['project_cod'], tech_id= data['tech_id'], tech_used= None, alias_used=None,alias_id=max_id.id_max+1, alias_name= data['alias_name'])
    try:
        transaction.begin()
        mySession.add(newAliasTechnology)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def deleteAliasTechnologyProject(user,projectid,techid,aliasid):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Prjalia).filter(Prjalia.user_name == user).filter(Prjalia.tech_id== techid).filter(Prjalia.project_cod==projectid).filter(Prjalia.alias_id==aliasid).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e