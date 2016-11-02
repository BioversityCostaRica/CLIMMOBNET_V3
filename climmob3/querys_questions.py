import uuid

import transaction
from sqlalchemy import func

from models import DBSession, Question, Qstoption, Registry
from encdecdata import encodeData,decodeData


def UserQuestion(user):
    res = []
    mySession = DBSession()
    result = mySession.query(Question).filter(Question.user_name == user).all()
    for question in result:
        includedquery = mySession.query(func.count(Registry.question_id).label("total")).filter(Registry.question_id == question.question_id).one()
        #includedquery = mySession.query(func.count(Question.).label("total")).one()


        res.append({"question_id":question.question_id,"question_desc":question.question_desc.decode('latin1'),'question_notes':question.question_notes.decode('latin1'),'question_unit':question.question_unit.decode('latin1'), 'question_dtype': question.question_dtype,'question_oth': question.question_oth,'question_cmp': question.question_cmp,'question_reqinreg': question.question_reqinreg,'question_reqinasses': question.question_reqinasses,'question_optperprj': question.question_optperprj,'parent_question': question.parent_question,'user_name': question.user_name,'included': includedquery.total })

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

def addOptionToQuestion(value_desc):
    mySession= DBSession()

    max_id_question = mySession.query(func.ifnull(func.max(Question.question_id),0).label("id_max")).one()
    max_id = mySession.query(func.ifnull(func.max(Qstoption.value_code),0).label("id_max")).filter(Qstoption.question_id==max_id_question.id_max).one()

    newQstoption= Qstoption(question_id = max_id_question.id_max, value_code=max_id.id_max+1, value_desc=value_desc)
    try:
        transaction.begin()
        mySession.add(newQstoption)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def addOptionToQuestion_modify(id_question,value_desc):
    mySession= DBSession()

    max_id = mySession.query(func.ifnull(func.max(Qstoption.value_code),0).label("id_max")).filter(Qstoption.question_id==id_question).one()

    newQstoption= Qstoption(question_id = id_question, value_code=max_id.id_max+1, value_desc=value_desc)
    try:
        transaction.begin()
        mySession.add(newQstoption)
        transaction.commit()
        mySession.close()
        return True,""

    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def updateOptionQuestion(options,id_question):
    mySesion =DBSession()
    print options
    result = mySesion.query(Qstoption).filter(Qstoption.question_id == id_question).filter(Qstoption.value_desc.notin_(options.split(','))).all()
    for option in result:
        deleteOptionQuestion(option.value_code, id_question)

    result = mySesion.query(Qstoption).filter(Qstoption.question_id == id_question).filter(Qstoption.value_desc.in_(options.split(','))).all()
    part = options.split(',')
    for element in part:
        encontrado = False
        for option in result:
            if element == option.value_desc:
                encontrado = True

        if encontrado == False:
            addOptionToQuestion_modify(id_question, element)


def deleteOptionQuestion(id_option,id_question):
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Qstoption).filter(Qstoption.value_code==id_option).filter(Qstoption.question_id==id_question).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()

        return False, e

def QuestionsOptions(user):
    res = []
    mySession = DBSession()
    subquery = mySession.query(Question.question_id).filter(Question.user_name==user).filter(Question.question_dtype.in_([5,6]))
    result = mySession.query(Qstoption).filter(Qstoption.question_id.in_(subquery)).all()
    for option in result:
        res.append({"question_id":option.question_id,"value_code":option.value_code, "value_desc":option.value_desc.decode('latin1') })
    mySession.close()
    return res

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