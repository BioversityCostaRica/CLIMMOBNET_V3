import uuid

import transaction

from models import DBSession,Technology,Project,Prjtech

"""def informacion_de_productos_biblioteca(user):

    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name != user).all()
    mySession.close()

    return result
"""
#This return the technologies of an user
def getUserTechs(user):
    mySession = DBSession()
    result = mySession.query(Technology).filter_by(user_name = user).all()
    mySession.close()
    return result

#This function search for a technology in the library by user
def findTechInLibrary(user,technology):
    mySession = DBSession()
    result = mySession.query(Technology).filter(Technology.user_name == user, Technology.tech_name==technology).all()
    mySession.close()

    if not result:
        return False
    else:
        return True

#Add a new technology to the library.
def addTechnology(user, technology):
    mySession= DBSession()
    newTech = Technology(user_name=user, tech_name= technology)
    try:
        transaction.begin()
        mySession.add(newTech)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

#Update the name of a technology
def updateTechnology(user,id, newName):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Technology).filter(Technology.user_name == user).filter(Technology.tech_id == id).update({ 'tech_name' : newName})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

#Remove the technology for a given user
def removeTechnology(user,id):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Technology).filter(Technology.user_name == user).filter(Technology.tech_id==id).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e


def show_projects(user):
    mySession= DBSession()
    result = mySession.query(Project.project_cod, Project.project_name, Project.project_abstract,Project.project_tags,Project.project_pi,Project.project_piemail,).filter(Project.user_name == user).all()
    mySession.close()
    return result

def out_technologies(user):
    mySession= DBSession()
    result = mySession.query(Technology).filter((Technology.user_name== user)|( Technology.user_name == 'bioversity')).all()
    mySession.close()

    return result

def showProjectTechnologies (user):
    mySession = DBSession
    result = mySession.query(Prjtech.tech_id).distinct(Prjtech.tech_id).filter(Prjtech.user_name == user).all()
    mySession.close()

    return result