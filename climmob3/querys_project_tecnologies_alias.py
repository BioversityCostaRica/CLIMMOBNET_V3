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
    mySession = DBSession()
    subquery = mySession.query(Prjalia.alias_used).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_name =='')
    result = mySession.query(Techalia, Technology).filter(Techalia.tech_id == Technology.tech_id).filter(Technology.tech_id == technology).filter(Techalia.alias_id.notin_(subquery)).all()
    mySession.close()
    return result

def AliasSearchTechnologyInProject(technology, user, projectid):
    mySession = DBSession
    result = mySession.query(Prjalia,Techalia).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_used==Techalia.alias_id)
    return result

def AliasExtraSearchTechnologyInProject(technology, user, projectid):
    mySession = DBSession
    result = mySession.query(Prjalia).filter(Prjalia.user_name == user).filter(Prjalia.project_cod == projectid).filter(Prjalia.tech_id == technology).filter(Prjalia.alias_name!='')
    return result

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