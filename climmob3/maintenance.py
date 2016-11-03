import uuid

import transaction
from sqlalchemy import func
from models import DBSession,Technology,Project,Prjtech, Techalia

"""def informacion_de_productos_biblioteca(user):

    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name != user).all()
    mySession.close()

    return result
"""
#This return the technologies of an user
def getUserTechs(user):
    res=[]
    mySession = DBSession()
    #result = mySession.query(Technology,func.count(Techalia.tech_id).label('quantity')).filter(Technology.user_name == user).filter(Technology.tech_id == Techalia.tech_id).group_by(Technology.tech_name) .all()
    result = mySession.query(Technology,mySession.query(func.count(Techalia.tech_id)).filter(Technology.tech_id == Techalia.tech_id).label("quantity")).filter_by(user_name = user).all()
    for technology in result:
        res.append({"tech_id":technology[0].tech_id,"tech_name":technology[0].tech_name.decode('latin1'),'user_name':technology[0].user_name,'quantity': technology.quantity})

    mySession.close()
    return res

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
    res=[]
    mySession= DBSession()
    result = mySession.query(Project).filter(Project.user_name == user).all()
    for project in result:
        res.append({"user_name":project.user_name,"project_cod":project.project_cod,"project_name":project.project_name.decode('latin1'),"project_abstract":project.project_abstract.decode('latin1'),"project_tags":project.project_tags.decode('latin1'),"project_pi":project.project_pi.decode('latin1'),"project_piemail":project.project_piemail.decode('latin1'),"project_active":project.project_active,"project_public":project.project_public,"project_numobs":project.project_numobs,"project_numcom":project.project_numcom,"project_lat":project.project_lat,"project_lon":project.project_lon,"project_creationdate":project.project_creationdate})

    mySession.close()
    return res

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