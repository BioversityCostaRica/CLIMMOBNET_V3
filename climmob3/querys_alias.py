import uuid

import transaction

from models import DBSession,Technology, Techalia, Prjalia
from sqlalchemy import func

def techBelongsToUser(user, techid):
    res=[]
    mySession = DBSession()
    result = mySession.query(Technology).filter(Technology.user_name == user, Technology.tech_id==techid).all()
    mySession.close()

    for technology in result:
        res.append({"tech_id":technology.tech_id,"tech_name":technology.tech_name.decode('latin1'),'user_name':technology.user_name})
    mySession.close()
    return res

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
    res=[]
    mySession = DBSession()
    result = mySession.query(Techalia,mySession.query(func.count(Prjalia.alias_id)).filter(Techalia.alias_id==Prjalia.alias_used).label("quantity")).filter(Techalia.tech_id==idtech).all()
    mySession.close()

    for techalias in result:
        res.append({"tech_id":techalias[0].tech_id,"alias_id":techalias[0].alias_id,'alias_name':techalias[0].alias_name.decode('latin1'),'quantity': techalias.quantity})

    mySession.close()
    return res

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