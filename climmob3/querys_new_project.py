import transaction

from models import DBSession, Project, Country
from sqlalchemy import or_, func,text
import os

def PrepareDataBase(projectid,dbuser,dbpassword,path):
    mySession = DBSession()
    sql = "create database "+projectid +";"
    result=mySession.execute(sql)
    mySession.close()

    print "mysql -u "+dbuser+" --password = "+dbpassword+" "+projectid+" > "+path+"DB/REG/create.sql"
    os.system("mysql -u "+dbuser+" --password='"+dbpassword+"' "+projectid+" < "+path+"DB/REG/create.sql")
    os.system("mysql -u "+dbuser+" --password='"+dbpassword+"' "+projectid+" < "+path+"DB/REG/insert.sql")