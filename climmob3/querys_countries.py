import uuid

import transaction

from models import DBSession, Country, Prjcnty, Project

def allCountries(projectid, user):
    res = []
    mySession = DBSession()
    subquery = mySession.query(Prjcnty.cnty_cod).filter(Prjcnty.project_cod == projectid).filter(Prjcnty.user_name == user)
    result = mySession.query(Country).filter(Country.cnty_cod.notin_(subquery)).order_by(Country.cnty_name).all()

    for cnty in result:
        res.append({"cnty_cod":cnty.cnty_cod,"cnty_name":cnty.cnty_name.decode('latin1')})

    mySession.close()
    return res

def CountriesProject(user,projectid):
    res = []
    mySession = DBSession()
    result = mySession.query(Prjcnty).filter(Prjcnty.user_name== user).filter(Prjcnty.project_cod ==projectid)

    for cnty in result:
        print cnty.cnty_cod
        res.append({"cnty_cod":cnty.cnty_cod,"cnty_contact":cnty.cnty_contact.decode('latin1')})

    mySession.close()
    return res

def addProjectCountry(data):
    mySession= DBSession()
    newProjectCountry = Prjcnty(cnty_cod= data['cnty_cod'],cnty_contact =data['cnty_contact'], user_name=data['user_name'],project_cod=data['project_cod'] )
    try:
        transaction.begin()
        mySession.add(newProjectCountry)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def ProjectBelongsToUser(user,projectid):
    mySession = DBSession()
    result = mySession.query(Project).filter(Project.user_name == user, Project.project_cod== projectid).all()
    mySession.close()

    if not result:
        return False
    else:
        return result

def updateContactCountry(data):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Prjcnty).filter(Prjcnty.user_name== data['user_name']).filter(Prjcnty.project_cod == data['project_cod']).filter(Prjcnty.cnty_cod == data['cnty_cod']).update({ 'cnty_contact' : data['cnty_contact']})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def removeContactCountry(data):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Prjcnty).filter(Prjcnty.user_name== data['user_name']).filter(Prjcnty.project_cod == data['project_cod']).filter(Prjcnty.cnty_cod == data['cnty_cod']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False, e