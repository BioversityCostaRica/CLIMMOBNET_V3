import uuid

import transaction
from sqlalchemy import func

from models import DBSession, Enumerator


def searchEnumerator(data):
    mySession = DBSession()
    result = mySession.query(Enumerator).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).all()

    return result

def SearchEnumeratorForId(data):
    mySession =DBSession()
    result = mySession.query(Enumerator).filter(Enumerator.user_name== data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id== data['enum_id']).all()

    if not result:
        return False
    else:
        return True

def addProjectEnumerator(data):
    mySession= DBSession()
    newProjectEnumerator = Enumerator(user_name= data['user_name'], project_cod=data['project_cod'],enum_id= data['enum_id'] ,enum_name=data['enumerator_name'], enum_password=data['enumerator_password'],enum_active= 1)
    try:
        transaction.begin()
        mySession.add(newProjectEnumerator)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def mdfProjectEnumerator(data):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Enumerator).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id==data['enum_id']).update({ 'enum_name':data['enumerator_name'], 'enum_password':data['enumerator_password'], 'enum_active':1 })
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def dltProjectEnumerator(data):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Enumerator).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id == data['enum_id']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e