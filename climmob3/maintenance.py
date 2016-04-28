import uuid

import transaction

from models import DBSession,Crop,Project

"""def informacion_de_productos_biblioteca(user):

    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name != user).all()
    mySession.close()

    return result
"""
#This return the technologies of an user
def getUserTechs(user):
    mySession = DBSession()
    result = mySession.query(Crop).filter_by(user_name = user).all()
    mySession.close()
    return result

#This function search for a technology in the library by user
def findTechInLibrary(user,technology):
    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name == user, Crop.crop_name==technology).all()
    mySession.close()

    if not result:
        return False
    else:
        return True

#Add a new technology to the library.
def addTechnology(user, technology):
    mySession= DBSession()
    newTech = Crop(user_name=user, crop_name= technology)
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
        mySession.query(Crop).filter(Crop.user_name == user).filter(Crop.crop_id == id).update({ 'crop_name' : newName})
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
        mySession.query(Crop).filter(Crop.user_name == user).filter(Crop.crop_id==id).delete()
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
    result = mySession.query(Project.project_cod, Project.project_name, Project.project_abstract,Project.project_tags,Project.project_pi,Project.project_piemail,Project.project_cnty, Project.project_crop, Project.project_lang ,Crop.crop_name).filter(Project.user_name == user, Project.project_crop==Crop.crop_id).all()
    mySession.close()
    return result

def out_technologies(user):
    mySession= DBSession()
    result = mySession.query(Crop).filter((Crop.user_name== user)|( Crop.user_name == 'bioversity')).all()
    mySession.close()

    return result