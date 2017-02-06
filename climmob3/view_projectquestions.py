
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from viewclasses import publicView, privateView


from resources import  ColorPickerJs,QuestionsInProject,moveQuestionAutoShow,addGroupAutoShow
from querys_countries import ProjectBelongsToUser
from querys_projectquestions import Prj_UserQuestion,AvailableQuestions, \
    UserGroups,AddGroup,changeGroupOrder,TotalGroupPerProject,AddQuestionToGroup,changeQuestionOrder,moveQuestionToGroup, generateFile, DeleteGroup, DeleteGroupQuestion, \
    AvailableQuestionsAssessment,UserGroupsAssessment,AddGroupAssessment,PrjUserQuestionAssessment,changeGroupOrderAssessment,TotalGroupPerProjectAssessment,AddQuestionToGroupAssessment,\
    changeQuestionOrderAssessment,moveQuestionToGroupAssessment,DeleteGroupAssessment,DeleteGroupQuestionAssessment
import os
from pyxform import xls2xform

@view_config(route_name='projectregistrationquestions', renderer='templates/project/projectquestions.html')
class questionsInProject(privateView):
    def processView(self):



        QuestionsInProject.need()
        ColorPickerJs.need()
        projectid = self.request.matchdict['projectid']

        path = self.request.registry.settings['odk.repository']+projectid.replace(" ", "_")+"/"

        dataworking = {}
        error_summary = {}
        accordion_open=""
        movequestion = False
        deleteelemente = False
        addgrouptoproject =False
        saveordergroup = False
        saveorderquestions = False
        data = ProjectBelongsToUser(self.user.login, projectid)
        if not data:
            raise HTTPNotFound()
        else:
            if(self.request.method == 'POST'):
                accordion_open = self.request.POST.get('txt_accordion_open','')
                dataworking['user_name']=self.user.login
                dataworking['project_cod']= projectid

                if 'btn_add_group' in self.request.POST:
                    dataworking['section_name'] = self.request.POST.get('txt_group_name','')
                    dataworking['section_content'] = self.request.POST.get('txt_group_desc','')
                    dataworking['section_color'] = ''

                    total =TotalGroupPerProject(self.user.login,projectid)

                    while (total>11):
                        total =total-11

                    if total== 1:
                        dataworking['section_color'] = '#4643E8'
                    else:
                        if total== 2:
                            dataworking['section_color'] = '#449d44'
                        else:
                            if total== 3:
                                dataworking['section_color'] = '#BB0CE8'
                            else:
                                if total== 4:
                                    dataworking['section_color'] = '#E8640C'
                                else:
                                    if total== 5:
                                        dataworking['section_color'] = '#17AAFF'
                                    else:
                                        if total== 6:
                                            dataworking['section_color'] = '#FFBF0D'
                                        else:
                                            if total== 7:
                                                dataworking['section_color'] = '#1f78b4'
                                            else:
                                                if total== 8:
                                                    dataworking['section_color'] = '#FF0000'
                                                else:
                                                    if total== 9:
                                                        dataworking['section_color'] = '#35D51C'
                                                    else:
                                                        if total== 10:
                                                            dataworking['section_color'] = '#E80CA3'
                                                        else:
                                                            if total== 11:
                                                                dataworking['section_color'] = '#ABD500'


                    if dataworking['section_name'] !='':
                        if dataworking['section_content'] !='':

                            addgroup,message = AddGroup(dataworking)

                            if not addgroup:
                                if message=="repeated":
                                    error_summary = {'repeated': "There is already a group with this name."}
                                else:
                                    error_summary = {'dberror': message}
                            else:
                                addgrouptoproject = True
                        else:
                            error_summary = {'sectiondescription': self._("The description of the group can not be empty.")}
                    else:
                        error_summary = {'sectionname': self._("The name of the group can not be empty.")}

                    if error_summary>0:
                        addGroupAutoShow.need()

                if 'btnsaveordergroup' in self.request.POST:
                    groups = self.request.POST.get('txt_groups','')

                    part = groups.split(',')
                    cont=0
                    for element in part:
                        cont = cont+1
                        attr = element.split('_')
                        cgo,message = changeGroupOrder(attr[1],cont,self.user.login, projectid)
                        if not cgo:
                            print "error en la base "+message
                        else:
                            saveordergroup = True

                if 'btn_add_question_to_group' in self.request.POST:

                    dataworking['section_user'] = self.request.POST.get('txt_section_user','')
                    dataworking['section_project'] = self.request.POST.get('txt_section_project','')
                    dataworking['section_id'] = self.request.POST.get('txt_section_id','')
                    dataworking['question_id'] = ""

                    questions_ids=self.request.POST.get('txt_id_questions','')
                    part = questions_ids.split(',')
                    many = len(part)
                    for x in range(0,many-1):
                        dataworking['question_id'] = part[x]

                        addq, message =AddQuestionToGroup(dataworking)

                        if not addq:
                            print "error en la base "
                        else:
                            print "agrego pregunta bien"

                if 'btnsaveorderquestions' in self.request.POST:

                    groups = self.request.POST.get('txt_groups','')
                    part = groups.split(',')

                    for element in part:

                        attr = element.split('_')
                        questions = self.request.POST.get('txtquestion_'+str(attr[1]),'')

                        if questions!="":
                            part_question = questions.split(',')
                            cont=0
                            for question in part_question:
                                if question!="":
                                    cont = cont + 1
                                    id_question = question.split('_')

                                    cqo, message = changeQuestionOrder(id_question[1],cont,attr[1],self.user.login,projectid)

                                    if not cqo:
                                        print "error en la base "+message
                                    else:
                                        saveorderquestions = True

                if 'btn_move_question' in self.request.POST:
                    groupid    = self.request.POST.get('move_groupid','')
                    questionid = self.request.POST.get('move_questionid','')
                    target_group =self.request.POST.get('cmbgroups','')

                    dataworking['section_id'] = groupid
                    dataworking['question_id'] = questionid
                    dataworking['target_group'] = target_group

                    if dataworking['target_group'] !="":
                        mv, message = moveQuestionToGroup(dataworking)
                        if not mv:
                            error_summary = {'dberror': message}
                        else:
                            movequestion = True
                    else:
                        error_summary = {'target_groupempty': self._("the target group can not be empty.")}

                    if error_summary>0:
                        moveQuestionAutoShow.need()

                if 'btn_delete_element' in self.request.POST:
                    groupid= self.request.POST.get('delete_group_id','')
                    questionid=  self.request.POST.get('delete_question_id','')

                    if questionid == "":
                        dataworking['section_id'] = groupid
                        dltelement,message = DeleteGroup(dataworking)

                        if not dltelement:
                            error_summary = {'dberror':message}
                        else:
                            deleteelemente = True
                    else:
                        dataworking['section_id'] = groupid
                        dataworking['question_id'] = questionid
                        dltelement,message = DeleteGroupQuestion(dataworking)

                        if not dltelement:
                            error_summary = {'dberror':message}
                        else:
                            deleteelemente = True


                if not os.path.exists(path[:-1]):
                    os.mkdir(path[:-1])
                    os.mkdir(path+"ODK")
                    os.mkdir(path+"DB")
                    os.mkdir(path+"DB/REG")
                    os.mkdir(path+"DB/ASS")
                    os.mkdir(path+"DATA")
                    os.mkdir(path+"DATA/XML")
                    os.mkdir(path+"DATA/JSON")

                if os.path.exists(path+"ODK/registry.xlsx"):
                    os.unlink(path+"ODK/registry.xlsx")

                if os.path.exists(path+"ODK/registry.xml"):
                    os.unlink(path+"ODK/registry.xml")

                generateFile(self.user.login, projectid, "registry", path+"ODK/")

                xls2xform.xls2xform_convert(path+"ODK/registry.xlsx",path+"ODK/registry.xml")


            return {'activeUser':self.user,'error_summary':error_summary,'addgrouptoproject':addgrouptoproject,'saveordergroup':saveordergroup,'saveorderquestions':saveorderquestions, 'movequestion':movequestion,'deleteelemente':deleteelemente, 'UserGroups':UserGroups(self.user.login,projectid), 'Questions':AvailableQuestions(self.user.login, projectid), 'Prj_UserQuestion':Prj_UserQuestion(self.user.login, projectid), 'accordion_open':accordion_open, 'dataworking':dataworking, 'archive':projectid.replace(" ", "_")+"_"+self._("registry")+".xml"}

