import uuid

import transaction

from models import DBSession,Technology, Techalia
from sqlalchemy import func

def techBelongsToUser(user, techid):
    mySession = DBSession()
    result = mySession.query(Technology).filter(Technology.user_name == user, Technology.tech_id==techid).all()
    mySession.close()

    if not result:
        return False
    else:
        return result

def findTechalias(data):
    mySession = DBSession()
    result = mySession.query(Techalia).filter(Techalia.tech_id==data['tech_id'], Techalia.alias_name==data['alias_name']).all()
    mySession.close()

    if not result:
        return False
    else:
        return result

def addTechAlias(data):
    mySession= DBSession()
    #max_id = mySession.query(func.max(Techalia.alias_id).label("id_max")).one()
    max_id = mySession.query(func.ifnull(func.max(Techalia.alias_id),0).label("id_max")).one()
    print max_id
    newTechalias = Techalia(tech_id =data['tech_id'], alias_name= data['alias_name'], alias_id=max_id.id_max+1)
    try:
        transaction.begin()
        mySession.add(newTechalias)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def getTechsAlias(idtech):
    mySession = DBSession()
    result = mySession.query(Techalia).filter_by(tech_id=idtech).all()
    mySession.close()

    if not result:
        return False
    else:
        return result

def updateAlias(data):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Techalia).filter(Techalia.alias_id == data['alias_id']).update({ 'alias_name' : data['alias_name']})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def removeAlias(data):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Techalia).filter(Techalia.alias_id == data['alias_id']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e