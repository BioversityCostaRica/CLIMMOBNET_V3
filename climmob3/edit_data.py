from models import DBSession
from sqlalchemy import or_, func, text
from glob import glob
import xml.etree.ElementTree as ET


def fill_table(db_name):
    mySession = DBSession()
    sql = "select originid, surveyid from %s.reg_maintable;" % db_name
    result = mySession.execute(sql)
    res = []
    for i in result:
        res.append([i[0], i[1]])
    mySession.close()
    return res


def make_selOne(bd, defa, multi, reg):
    mySession = DBSession()
    design=''
    if reg:
        mm = 'multiple'
    else:
        mm = 'multiple2'
    if (multi == ""):
        result = mySession.execute('select question_9_cod as qc,question_9_des as qd from %s.reg_lkpquestion_9;' % bd)
        design = '<select ' + str(multi) + ' class="form-control" style="width:100%;display:inline;" >'
    else:
        result = mySession.execute('select question_10_cod as qc,question_10_des as qd from %s.reg_lkpquestion_10;' % bd)
        design = '<select '+str(multi)+' class="'+mm+' form-control" style="width:100%;display:inline;" >'

    for res in result:
        if (str(res['qc']) in str(defa)):
            print res['qc']
            design = design + '<option selected="selected">' + res['qd'] + '</option>'
        else:
            design = design + '<option >' + res['qd'] + '</option>'
    mySession.close()
    design += '</select>'
    return design


def getTableContent(f, bd, sur_id):
    tree = ET.parse(f)
    query = 'select '
    style = []  # [label, type] type=1=input,2 dropdown,3dropdowchek
    design = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'
    for table in tree.iter('table'):
        if table.attrib['name'] == 'reg_maintable':
            for field in table:
                if field.attrib['name'] != 'rowuuid':
                    try:
                        x = field.attrib['name'] + '\t*-*-*\t' + field.attrib['desc'] + '\t*-*-*\t' + field.attrib[
                            'type']
                        query = query + ' ' + field.attrib['name'] + ' as "' + field.attrib['desc'] + '", '
                        st = []
                        st.append(field.attrib['desc'])
                        if ('_10' in field.attrib['name']):
                            st.append(3)
                        else:
                            if '_9' in field.attrib['name']:
                                st.append(2)
                            else:
                                st.append(1)
                        style.append(st)
                    except:
                        pass
    sql = query[:-2] + ' from %s.reg_maintable where surveyid=%s;' % (bd, sur_id)
    mySession = DBSession()
    result = mySession.execute(sql)
    mySession.close()
    # print result
    for res in result:
        for i, r in enumerate(res):
            if 'Survey ID' not in style[i][0] and 'Origin ID' not in style[i][0]:
                if style[i][1] == 1:
                    design = design + '<td>' + style[i][
                        0] + '</td><td><input class ="form-control" type="text" value="' + str(r) + '" /></td>'

                if style[i][1] == 2 or style[i][1] == 3:
                    if ( style[i][1]==3):
                        multi = 'multiple="multiple" id="multi" '
                        r = r.split(',')
                    else:
                        multi = ''
                    design = design + '<td>' + style[i][0] + '</td><td>' + make_selOne(bd, str(r), multi, True)
                if (i % 2 == 0):
                    design = '<tr>' + design
                else:
                    design = design + '</tr>'

    return design + '</table>'


def fill_table_content(db, sur_id, path):
    file = "/home/lluis/Tmp/repo/www/DB/REG/create.xml"
    content = getTableContent(file, 'www', sur_id)
    return content

def getNamesEditByColums(db):
    file = "/home/lluis/Tmp/repo/www/DB/REG/create.xml"
    tree = ET.parse(file)
    columns=[]

    for table in tree.iter('table'):
        if table.attrib['name'] == 'reg_maintable' and '_msel_' not in table.attrib['name']:
            for field in table:
                if field.attrib['name'] not in ['rowuuid','surveyid','originid'] and '_msel_' not in field.attrib['name']:
                    columns.append([field.attrib['name'],field.attrib['desc']])
    return columns


def fillDataTable(db, columns):
    sql='select '
    db='www'
    data=[]
    row=[]
    style = [] # [label, type] type=1=input,2 dropdown,3dropdowchek

    for col in columns:
        print col
        col=col.split("$%*")
        if ('_10' in col[0]):
            style.append([col[1], 3])
        else:
            if ('_9' in col[0]):
                style.append([col[1], 2])
            else:
                style.append([col[1], 1])
        sql = sql + col[0] + ','
        row.append(col[1])
    sql = sql[:-1]+' from %s.reg_maintable' %db


    mySession = DBSession()
    result = mySession.execute(sql)
    data.append(row[:])
    del row[:]
    design = '<table class="table table-striped table-hover table-bordered" id="editable-sample"><thead><tr>'
    design += '<th></th>'
    for lbl in style:
        design += '<th>' + lbl[0] + '</th>'

    design += '</tr></thead><tbody>'
    count = 0
    for res in result:
        count += 1
        design += '<tr class=""><td>%s</td>' %str(count)

        for i, r in enumerate(res):
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>"+str(i)
            if style[i][1] == 1:
                design += '<td><input class ="form-control" type="text" value="' + str(r) + '" style="width: 100%" /></td>'
                row.append(str(r))
            else:
                if style[i][1] == 2:
                    design += '<td>' + make_selOne(db, str(r), '', False) + '</td>'
                    row.append(str(r))
                else:
                    if style[i][1] == 3:
                        design += '<td>' + make_selOne(db, str(r), ' multiple="multiple" id="multi" ',False) + '</td>'
                    row.append(str(r))

        data.append(row[:])
        design +='</tr>'
        del row[:]
    mySession.close()

    design+= '</tbody></table>'

    print '***********DESIGN*************'
    print design
    print '******************************'
    #return data
    return  design
