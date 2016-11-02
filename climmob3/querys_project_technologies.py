import uuid

import transaction

from models import DBSession, Technology,Prjtech,Prjalia
from sqlalchemy import or_, func


def searchTechnologies(user,projectid):
    res=[]
    mySession = DBSession()
    subquery = mySession.query(Prjtech.tech_id).filter(Prjtech.project_cod == projectid).filter(Prjtech.user_name == user)
    result = mySession.query(Technology).filter(or_(Technology.user_name == user, Technology.user_name == 'bioversity')).filter(Technology.tech_id.notin_(subquery)).all()
    for technology in result:
        res.append({"tech_id":technology.tech_id,"tech_name":technology.tech_name.decode('latin1'),'user_name':technology.user_name})

    mySession.close()
    return res

def searchTechnologiesInProject(user,project_id):
    res=[]
    mySession = DBSession()
    result = mySession.query(Technology.tech_name,Prjtech,mySession.query(func.count(Prjalia.alias_id)).filter(Prjalia.tech_id == Prjtech.tech_id).filter(Prjalia.project_cod == project_id).filter(Prjalia.user_name == user).label("quantity")).filter(Prjtech.tech_id == Technology.tech_id).filter(Prjtech.user_name == user).filter(Prjtech.project_cod == project_id).all()
    for technology in result:
        print technology
        res.append({"tech_name":technology.tech_name.decode('latin1'),'user_name':technology[1].user_name,'project_cod':technology[1].project_cod,'tech_id':technology[1].tech_id,'quantity': technology.quantity})

    mySession.close()
    return res

def addTechnologyProject(user,projectid,tech_id):
    mySession= DBSession()
    newTechnologyProject = Prjtech( user_name= user , project_cod= projectid, tech_id= tech_id )
    try:
        transaction.begin()
        mySession.add(newTechnologyProject)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def deleteTechnologyProject(user, projectid,tech_id):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Prjtech).filter(Prjtech.user_name == user).filter(Prjtech.tech_id == tech_id).filter(Prjtech.project_cod == projectid).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e

def number_of_technologies(user,projectid):
    mySession = DBSession()
    result = mySession.query(func.count(Prjtech.project_cod).label("number")).filter(Prjtech.user_name==user).filter(Prjtech.project_cod==projectid).one()
    mySession.close()
    return result.number