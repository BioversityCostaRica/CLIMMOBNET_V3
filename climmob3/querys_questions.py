import uuid

import transaction
from sqlalchemy import func

from models import DBSession, Question
from encdecdata import encodeData,decodeData


def UserQuestion(user):
    res = []
    mySession = DBSession()
    result = mySession.query(Question).filter(Question.user_name == user).all()
    for question in result:
        res.append({"question_id":question.question_id,"question_desc":question.question_desc.decode('latin1'),'question_notes':question.question_notes.decode('latin1'),'question_unit':question.question_unit.decode('latin1'), 'question_dtype': question.question_dtype,'question_oth': question.question_oth,'question_cmp': question.question_cmp,'question_reqinreg': question.question_reqinreg,'question_reqinasses': question.question_reqinasses,'question_optperprj': question.question_optperprj,'parent_question': question.parent_question,'user_name': question.user_name })

    mySession.close()
    return res

def addQuestion(data):
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
        return False,e


def deleteQuestion(data):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Question).filter(Question.question_id==data['question_id']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()

        return False, e