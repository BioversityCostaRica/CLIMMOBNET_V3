from sqlalchemy import (
    Column,
    ForeignKey
    )

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TEXT, DATETIME, TINYINT
from sqlalchemy.ext.declarative import declarative_base

import datetime

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#Lookup Table Country Model
class Lkpcountry(Base):
    __tablename__ = 'country'
    cnty_cod = Column('cnty_cod', VARCHAR(length=3), primary_key=True, nullable=False)
    cnty_name = Column('cnty_name', VARCHAR(length=120))

    def __init__(self,cnty_cod,cnty_name):
        self.cnty_cod = cnty_cod
        self.cnty_name = cnty_name

#Lookup Table Sector Model
class Lkpsector(Base):
    __tablename__ = 'sector'
    sector_cod = Column('sector_cod', INTEGER(display_width=11), primary_key=True, nullable=False)
    sector_name = Column('sector_name', VARCHAR(length=120))

    def __init__(self,sector_cod,sector_name):
        self.sector_cod = sector_cod
        self.sector_name = sector_name

#Table User Model
class User(Base):
    __tablename__ = 'user'
    user_name= Column('user_name', VARCHAR(length=80), primary_key=True, nullable=False)
    user_fullname= Column('user_fullname', VARCHAR(length=120))
    user_password= Column('user_password', VARCHAR(length=80))
    user_organization = Column('user_organization', VARCHAR(length=120))
    user_email = Column('user_email', VARCHAR(length=120))
    user_apikey = Column('user_apikey', VARCHAR(length=45))
    user_about = Column('user_about',TEXT)
    user_cnty = Column('user_cnty', VARCHAR(length=3), ForeignKey('country.cnty_cod'), nullable=False)
    user_sector = Column('user_sector', INTEGER(display_width=11), ForeignKey('sector.sector_cod'), nullable=False)
    user_active = Column('user_active', TINYINT(display_width=4))


    def __init__(self,user_name,user_fullname,user_password,user_organization,user_email,user_apikey,user_cnty,user_sector,user_about):
        self.user_name = user_name
        self.user_fullname = user_fullname
        self.user_password = user_password
        self.user_organization = user_organization
        self.user_email = user_email
        self.user_apikey = user_apikey
        self.user_cnty = user_cnty
        self.user_sector = user_sector
        self.user_about = user_about
        self.user_active = 1



#Table ActivityLog Model
class Activitylog(Base):
    __tablename__ = 'activitylog'
    log_id = Column('log_id', INTEGER(display_width=9), primary_key=True, nullable=False)
    log_user = Column('log_user', VARCHAR(length=80), ForeignKey('user.user_name'))
    log_datetime = Column('log_datetime', DATETIME)
    log_type = Column('log_type', VARCHAR(length=3))
    log_message = Column('log_message',TEXT)

    def __init__(self,log_user,log_type,log_message):
        self.log_user = log_user
        self.log_datetime = datetime.datetime.now()
        self.log_type = log_type
        self.log_message = log_message


class Apilog(Base):
    __tablename__ = 'apilog'

    #column definitions
    log_datetime = Column('log_datetime', DATETIME())
    log_id = Column('log_id', INTEGER(display_width=9), primary_key=True, nullable=False)
    log_ip = Column('log_ip', VARCHAR(length=45))
    log_user = Column('log_user', VARCHAR(length=80), ForeignKey('user.user_name'), nullable=False)
    log_uuid = Column('log_uuid', VARCHAR(length=80))
    log_xmlsource = Column('log_xmlsource', TEXT())

    def __init__(self,log_ip,log_user,log_uuid,log_xmlsource):
        self.log_datetime = datetime.datetime.now()
        self.log_ip = log_ip
        self.log_user = log_user
        self.log_uuid = log_uuid
        self.log_xmlsource = log_xmlsource
