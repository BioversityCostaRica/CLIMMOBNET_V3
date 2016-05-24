import uuid

import transaction

from models import DBSession, Technology,Prjtech
from sqlalchemy import or_

def searchTechnologies(user,projectid):
    mySession = DBSession()
    subquery = mySession.query(Prjtech.tech_id).filter(Prjtech.project_cod == projectid).filter(Prjtech.user_name == user)
    result = mySession.query(Technology).filter(or_(Technology.user_name == user, Technology.user_name == 'bioversity')).filter(Technology.tech_id.notin_(subquery)).all()
    mySession.close()

    return result

def searchTechnologiesInProject(user,project_id):
    mySession = DBSession()
    result = mySession.query(Technology,Prjtech).filter(Prjtech.tech_id == Technology.tech_id).filter(Prjtech.user_name == user).filter(Prjtech.project_cod == project_id).all()
    mySession.close()
    return result

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