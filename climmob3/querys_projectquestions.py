import uuid

import transaction
from sqlalchemy import func
from sqlalchemy import or_

from models import DBSession, Question, Regsection, Registry
from encdecdata import encodeData,decodeData


def AvailableQuestions(user,project):
    res = []
    mySession = DBSession()
    subquery= mySession.query(Registry.question_id).filter(Registry.user_name == user).filter(Registry.project_cod == project)
    result = mySession.query(Question).filter(or_(Question.user_name == user, Question.user_name == "bioversity")).filter(Question.question_id.notin_(subquery)).all()
    for question in result:
        res.append({"question_id":question.question_id,"question_desc":question.question_desc.decode('latin1'),'question_notes':question.question_notes.decode('latin1'),'question_unit':question.question_unit.decode('latin1'), 'question_dtype': question.question_dtype,'question_oth': question.question_oth,'question_cmp': question.question_cmp,'question_reqinreg': question.question_reqinreg,'question_reqinasses': question.question_reqinasses,'question_optperprj': question.question_optperprj,'parent_question': question.parent_question,'user_name': question.user_name })

    mySession.close()
    return res

def Prj_UserQuestion(user,project):
    res = []
    mySession = DBSession()
    result =mySession.query(Registry,Question).filter(Registry.project_cod == project).filter(Registry.user_name == user).filter(Registry.question_id ==Question.question_id).order_by(Registry.question_order).all()
    for question in result:
        res.append({"section_id":question[0].section_id,"section_order":question[0].question_order,"question_id":question[1].question_id,"question_desc":question[1].question_desc.decode('latin1'),'question_notes':question[1].question_notes.decode('latin1'),'question_unit':question[1].question_unit.decode('latin1'), 'question_dtype': question[1].question_dtype,'question_oth': question[1].question_oth,'question_cmp': question[1].question_cmp,'question_reqinreg': question[1].question_reqinreg,'question_reqinasses': question[1].question_reqinasses,'question_optperprj': question[1].question_optperprj,'parent_question': question[1].parent_question,'user_name': question[1].user_name })

    mySession.close()

    return res


def AddGroup(data):
    mySession= DBSession()
    max_id = mySession.query(func.ifnull(func.max(Regsection.section_id),0).label("id_max")).one()
    max_order = mySession.query(func.ifnull(func.max(Regsection.section_order),0).label("id_max")).filter(Regsection.user_name==data['user_name']).filter(Regsection.project_cod==data['project_cod']).one()
    newGroup = Regsection(user_name=data['user_name'], project_cod=data['project_cod'],section_id=max_id.id_max+1,section_name=data['section_name'],section_content=data['section_content'], section_order=max_order.id_max+1, section_color=data['section_color'])
    try:
        transaction.begin()
        mySession.add(newGroup)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def TotalGroupPerProject(user,project):
    mySession = DBSession()
    total = mySession.query(func.count(Regsection).label("total")).filter(Regsection.user_name== user, Regsection.project_cod==project).one()

    return total.total+1

def UserGroups(user, project):
    res = []
    mySession = DBSession()
    result = mySession.query(Regsection).filter(Regsection.user_name== user, Regsection.project_cod==project).order_by(Regsection.section_order).all()

    for group in result:
        res.append({"user_name":group.user_name,"project_cod":group.project_cod, "section_id": group.section_id,"section_name":group.section_name.decode('latin1'), "section_content":group.section_content.decode('latin1'),"section_color":group.section_color})

    mySession.close()
    return res

def changeGroupOrder(groupid, order, user,project):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Regsection).filter(Regsection.user_name == user).filter(Regsection.project_cod == project).filter(Regsection.section_id == groupid).update({Regsection.section_order :order})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def AddQuestionToGroup(data):
    mySession= DBSession()
    max_order = mySession.query(func.ifnull(func.max(Registry.question_order),0).label("id_max")).filter(Registry.user_name==data['user_name']).filter(Registry.project_cod==data['project_cod']).filter(Registry.section_id==data['section_id']).one()
    newQuestion = Registry(user_name=data['user_name'], project_cod=data['project_cod'],question_id=data['question_id'],section_user=data['section_user'],section_project=data['section_project'],section_id=data['section_id'],question_order=max_order.id_max+1)
    try:
        transaction.begin()
        mySession.add(newQuestion)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def changeQuestionOrder(question_id,order, group_id, user,project):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Registry).filter(Registry.project_cod == project).filter(Registry.user_name == user).filter(Registry.section_id == group_id).filter(Registry.question_id == question_id).update({Registry.question_order :order})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e


"""def addQuestion(data):
    mySession= DBSession()
    newQuestion = Question( question_desc=data['question_desc'], question_notes=data['question_notes'], question_unit=data['question_unit'], question_dtype=data['question_dtype'], question_oth=data['question_oth'],question_cmp=data['question_cmp'],question_reqinreg=data['question_reqinreg'], question_reqinasses=data['question_reqinasses'], question_optperprj=data['question_optperprj'],parent_question=None, user_name=data['user_name'])
    try:
        transaction.begin()
        mySession.add(newQuestion)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def updateQuestion(data):
    mySession= DBSession()
    try:
        transaction.begin()
        mySession.query(Question).filter(Question.user_name ==data['user_name']).filter(Question.question_id == data['question_id']).update({Question.question_desc:data['question_desc'], Question.question_notes:data['question_notes'], Question.question_unit:data['question_unit'], Question.question_dtype:data['question_dtype'], Question.question_oth:data['question_oth'],Question.question_cmp:data['question_cmp'],Question.question_reqinreg:data['question_reqinreg'], Question.question_reqinasses:data['question_reqinasses'], Question.question_optperprj:data['question_optperprj'],Question.parent_question:None})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e"""