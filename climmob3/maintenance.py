import uuid

import transaction

from models import DBSession,Crop,Project

"""def informacion_de_productos_biblioteca(user):

    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name != user).all()
    mySession.close()

    return result
"""
#Sacamos la informacion de los productos existentes por usuario (sea el de la session o el de ClimMob)
def informacion_de_productos(user):
    mySession = DBSession()
    result = mySession.query(Crop).filter_by(user_name = user).all()
    mySession.close()

    return result
#buscamos haber si ya los productos existen dentro de la biblioteca sea de ClimMob o del Usuario
def buscar_producto_en_biblioteca(user,producto):
    mySession = DBSession()
    result = mySession.query(Crop).filter(Crop.user_name == user, Crop.crop_name==producto).all()
    mySession.close()

    if not result:
        return False
    else:
        return True

#Agregamos un producto a nombre de un usuario.
def agregar_producto(user, producto):
    mySession= DBSession()
    nuevo_producto = Crop(user_name=user, crop_name= producto)
    try:
        transaction.begin()
        mySession.add(nuevo_producto)
        transaction.commit()
        mySession.close()

        return True

    except Exception, e:

        print str(e)

        transaction.abort()
        mySession.close()

        return False

#Actualizamos la informacion de un producto mediante el id
def actualizar_producto(id, nuevo_nombre):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Crop).filter(Crop.crop_id == id).update({ 'crop_name' : nuevo_nombre})
        transaction.commit()
        mySession.close()

        return True
    except Exception, e:

        print str(e)

        transaction.abort()
        mySession.close()

        return False

#Eliminamos el producto mediante el id.
def eliminar_producto(id):
    mySession= DBSession()
    transaction.begin()
    mySession.query(Crop).filter(Crop.crop_id==id).delete()
    transaction.commit()
    mySession.close()

    return True


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