import uuid

import transaction

from models import DBSession,User,Activitylog,Apilog
from encdecdata import encodeData,decodeData


def userExists(user):
    res = False
    mySession = DBSession()
    result = mySession.query(User).filter_by(user_name = user).first()
    if not result is None:
        res = True
    mySession.close()
    return  res

def emailExists(email):
    res = False
    mySession = DBSession()
    result = mySession.query(User).filter_by(user_email = email).first()
    if not result is None:
        res = True
    mySession.close()
    return  res

def addUser(userData):
    mySession = DBSession()
    newUser = User(userData["user_name"],userData["user_fullname"],encodeData(userData["user_password"]),userData["user_organization"],userData["user_email"],
                   str(uuid.uuid4()),"",userData["user_cnty"],userData["user_sector"])
    try:
        transaction.begin()
        mySession.add(newUser) #Add the ne user to MySQL
        transaction.commit()

        mySession.close()
        return True,""
    except Exception, e:
        transaction.abort()
        mySession.close()
        return False,str(e)


def getUserPassword(user):
    res = ""
    mySession = DBSession()
    result = mySession.query(User).filter_by(user_name = user).first()
    if not result is None:
        res = decodeData(result.user_password)
    mySession.close()
    return  res

def changeUserPassword(user,password):
    mySession = DBSession()
    try:
        transaction.begin()
        mySession.query(User).filter_by(user_name = user).update({"user_password": encodeData(password)})
        transaction.commit()
        mySession.close()
        return True
    except:
        transaction.abort()
        mySession.close()
        return False

def otherUserHasEmail(user,email):
    res = False
    mySession = DBSession()
    result = mySession.query(User).filter(User.user_name != user).filter_by(user_email = email).first()
    if not result is None:
        res = True
    mySession.close()
    return  res

def updateProfile(user,data):
    mySession = DBSession()
    try:
        transaction.begin()
        mySession.query(User).filter_by(user_name = user).update({"user_fullname": data["user_fullname"],"user_organization": data["user_organization"],
                                                                  "user_email": data["user_email"],"user_cnty": data["user_cnty"],"user_sector": data["user_sector"],
                                                                  "user_about": data["user_about"]})
        transaction.commit()
        mySession.close()
        return True
    except Exception, e:
        print str(e)
        transaction.abort()
        mySession.close()
        return False

def addToLog(log_user,log_type,log_message):
    mySession = DBSession()
    newLog = Activitylog(log_user,log_type,log_message)
    try:
        transaction.begin()
        mySession.add(newLog) #Add the new log to MySQL
        transaction.commit()
        mySession.close()
    except:
        transaction.abort()
        mySession.close()

def getUserLog(user,limit = True):
    sql = "SELECT DATE_FORMAT(DATE(log_datetime), '%%W %%D %%M %%Y') as log_date,TIME(log_datetime) as log_time,log_type,log_message,log_datetime as date1,log_datetime as date2 FROM activitylog WHERE log_user = '" + user + "' ORDER BY date1 DESC,date2 ASC,log_id desc"
    if limit:
        sql = sql + " LIMIT 20"
    mySession = DBSession()
    connection = mySession.connection()
    activities = connection.execute(sql)
    items = []
    count = 1
    for activity in activities:
        if count%2 == 0:
            alt = False
        else:
            alt= True
        count = count + 1
        if activity[2] == "PRF":
            color = "terques"
            icon = "fa-user"
        else:
            if activity[2] == "MOD":
                color = "purple"
                icon = "fa-gears"
            else:
                if activity[2] == "FED":
                    color = "blue"
                    icon = "fa-leaf"
                else:
                    if activity[2] == "API":
                        color = "green"
                        icon = "fa-bolt"
                    else:
                        color = "red"
                        icon = "fa-bullhorn"

        items.append({"date":activity[0],"time":activity[1],"type":activity[2],"message":activity[3],"alt":alt,"icon":icon,"color":color})
    connection.close()
    mySession.close()
    return items

def getUserWithKey(key):
    res = ""
    mySession = DBSession()
    result = mySession.query(User).filter_by(user_apikey = key).first()
    if not result is None:
        res = result.user_name
    mySession.close()
    return  res


def addAPILog(ipaddress,user,requestID,inputData):
    mySession = DBSession()
    newApilog = Apilog(ipaddress,user,requestID)
    try:
        transaction.begin()
        mySession.add(newApilog)
        transaction.commit()
        mySession.close()
        return True
    except:
        transaction.abort()
        mySession.close()
        return False

def getAPILog(requestID):
    res = ""
    mySession = DBSession()
    result = mySession.query(Apilog).filter_by(log_uuid = requestID).first()
    if not result is None:
        res = result.log_id
    mySession.close()
    return  res

#This removes the funny 0E-10
def fixData(data):
    for key,value in data.iteritems():
        if value == 0E-10:
            data[key] = 0
    return data


def getStats(currUser = None):
    data = {}
    mySession = DBSession()
    data["totUsers"] = mySession.query(User).count()
    if currUser == None:
        data["totFeeds"] = 0
        data["totModels"] = 0
    else:
        data["totFeeds"] = 0
        data["totModels"] = 0
    mySession.close()
    return data


def getUserInfo(userid):
    mySession = DBSession()

    sql = "SELECT user_fullname, user_organization, user_email, user_about,lkpcountry.cnty_name,lkpsector.sector_name FROM " \
          "user,lkpcountry,lkpsector WHERE user_cnty = lkpcountry.cnty_cod AND user_sector = lkpsector.sector_cod AND user_name = " + "'" + userid + "'"

    connection = mySession.connection()
    results = connection.execute(sql)

    userInfo = {}
    for result in results:
        userInfo["user_fullname"] = result[0];
        userInfo["user_organization"] = result[1];
        userInfo["user_email"] = result[2];
        userInfo["user_about"] = result[3];
        userInfo["cnty_name"] = result[4];
        userInfo["sector_name"] = result[5];
    connection.close()
    mySession.close()
    return userInfo


def getAPIInfo(logID):
    res = {}
    mySession = DBSession()
    result = mySession.query(Apilog).filter_by(log_id = logID).first()
    if not result is None:
        res["log_datetime"] = result.log_datetime
        res["log_ip"] = result.log_ip
    mySession.close()
    return  res



def fixValue(value):
    if value == 0E-10:
            return 0
    else:
        return value

#This removes .0 and . after a strip(0)
def fixString(value):
    if len(value) > 0:
        res = value
        if value[0] == ".":
            res = "0" + res
        if value[-1] == ".":
            res = res + "0"
        if res[-2:] == ".0":
            res = res[:-2]
        return res
    else:
        return "0"