@view_config(route_name='projectobservationsquestions', renderer='templates/project/projectquestions.html')
class questionsObservationsInProject(privateView):
    def processView(self):

        QuestionsInProject.need()
        ColorPickerJs.need()
        projectid = self.request.matchdict['projectid']

        path = self.request.registry.settings['odk.repository']+projectid.replace(" ", "_")+"/"

        dataworking = {}
        error_summary = {}
        accordion_open=""
        movequestion = False
        deleteelemente = False
        addgrouptoproject =False
        saveordergroup = False
        saveorderquestions = False
        data = ProjectBelongsToUser(self.user.login, projectid)
        if not data:
            raise HTTPNotFound()
        else:
            if(self.request.method == 'POST'):
                accordion_open = self.request.POST.get('txt_accordion_open','')
                dataworking['user_name']=self.user.login
                dataworking['project_cod']= projectid

                if 'btn_add_group' in self.request.POST:
                    dataworking['section_name'] = self.request.POST.get('txt_group_name','')
                    dataworking['section_content'] = self.request.POST.get('txt_group_desc','')
                    dataworking['section_color'] = ''

                    total =TotalGroupPerProjectAssessment(self.user.login,projectid)

                    while (total>11):
                        total =total-11

                    if total== 1:
                        dataworking['section_color'] = '#4643E8'
                    else:
                        if total== 2:
                            dataworking['section_color'] = '#449d44'
                        else:
                            if total== 3:
                                dataworking['section_color'] = '#BB0CE8'
                            else:
                                if total== 4:
                                    dataworking['section_color'] = '#E8640C'
                                else:
                                    if total== 5:
                                        dataworking['section_color'] = '#17AAFF'
                                    else:
                                        if total== 6:
                                            dataworking['section_color'] = '#FFBF0D'
                                        else:
                                            if total== 7:
                                                dataworking['section_color'] = '#1f78b4'
                                            else:
                                                if total== 8:
                                                    dataworking['section_color'] = '#FF0000'
                                                else:
                                                    if total== 9:
                                                        dataworking['section_color'] = '#35D51C'
                                                    else:
                                                        if total== 10:
                                                            dataworking['section_color'] = '#E80CA3'
                                                        else:
                                                            if total== 11:
                                                                dataworking['section_color'] = '#ABD500'


                    if dataworking['section_name'] !='':
                        if dataworking['section_content'] !='':

                            addgroup,message = AddGroupAssessment(dataworking)

                            if not addgroup:
                                if message=="repeated":
                                    error_summary = {'repeated': "There is already a group with this name."}
                                else:
                                    error_summary = {'dberror': message}
                            else:
                                addgrouptoproject = True
                        else:
                            error_summary = {'sectiondescription': self._("The description of the group can not be empty.")}
                    else:
                        error_summary = {'sectionname': self._("The name of the group can not be empty.")}

                    if error_summary>0:
                        addGroupAutoShow.need()

                if 'btnsaveordergroup' in self.request.POST:
                    groups = self.request.POST.get('txt_groups','')

                    part = groups.split(',')
                    cont=0
                    for element in part:
                        cont = cont+1
                        attr = element.split('_')
                        cgo,message = changeGroupOrderAssessment(attr[1],cont,self.user.login, projectid)
                        if not cgo:
                            print "error en la base "+message
                        else:
                            saveordergroup = True

                if 'btn_add_question_to_group' in self.request.POST:

                    dataworking['section_user'] = self.request.POST.get('txt_section_user','')
                    dataworking['section_project'] = self.request.POST.get('txt_section_project','')
                    dataworking['section_id'] = self.request.POST.get('txt_section_id','')
                    dataworking['question_id'] = ""

                    questions_ids=self.request.POST.get('txt_id_questions','')
                    part = questions_ids.split(',')
                    many = len(part)
                    for x in range(0,many-1):
                        dataworking['question_id'] = part[x]

                        addq, message =AddQuestionToGroupAssessment(dataworking)

                        if not addq:
                            print "error en la base "+message
                        else:
                            print "agrego pregunta bien"

                if 'btnsaveorderquestions' in self.request.POST:

                    groups = self.request.POST.get('txt_groups','')
                    part = groups.split(',')

                    for element in part:

                        attr = element.split('_')
                        questions = self.request.POST.get('txtquestion_'+str(attr[1]),'')

                        if questions!="":
                            part_question = questions.split(',')
                            cont=0
                            for question in part_question:
                                if question!="":
                                    cont = cont + 1
                                    id_question = question.split('_')

                                    cqo, message = changeQuestionOrderAssessment(id_question[1],cont,attr[1],self.user.login,projectid)

                                    if not cqo:
                                        print "error en la base "+message
                                    else:
                                        saveorderquestions = True

                if 'btn_move_question' in self.request.POST:
                    groupid    = self.request.POST.get('move_groupid','')
                    questionid = self.request.POST.get('move_questionid','')
                    target_group =self.request.POST.get('cmbgroups','')

                    dataworking['section_id'] = groupid
                    dataworking['question_id'] = questionid
                    dataworking['target_group'] = target_group

                    if dataworking['target_group'] !="":
                        mv, message = moveQuestionToGroupAssessment(dataworking)
                        if not mv:
                            error_summary = {'dberror': message}
                        else:
                            movequestion = True
                    else:
                        error_summary = {'target_groupempty': self._("the target group can not be empty.")}

                    if error_summary>0:
                        moveQuestionAutoShow.need()

                if 'btn_delete_element' in self.request.POST:
                    groupid= self.request.POST.get('delete_group_id','')
                    questionid=  self.request.POST.get('delete_question_id','')

                    if questionid == "":
                        dataworking['section_id'] = groupid
                        dltelement,message = DeleteGroupAssessment(dataworking)

                        if not dltelement:
                            error_summary = {'dberror':message}
                        else:
                            deleteelemente = True
                    else:
                        dataworking['section_id'] = groupid
                        dataworking['question_id'] = questionid
                        dltelement,message = DeleteGroupQuestionAssessment(dataworking)

                        if not dltelement:
                            error_summary = {'dberror':message}
                        else:
                            deleteelemente = True

                if not os.path.exists(path[:-1]):
                    os.mkdir(path[:-1])
                    os.mkdir(path+"ODK")
                    os.mkdir(path+"DB")
                    os.mkdir(path+"DB/REG")
                    os.mkdir(path+"DB/ASS")
                    os.mkdir(path+"DATA")
                    os.mkdir(path+"DATA/XML")
                    os.mkdir(path+"DATA/JSON")

                if os.path.exists(path+"ODK/assessment.xlsx"):
                    os.unlink(path+"ODK/assessment.xlsx")

                if os.path.exists(path+"ODK/assessment.xml"):
                    os.unlink(path+"ODK/assessment.xml")

                generateFile(self.user.login, projectid, "assessment", path+"ODK/")

                #os.system("python climmob3/pyxform-master/pyxform/xls2xform.py "+path+"ODK/assessment.xlsx "+path+"ODK/assessment.xml")
                xls2xform.xls2xform_convert(path+"ODK/assessment.xlsx",path+"ODK/assessment.xml")


            return {'activeUser':self.user,'error_summary':error_summary,'addgrouptoproject':addgrouptoproject,'saveordergroup':saveordergroup,'saveorderquestions':saveorderquestions, 'movequestion':movequestion,'deleteelemente':deleteelemente, 'UserGroups':UserGroupsAssessment(self.user.login,projectid), 'Questions':AvailableQuestionsAssessment(self.user.login, projectid), 'Prj_UserQuestion':PrjUserQuestionAssessment(self.user.login, projectid), 'accordion_open':accordion_open, 'dataworking':dataworking, 'archive':projectid.replace(" ", "_")+"_"+self._("observations")+".xml"}
