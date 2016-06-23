import uuid

import transaction

from models import DBSession, Project, Country

def searchproject(data):
    mySession = DBSession()
    result = mySession.query(Project).filter(Project.user_name == data['user_name'], Project.project_cod==data['project_cod']).all()
    mySession.close()

    if not result:
        return False
    else:
        return True

def addproject(data):
    mySession= DBSession()
    newProject = Project(user_name= data['user_name'], project_cod=data['project_cod'], project_abstract=data['project_abstract'],project_name=data['project_name'],project_tags=data['project_tags'], project_pi=data['project_pi'],project_piemail=data['project_piemail'])
    try:
        transaction.begin()
        mySession.add(newProject)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def updateProject(data):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Project).filter(Project.user_name == data['user_name']).filter(Project.project_cod == data['project_cod']).update({ 'project_name' : data['project_name'], 'project_abstract': data['project_abstract'],'project_tags':data['project_tags'],'project_pi':data['project_pi'],'project_piemail':data['project_piemail']})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def deleteProject(data):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Project).filter(Project.user_name == data['user_name']).filter(Project.project_cod == data['project_cod']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()

        return False, e

def allCountries():
    res = []
    numcnty = 1
    mySession = DBSession()
    result = mySession.query(Country).order_by(Country.cnty_name).all()
    for cnty in result:
        res.append({"code":cnty.cnty_cod,"name":cnty.cnty_name.decode('latin1'),'num':numcnty})
        numcnty = numcnty + 1

    mySession.close()
    return res

