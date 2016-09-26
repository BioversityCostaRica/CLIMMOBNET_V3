import uuid

import transaction
from sqlalchemy import func
from sqlalchemy import or_

from models import DBSession, Question, Regsection, Registry, Qstoption
from encdecdata import encodeData,decodeData

import xlwt

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
    result = 0
    result = mySession.query(func.count(Regsection).label("total")).filter(Regsection.project_cod==data['project_cod']).filter(Regsection.user_name==data['user_name']).filter(Regsection.section_name==data['section_name']).one()
    if result.total<=0:
        max_id = mySession.query(func.ifnull(func.max(Regsection.section_id),0).label("id_max")).filter(Regsection.project_cod==data['project_cod']).one()
        max_order = mySession.query(func.ifnull(func.max(Regsection.section_order),0).label("id_max")).filter(Regsection.user_name==data['user_name']).filter(Regsection.project_cod==data['project_cod']).one()
        newGroup = Regsection(user_name=data['user_name'], project_cod=data['project_cod'],section_id=max_id.id_max+1,section_name=data['section_name'],section_content=data['section_content'], section_order=max_order.id_max+1, section_color=data['section_color'])
        try:
            transaction.begin()
            mySession.add(newGroup)
            transaction.commit()
            mySession.close()
            return True,""

        except Exception, e:
            transaction.abort()
            mySession.close()
            return False,e
    else:
        return False, "repeated"

def TotalGroupPerProject(user,project):
    mySession = DBSession()
    total = mySession.query(func.count(Regsection).label("total")).filter(Regsection.user_name== user, Regsection.project_cod==project).one()

    return total.total+1

def UserGroups(user, project):
    res = []
    mySession = DBSession()

    result = mySession.query(Regsection, mySession.query(func.count(Registry)).filter(Registry.question_id == Question.question_id).filter(Question.question_reqinreg == 1).filter(Registry.user_name==user).filter(Registry.project_cod==project).filter(Registry.section_id == Regsection.section_id).label("total")).filter(Regsection.user_name== user, Regsection.project_cod==project).order_by(Regsection.section_order).all()


    for group in result:
        print group
        res.append({"user_name":group.Regsection.user_name,"project_cod":group.Regsection.project_cod, "section_id": group.Regsection.section_id,"section_name":group.Regsection.section_name.decode('latin1'), "section_content":group.Regsection.section_content.decode('latin1'),"section_color":group.Regsection.section_color, "totalrequired": group.total})

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

def moveQuestionToGroup(data):
    mySession= DBSession()
    try:
        transaction.begin()
        max_order = mySession.query(func.ifnull(func.max(Registry.question_order),0).label("id_max")).filter(Registry.user_name==data['user_name']).filter(Registry.project_cod==data['project_cod']).filter(Registry.section_id==data['target_group']).one()
        mySession.query(Registry).filter(Registry.project_cod == data['project_cod']).filter(Registry.user_name == data['user_name']).filter(Registry.section_id == data['section_id']).filter(Registry.question_id == data['question_id']).update({Registry.section_id:data['target_group'], Registry.question_order :max_order.id_max+1})
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False,e

