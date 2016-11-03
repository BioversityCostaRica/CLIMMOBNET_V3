import uuid

import transaction
from sqlalchemy import func

from models import DBSession, Enumerator
from encdecdata import encodeData,decodeData


def searchEnumerator(data):
    res = []
    mySession = DBSession()
    result = mySession.query(Enumerator).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).all()
    for enumerator in result:
        res.append({"enum_id":enumerator.enum_id,"enum_name":enumerator.enum_name. decode('latin1'),'enum_active':enumerator.enum_active})
    return res

def SearchEnumeratorForId(data):
    mySession =DBSession()
    result = mySession.query(Enumerator).filter(Enumerator.user_name== data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id== data['enum_id']).all()

    if not result:
        return False
    else:
        return True

def addProjectEnumerator(data):
    mySession= DBSession()
    newProjectEnumerator = Enumerator(user_name= data['user_name'], project_cod=data['project_cod'],enum_id= data['enum_id'] ,enum_name=data['enumerator_name'], enum_password=encodeData(data['enumerator_password']),enum_active= 1)
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
        mySession.query(Enumerator).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id==data['enum_id']).update({ 'enum_name':data['enumerator_name'], 'enum_password':encodeData(data['enumerator_password']), 'enum_active':data['enum_active'] })
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

def SearchPasswordForUser(data,password):
    mySession = DBSession()
    result = mySession.query(Enumerator.enum_password).filter(Enumerator.user_name == data['user_name']).filter(Enumerator.project_cod == data['project_cod']).filter(Enumerator.enum_id == data['enum_id']).filter(Enumerator.enum_password == encodeData(password)).all()

    if not result:
        return False
    else:
        return True