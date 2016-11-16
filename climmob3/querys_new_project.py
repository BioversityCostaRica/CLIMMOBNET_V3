
from models import DBSession
import os

def PrepareDataBase(projectid,dbuser,dbpassword,path):
    mySession = DBSession()
    sql = "Create database "+projectid
    result=mySession.execute(sql)
    mySession.close()

    os.system("mysql -u "+dbuser+" --password='"+dbpassword+"' "+projectid+" < "+path+"DB/REG/create.sql")
    os.system("mysql -u "+dbuser+" --password='"+dbpassword+"' "+projectid+" < "+path+"DB/REG/insert.sql")