def DeleteGroup(data):
    mySession = DBSession()
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Regsection).filter(Regsection.user_name ==data['user_name']).filter(Regsection.project_cod==data['project_cod']).filter(Regsection.section_id==data['section_id']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()

        return False, e

def DeleteGroupQuestion(data):
    mySession = DBSession()
    try:
        mySession= DBSession()
        transaction.begin()
        mySession.query(Registry).filter(Registry.user_name ==data['user_name']).filter(Registry.project_cod==data['project_cod']).filter(Registry.section_id==data['section_id']).filter(Registry.question_id==data['question_id']).delete()
        transaction.commit()
        mySession.close()
        return True,""
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()

        return False, e

def generateFile(user,projectid):
    mySession =DBSession()

    book = xlwt.Workbook()

    sheet1 = book.add_sheet("survey")
    sheet1.write(0, 0, 'type')
    sheet1.write(0, 1, 'name')
    sheet1.write(0, 2, 'label')
    sheet1.write(0, 3, 'hint')
    sheet1.write(0, 4, 'constraint')
    sheet1.write(0, 5, 'constraint_message')
    sheet1.write(0, 6, 'required')
    sheet1.write(0, 7, 'required_message')
    sheet1.write(0, 8, 'appearance')
    sheet1.write(0, 9, 'default')
    sheet1.write(0, 10, 'relevant')
    sheet1.write(0, 11, 'repeat_count')
    sheet1.write(0, 12, 'read_only')
    sheet1.write(0, 13, 'choice_filter')
    sheet1.write(0, 14, 'calculation')

    sheet2 = book.add_sheet("choices")
    sheet2.write(0, 0, 'list_name')
    sheet2.write(0, 1, 'name')
    sheet2.write(0, 2, 'label')

    sheet3 = book.add_sheet("settings")
    sheet3.write(0, 0, 'form_title')
    sheet3.write(0, 1, 'form_id')
    sheet3.write(0, 2, 'instance_name')

    sheet3.write(1,0,projectid)
    sheet3.write(1,1,projectid.replace(" ", "_"))

    groups =mySession.query(Regsection).filter(Regsection.user_name==user).filter(Regsection.project_cod==projectid).order_by(Regsection.section_order).all()
    rowcountersurvey=0
    rowcounterchoices=0
    for group in groups:
        """               Inicia el encabezado de un grupo               """
        rowcountersurvey = rowcountersurvey + 1
        sheet1.write(rowcountersurvey,0,'begin group')
        sheet1.write(rowcountersurvey,1,'group_'+str(group.section_id))
        sheet1.write(rowcountersurvey,2,str(group.section_name).decode('latin1'))
        sheet1.write(rowcountersurvey,8,'field-list')
        rowcountersurvey = rowcountersurvey + 2
        """--------------------------------------------------------------"""

        questionsingroup =mySession.query(Registry).filter(Registry.user_name==user).filter(Registry.project_cod==projectid).filter(Registry.section_id==group.section_id).order_by(Registry.question_order).all()
        for questioningroup in questionsingroup:

            question = mySession.query(Question).filter(Question.question_id == questioningroup.question_id).one()

            if question.question_dtype ==1:
                sheet1.write(rowcountersurvey,0,'text')
            else:
                if question.question_dtype ==2:
                    sheet1.write(rowcountersurvey,0,'decimal')
                else:
                    if question.question_dtype ==3:
                        sheet1.write(rowcountersurvey,0,'integer')
                    else:
                        if question.question_dtype ==4:
                            sheet1.write(rowcountersurvey,0,'geopoint')
                        else:
                            if question.question_dtype ==5 or question.question_dtype ==7:
                                sheet1.write(rowcountersurvey,0,'select_one list_'+str(question.question_id))
                            else:
                                if question.question_dtype ==6:
                                    sheet1.write(rowcountersurvey,0,'select_multiple list_'+str(question.question_id))

            if question.question_dtype ==5 or question.question_dtype ==6:
                options = mySession.query(Qstoption).filter(Qstoption.question_id==question.question_id).all()
                rowcounterchoices =rowcounterchoices + 2
                for option in options:
                    sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                    sheet2.write(rowcounterchoices,1,str(option.value_code))
                    sheet2.write(rowcounterchoices,2,str(option.value_desc))
                    rowcounterchoices =rowcounterchoices + 1

            if question.question_dtype ==7:
                sheet1.write(rowcountersurvey,8,'minimal')
                rowcounterchoices =rowcounterchoices+2
                sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                sheet2.write(rowcounterchoices,1,str('1'))
                sheet2.write(rowcounterchoices,2,str('paquete 1'))
                rowcounterchoices =rowcounterchoices + 1
                sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                sheet2.write(rowcounterchoices,1,str('2'))
                sheet2.write(rowcounterchoices,2,str('paquete 2'))
                rowcounterchoices =rowcounterchoices + 1
                sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                sheet2.write(rowcounterchoices,1,str('3'))
                sheet2.write(rowcounterchoices,2,str('paquete 3'))
                rowcounterchoices =rowcounterchoices + 1
                sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                sheet2.write(rowcounterchoices,1,str('4'))
                sheet2.write(rowcounterchoices,2,str('paquete 4'))
                rowcounterchoices =rowcounterchoices + 1
                sheet2.write(rowcounterchoices,0,'list_'+str(question.question_id))
                sheet2.write(rowcounterchoices,1,str('5'))
                sheet2.write(rowcounterchoices,2,str('paquete 5'))
                rowcounterchoices =rowcounterchoices + 1


            sheet1.write(rowcountersurvey,1,'question_'+str(question.question_id))
            sheet1.write(rowcountersurvey,2,str(question.question_desc).decode('latin1'))
            sheet1.write(rowcountersurvey,3,str(question.question_unit).decode('latin1'))

            if question.question_reqinreg==1:
                sheet1.write(rowcountersurvey,6,'yes')

            rowcountersurvey = rowcountersurvey + 1


        """--------------------------------------------------------------"""
        """               Cierra el encabezado de un grupo               """
        rowcountersurvey = rowcountersurvey + 1
        sheet1.write(rowcountersurvey,1,'group_'+str(group.section_id))
        sheet1.write(rowcountersurvey,0,'end group')
        rowcountersurvey = rowcountersurvey + 1
        """--------------------------------------------------------------"""

    book.save(projectid.replace(" ", "_")+".xls")


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