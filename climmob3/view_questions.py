
from pyramid.view import view_config
from viewclasses import  privateView


from resources import  EnumeratorJS,projectJS, ProjectQuestionResources,addQuestionAutoShow,updateQuestionAutoShow,deleteQuestionAutoShow
from querys_questions import UserQuestion,addQuestion,updateQuestion,deleteQuestion,addOptionToQuestion,QuestionsOptions,updateOptionQuestion

@view_config(route_name='questions', renderer='templates/project/questions.html')
class questions_view(privateView):
    def processView(self):
        projectJS.need()
        ProjectQuestionResources.need()
        EnumeratorJS.need()
        error_summary={}
        dataworking ={}
        newquestion=False
        editquestion=False
        deletequestion=False

        if (self.request.method == 'POST'):

                if 'btn_add_question' in self.request.POST:
                    dataworking['question_notes']         = self.request.POST.get('txt_notes','')
                    dataworking['question_desc']          = self.request.POST.get('txt_description','')
                    dataworking['question_unit']          = self.request.POST.get('txt_indication','')
                    dataworking['question_dtype']         = self.request.POST.get('cmbtype','')
                    dataworking['question_twoitems']      = self.request.POST.get('txt_twoitems','')
                    dataworking['question_tri_best']      = self.request.POST.get('txt_tribest','')
                    dataworking['question_tri_worse']     = self.request.POST.get('txt_triworse','')
                    dataworking['question_moreitems']     = self._("Which was in the position:")
                    dataworking['question_select']        = self.request.POST.get('txt_select','')
                    dataworking['question_oth']           = self.request.POST.get('ckb_acceptother','')
                    dataworking['question_cmp']           = ""
                    dataworking['question_reqinreg']      = self.request.POST.get('ckb_registrationrequired','')
                    dataworking['question_reqinasses']    = self.request.POST.get('ckb_assessmentrequired','')
                    dataworking['question_requiredvalue'] = self.request.POST.get('ckb_required_value','')
                    dataworking['question_optperprj']     = ""
                    dataworking['user_name']              = self.user.login

                    if dataworking['question_reqinreg']== 'on':
                        dataworking['question_reqinreg'] = 1
                    else:
                        dataworking['question_reqinreg'] = 0

                    if dataworking['question_reqinasses']== 'on':
                        dataworking['question_reqinasses'] = 1
                    else:
                        dataworking['question_reqinasses'] = 0

                    if dataworking['question_oth']== 'on':
                        dataworking['question_oth'] = 1
                    else:
                        dataworking['question_oth'] = 0

                    if dataworking['question_requiredvalue']== 'on':
                        dataworking['question_requiredvalue'] = 1
                    else:
                        dataworking['question_requiredvalue'] = 0

                    if dataworking['question_desc'] != "" and dataworking['question_notes'] !="" and dataworking['question_dtype'] !="":
                        if dataworking['question_dtype'] == "5" or dataworking['question_dtype']== "6":
                            if dataworking['question_select'] !="":

                                dataworking['question_tri_worse'] = ""
                                dataworking['question_tri_best']  = ""
                                dataworking['question_twoitems']  = ""
                                dataworking['question_moreitems'] = ""

                                part = dataworking['question_select'].split('~')

                                if len(part)>=2:

                                    add, message = addQuestion(dataworking)

                                    if not add:
                                        error_summary = {'dberror': message}
                                    else:


                                        for element in part:
                                            addopt, message =addOptionToQuestion(element)

                                            if not addopt:
                                                error_summary = {'dberror': message}
                                            else:
                                                newquestion = True
                                else:
                                    error_summary = {'optionempty': self._("Should write options answer to your question.")}
                            else:
                                error_summary = {'optionempty': self._("Should write options answer to your question.")}
                        else:
                            if dataworking['question_dtype'] =="9":
                                if dataworking['question_twoitems'] != "" and dataworking['question_tri_worse'] != "" and dataworking['question_tri_best'] !="":

                                    add, message = addQuestion(dataworking)

                                    if not add:
                                        error_summary = {'dberror': message}
                                    else:
                                        newquestion = True
                                else:
                                    error_summary = {'questionempty': self._("Please review the information relevant questions according to the number of items.")}
                            else:
                                dataworking['question_tri_worse'] = ""
                                dataworking['question_tri_best']  = ""
                                dataworking['question_twoitems']  = ""
                                dataworking['question_moreitems'] = ""

                                add, message = addQuestion(dataworking)

                                if not add:
                                    error_summary = {'dberror': message}
                                else:
                                    newquestion = True
                    else:
                        error_summary = {'questionempty': self._("Please review the information that must complete.")}

                    if error_summary>0:
                        addQuestionAutoShow.need()

                if 'btn_modify_question' in self.request.POST:
                    dataworking['question_id']            = self.request.POST.get('modify_txt_id','')
                    dataworking['question_notes']         = self.request.POST.get('modify_txt_notes','')
                    dataworking['question_desc']          = self.request.POST.get('modify_txt_description','')
                    dataworking['question_unit']          = self.request.POST.get('modify_txt_indication','')
                    dataworking['question_dtype']         = self.request.POST.get('modify_cmbtype','')
                    dataworking['question_twoitems']      = self.request.POST.get('modify_txt_twoitems','')
                    dataworking['question_tri_best']      = self.request.POST.get('modify_txt_triadric_best','')
                    dataworking['question_tri_worse']     = self.request.POST.get('modify_txt_triadric_worse','')
                    dataworking['question_moreitems']     = self._("Which was in the position:")
                    dataworking['question_select']        = self.request.POST.get('txt_select','')
                    dataworking['question_oth']           = self.request.POST.get('modify_ckb_acceptother','')
                    dataworking['question_cmp']           = ""
                    dataworking['question_reqinreg']      = self.request.POST.get('modify_ckb_registrationrequired','')
                    dataworking['question_reqinasses']    = self.request.POST.get('modify_ckb_assessmentrequired','')
                    dataworking['question_requiredvalue'] = self.request.POST.get('modify_ckb_required_value','')
                    dataworking['question_optperprj']     = ""
                    dataworking['user_name']              = self.user.login


                    if dataworking['question_reqinreg']== 'on':
                        dataworking['question_reqinreg'] = 1
                    else:
                        dataworking['question_reqinreg'] = 0

                    if dataworking['question_reqinasses']== 'on':
                        dataworking['question_reqinasses'] = 1
                    else:
                        dataworking['question_reqinasses'] = 0

                    if dataworking['question_oth']== 'on':
                        dataworking['question_oth'] = 1
                    else:
                        dataworking['question_oth'] = 0

                    if dataworking['question_requiredvalue']== 'on':
                        dataworking['question_requiredvalue'] = 1
                    else:
                        dataworking['question_requiredvalue'] = 0

                    if dataworking['question_desc'] != "" and dataworking['question_notes'] !="" and dataworking['question_dtype'] !="":
                        if dataworking['question_dtype'] == "5" or dataworking['question_dtype']== "6":
                            if dataworking['question_select'] !="":

                                dataworking['question_tri_worse'] = ""
                                dataworking['question_tri_best']  = ""
                                dataworking['question_twoitems']  = ""
                                dataworking['question_moreitems'] = ""

                                options = ""
                                part = dataworking['question_select'].split('~')
                                contador = 0
                                for element in part:
                                    contador = contador+1
                                    if options=="":
                                        options = element
                                    else:
                                        options = options+","+element

                                #options = options[0:len(options)-1]
                                if contador >= 2:
                                    mdf, message =updateQuestion(dataworking)

                                    if not mdf:
                                        error_summary = {'dberror': message}
                                    else:
                                        editquestion = True

                                    if editquestion == True:
                                        updateOptionQuestion(options,dataworking['question_id'])
                                else:
                                    error_summary = {'optionempty': self._("Should write options answer to your question.")}
                            else:
                                error_summary = {'optionempty': self._("Should write options answer to your question.")}
                        else:
                            if dataworking['question_dtype'] =="9":
                                if dataworking['question_twoitems'] != "" and dataworking['question_tri_worse'] != "" and dataworking['question_tri_best'] !="":

                                    mdf, message =updateQuestion(dataworking)

                                    if not mdf:
                                        error_summary = {'dberror': message}
                                    else:
                                        editquestion = True
                                else:
                                    error_summary = {'questionempty': self._("Please review the information relevant questions according to the number of items.")}
                            else:
                                dataworking['question_tri_worse'] = ""
                                dataworking['question_tri_best']  = ""
                                dataworking['question_twoitems']  = ""
                                dataworking['question_moreitems'] = ""
                                mdf, message =updateQuestion(dataworking)

                                if not mdf:
                                    error_summary = {'dberror': message}
                                else:
                                    editquestion = True
                    else:
                        error_summary = {'questionempty': self._("Please review the information that must complete.")}

                    if error_summary>0:
                        updateQuestionAutoShow.need()

                if 'btn_delete_question' in self.request.POST:

                    dataworking['question_id'] = self.request.POST.get('delete_question_id','')

                    dlt,message = deleteQuestion(dataworking)

                    if not dlt:
                        error_summary = {'dberror': message}
                    else:
                        deletequestion =True

                    if error_summary>0:
                        deleteQuestionAutoShow.need()

        return {'activeUser':self.user,'error_summary':error_summary,'newquestion':newquestion,'editquestion': editquestion,'deletequestion':deletequestion,'dataworking':dataworking,'UserQuestion':UserQuestion(self.user.login),'ClimMobQuestion':UserQuestion('bioversity'), 'QuestionsOptions':QuestionsOptions(self.user.login),'ClimMobQuestionsOptions':QuestionsOptions('bioversity')}
