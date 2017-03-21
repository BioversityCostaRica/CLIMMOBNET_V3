# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, text, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
metadata = Base.metadata

import datetime

class Activitylog(Base):
    __tablename__ = 'activitylog'

    log_id = Column(Integer, primary_key=True)
    log_user = Column(ForeignKey(u'user.user_name'), nullable=False, index=True)
    log_datetime = Column(DateTime)
    log_type = Column(String(3))
    log_message = Column(Text)

    user = relationship(u'User')

    def __init__(self,log_user,log_type,log_message):
        self.log_user = log_user
        self.log_datetime = datetime.datetime.now()
        self.log_type = log_type
        self.log_message = log_message


class Apilog(Base):
    __tablename__ = 'apilog'

    log_id = Column(Integer, primary_key=True)
    log_datetime = Column(DateTime)
    log_ip = Column(String(45))
    log_user = Column(ForeignKey(u'user.user_name'), nullable=False, index=True)
    log_uuid = Column(String(80))

    user = relationship(u'User')

    def __init__(self,log_ip,log_user,log_uuid):
        self.log_datetime = datetime.datetime.now()
        self.log_ip = log_ip
        self.log_user = log_user
        self.log_uuid = log_uuid


class Assessment(Base):
    __tablename__ = 'assessment'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['section_user', 'section_project', 'section_id'], [u'asssection.user_name', u'asssection.project_cod', u'asssection.section_id'], ondelete=u'CASCADE'),
        Index('fk_assessment_asssection1_idx', 'section_user', 'section_project', 'section_id')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    section_user = Column(String(80), nullable=False)
    section_project = Column(String(80), nullable=False)
    section_id = Column(Integer, nullable=False)
    question_order =Column(Integer)

    project = relationship(u'Project')
    question = relationship(u'Question')
    asssection = relationship(u'Asssection')

    def __init__(self,user_name,project_cod,question_id,section_user,section_project,section_id,question_order):
        self.user_name = user_name
        self.project_cod = project_cod
        self.question_id = question_id
        self.section_user = section_user
        self.section_project = section_project
        self.section_id = section_id
        self.question_order = question_order


class Asssection(Base):
    __tablename__ = 'asssection'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    section_id = Column(Integer, primary_key=True, nullable=False)
    section_name = Column(String(120))
    section_content = Column(Text)
    section_order = Column(Integer)
    section_color = Column(String(20))

    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,section_id,section_name,section_content,section_order,section_color):
        self.user_name = user_name
        self.project_cod = project_cod
        self.section_id = section_id
        self.section_name = section_name
        self.section_content = section_content
        self.section_order = section_order
        self.section_color = section_color


class Country(Base):
    __tablename__ = 'country'

    cnty_cod = Column(String(3), primary_key=True)
    cnty_name = Column(String(120))

    def __init__(self,cnty_cod,cnty_name):
        self.cnty_cod = cnty_cod
        self.cnty_name = cnty_name


class Enumerator(Base):
    __tablename__ = 'enumerator'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    enum_id = Column(String(80), primary_key=True, nullable=False)
    enum_name = Column(String(120))
    enum_password = Column(String(80))
    enum_active = Column(Integer)

    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,enum_id,enum_name,enum_password,enum_active):
        self.user_name = user_name
        self.project_cod = project_cod
        self.enum_id = enum_id
        self.enum_name = enum_name
        self.enum_password = enum_password
        self.enum_active = enum_active


class I18n(Base):
    __tablename__ = 'i18n'

    lang_code = Column(String(5), primary_key=True)
    lang_name = Column(String(120))

    def __init__(self,lang_code,lang_name):
        self.lang_code = lang_code
        self.lang_name = lang_name


class Package(Base):
    __tablename__ = 'package'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    package_id = Column(Integer, primary_key=True, nullable=False)

    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,package_id):
        self.user_name = user_name
        self.project_cod = project_cod
        self.package_id = package_id


class Pkgcomb(Base):
    __tablename__ = 'pkgcomb'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod', 'package_id'], [u'package.user_name', u'package.project_cod', u'package.package_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['comb_user', 'comb_project', 'comb_code'], [u'prjcombination.user_name', u'prjcombination.project_cod', u'prjcombination.comb_code'], ondelete=u'CASCADE'),
        Index('fk_pkgcomb_prjcombination1_idx', 'comb_user', 'comb_project', 'comb_code')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    package_id = Column(Integer, primary_key=True, nullable=False)
    comb_user = Column(String(80), primary_key=True, nullable=False)
    comb_project = Column(String(80), primary_key=True, nullable=False)
    comb_code = Column(Integer, primary_key=True, nullable=False)
    pkgcomb_code = Column(String(45))
    pkgcomb_image = Column(LargeBinary)

    package = relationship(u'Package')
    prjcombination = relationship(u'Prjcombination')

    def __init__(self,user_name,project_cod,package_id,comb_user,comb_project,comb_code,pkgcomb_code,pkgcomb_image):
        self.user_name = user_name
        self.project_cod = project_cod
        self.package_id = package_id
        self.comb_user = comb_user
        self.comb_project = comb_project
        self.comb_code = comb_code
        self.pkgcomb_code = pkgcomb_code
        self.pkgcomb_image = pkgcomb_image


class Prjalia(Base):
    __tablename__ = 'prjalias'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod', 'tech_id'], [u'prjtech.user_name', u'prjtech.project_cod', u'prjtech.tech_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['tech_used', 'alias_used'], [u'techalias.tech_id', u'techalias.alias_id'], ondelete=u'CASCADE'),
        Index('fk_prjalias_techalias1_idx', 'tech_used', 'alias_used'),
        Index('fk_prjalias_prjtech1_idx', 'user_name', 'project_cod', 'tech_id')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    tech_id = Column(Integer, primary_key=True, nullable=False)
    alias_id = Column(Integer, primary_key=True, nullable=False)
    alias_name = Column(String(120))
    tech_used = Column(Integer)
    alias_used = Column(Integer)

    prjtech = relationship(u'Prjtech')
    techalia = relationship(u'Techalia')
    prjcombination = relationship(u'Prjcombination', secondary='prjcombdet')

    def __init__(self,user_name,project_cod,tech_id,alias_id,alias_name,tech_used,alias_used):
        self.user_name = user_name
        self.project_cod = project_cod
        self.tech_id = tech_id
        self.alias_id = alias_id
        self.alias_name = alias_name
        self.tech_used = tech_used
        self.alias_used = alias_used


class Prjcnty(Base):
    __tablename__ = 'prjcnty'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    cnty_cod = Column(ForeignKey(u'country.cnty_cod', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    cnty_contact = Column(String(120))

    country = relationship(u'Country')
    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,cnty_cod,cnty_contact):
        self.user_name = user_name
        self.project_cod = project_cod
        self.cnty_cod = cnty_cod
        self.cnty_contact = cnty_contact


class Prjcombdet(Base):
    __tablename__ = 'prjcombdet'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod', 'tech_id', 'alias_id'],
                             [u'prjalias.user_name', u'prjalias.project_cod', u'prjalias.tech_id',
                              u'prjalias.alias_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['prjcomb_user', 'prjcomb_project', 'comb_code'],
                             [u'prjcombination.user_name', u'prjcombination.project_cod', u'prjcombination.comb_code'],
                             ondelete=u'CASCADE'),
        Index('fk_prjcombdet_prjalias1_idx', 'user_name', 'project_cod', 'tech_id', 'alias_id')
    )

    prjcomb_user = Column('prjcomb_user', String(80), primary_key=True, nullable=False)
    prjcomb_project = Column('prjcomb_project', String(80), primary_key=True, nullable=False)
    comb_code = Column('comb_code', Integer, primary_key=True, nullable=False)
    user_name = Column('user_name', String(80), primary_key=True, nullable=False)
    project_cod = Column('project_cod', String(80), primary_key=True, nullable=False)
    tech_id = Column('tech_id', Integer, primary_key=True, nullable=False)
    alias_id = Column('alias_id', Integer, primary_key=True, nullable=False)

    def __init__(self,prjcomb_user,prjcomb_project,comb_code,user_name,project_cod,tech_id,alias_id):
        self.prjcomb_user = prjcomb_user
        self.prjcomb_project = prjcomb_project
        self.comb_code = comb_code
        self.user_name = user_name
        self.project_cod = project_cod
        self.tech_id = tech_id
        self.alias_id = alias_id


class Prjcombination(Base):
    __tablename__ = 'prjcombination'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    comb_code = Column(Integer, primary_key=True, nullable=False)
    comb_usable = Column(Integer)

    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,comb_code,comb_usable):
        self.user_name = user_name
        self.project_cod = project_cod
        self.comb_code = comb_code
        self.comb_usable = comb_usable


class Prjlang(Base):
    __tablename__ = 'prjlang'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    lang_code = Column(ForeignKey(u'i18n.lang_code', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    lang_default = Column(Integer)

    i18n = relationship(u'I18n')
    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,lang_code,lang_default):
        self.user_name = user_name
        self.project_cod = project_cod
        self.lang_code = lang_code
        self.lang_default = lang_default


class Prjtech(Base):
    __tablename__ = 'prjtech'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    tech_id = Column(ForeignKey(u'technology.tech_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)


    country = relationship(u'Technology')
    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,tech_id):
        self.user_name = user_name
        self.project_cod = project_cod
        self.tech_id = tech_id


class Project(Base):
    __tablename__ = 'project'

    user_name = Column(ForeignKey(u'user.user_name'), primary_key=True, nullable=False, index=True)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    project_name = Column(String(120))
    project_abstract = Column(Text)
    project_tags = Column(Text)
    project_pi = Column(String(120))
    project_piemail = Column(String(120))
    project_active = Column(Integer)
    project_public = Column(Integer)
    project_numobs = Column(Integer)
    project_numcom = Column(Integer)
    project_lat = Column(DECIMAL)
    project_lon = Column(DECIMAL)
    project_creationdate = Column(DateTime)

    project_active = Column(Integer)
    project_public = Column(Integer)
    project_numobs = Column(Integer)

    user = relationship(u'User')
    techs = relationship(u'Technology', secondary='prjtech')



    def __init__(self,user_name,project_cod,project_name,project_abstract,project_tags,project_pi,project_piemail,project_active,project_public,project_numobs,project_numcom,project_lat,project_lon,project_creationdate):
        self.user_name = user_name
        self.project_cod = project_cod
        self.project_name = project_name
        self.project_abstract = project_abstract
        self.project_tags = project_tags
        self.project_pi = project_pi
        self.project_piemail = project_piemail
        self.project_active = project_active
        self.project_public = project_public
        self.project_numobs = project_numobs
        self.project_numcom = project_numcom
        self.project_lat = project_lat
        self.project_lon = project_lon
        self.project_creationdate = project_creationdate


class Qstoption(Base):
    __tablename__ = 'qstoption'

    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False)
    value_code = Column(Integer, primary_key=True, nullable=False)
    value_desc = Column(String(120))

    question = relationship(u'Question')

    def __init__(self,question_id,value_code,value_desc):
        self.question_id = question_id
        self.value_code = value_code
        self.value_desc = value_desc


class Qstprjopt(Base):
    __tablename__ = 'qstprjopt'
    __table_args__ = (
        ForeignKeyConstraint(['project_user', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['parent_user', 'parent_project', 'parent_question', 'parent_value'], [u'qstprjopt.project_user', u'qstprjopt.project_cod', u'qstprjopt.question_id', u'qstprjopt.value_code'], ondelete=u'CASCADE'),
        Index('fk_qstprjopt_qstprjopt1_idx', 'parent_user', 'parent_project', 'parent_question', 'parent_value')
    )

    project_user = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    value_code = Column(Integer, primary_key=True, nullable=False)
    value_desc = Column(String(120))
    parent_user = Column(String(80))
    parent_project = Column(String(80))
    parent_question = Column(Integer)
    parent_value = Column(Integer)

    project = relationship(u'Project')
    parent = relationship(u'Qstprjopt', remote_side=[project_user, project_cod, question_id, value_code])
    question = relationship(u'Question')

    def __init__(self,project_user,project_cod,question_id,value_code,value_desc,parent_user,parent_project,parent_question,parent_value):
        self.project_user = project_user
        self.project_cod = project_cod
        self.question_id = question_id
        self.value_code = value_code
        self.value_desc = value_desc
        self.parent_user = parent_user
        self.parent_project = parent_project
        self.parent_question = parent_question
        self.parent_value = parent_value


class Question(Base):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True)
    question_desc = Column(String(120))
    question_notes = Column(Text)
    question_unit = Column(String(120))
    question_dtype = Column(Integer)
    question_oth = Column(Integer)
    question_cmp = Column(String(120))
    question_reqinreg = Column(Integer, server_default=text("'0'"))
    question_reqinasses = Column(Integer, server_default=text("'0'"))
    question_optperprj = Column(Integer, server_default=text("'0'"))

    question_posstm=Column(String(120))
    question_negstm=Column(String (120))

    parent_question = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), index=True)
    user_name = Column(ForeignKey(u'user.user_name'), index=True)
    question_posstm = Column(String(120))
    question_negstm = Column(String(120))
    question_twoitems = Column(String(120))
    question_moreitems = Column(String(120))
    question_requiredvalue = Column(Integer)

    parent = relationship(u'Question', remote_side=[question_id])
    user = relationship(u'User')

    def __init__(self,question_desc,question_notes,question_unit,question_dtype,question_oth,question_cmp,question_reqinreg,question_reqinasses,question_optperprj,parent_question,user_name,question_posstm,question_negstm,question_twoitems,question_moreitems,question_requiredvalue):

        self.question_desc = question_desc
        self.question_notes = question_notes
        self.question_unit = question_unit
        self.question_dtype = question_dtype
        self.question_oth = question_oth
        self.question_cmp = question_cmp
        self.question_reqinreg = question_reqinreg
        self.question_reqinasses = question_reqinasses
        self.question_optperprj = question_optperprj
        self.parent_question = parent_question
        self.user_name = user_name
        self.question_posstm = question_posstm
        self.question_negstm = question_negstm
        self.question_twoitems = question_twoitems
        self.question_moreitems = question_moreitems
        self.question_requiredvalue = question_requiredvalue


class Registry(Base):
    __tablename__ = 'registry'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['section_user', 'section_project', 'section_id'], [u'regsection.user_name', u'regsection.project_cod', u'regsection.section_id'], ondelete=u'CASCADE'),
        Index('fk_registry_regsection1_idx', 'section_user', 'section_project', 'section_id')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    section_user = Column(String(80))
    section_project = Column(String(80))
    section_id = Column(Integer)
    question_order =Column(Integer)

    project = relationship(u'Project')
    question = relationship(u'Question')
    regsection = relationship(u'Regsection')

    def __init__(self,user_name,project_cod,question_id,section_user,section_project,section_id, question_order):
        self.user_name = user_name
        self.project_cod = project_cod
        self.question_id = question_id
        self.section_user = section_user
        self.section_project = section_project
        self.section_id = section_id
        self.question_order = question_order


class Regsection(Base):
    __tablename__ = 'regsection'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    section_id = Column(Integer, primary_key=True, nullable=False)
    section_name = Column(String(45))
    section_content = Column(Text)
    section_order = Column(Integer)
    section_color =Column(String(20))

    project = relationship(u'Project')

    def __init__(self,user_name,project_cod,section_id,section_name,section_content,section_order,section_color):
        self.user_name = user_name
        self.project_cod = project_cod
        self.section_id = section_id
        self.section_name = section_name
        self.section_content = section_content
        self.section_order = section_order
        self.section_color = section_color


class Sector(Base):
    __tablename__ = 'sector'

    sector_cod = Column(Integer, primary_key=True)
    sector_name = Column(String(120))

    def __init__(self,sector_cod,sector_name):
        self.sector_cod = sector_cod
        self.sector_name = sector_name


class Submission(Base):
    __tablename__ = 'submission'

    submission_uuid = Column(String(80), primary_key=True)
    submission_date = Column(DateTime)
    submission_type = Column(Integer)

    def __init__(self,submission_uuid,submission_date,submission_type):
        self.submission_uuid = submission_uuid
        self.submission_date = submission_date
        self.submission_type = submission_type


class Techalia(Base):
    __tablename__ = 'techalias'

    tech_id = Column(ForeignKey(u'technology.tech_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    alias_id = Column(Integer, primary_key=True, nullable=False)
    alias_name = Column(String(120))

    tech = relationship(u'Technology')

    def __init__(self,tech_id,alias_id,alias_name):
        self.tech_id = tech_id
        self.alias_id = alias_id
        self.alias_name = alias_name


class Technology(Base):
    __tablename__ = 'technology'

    tech_id = Column(Integer, primary_key=True)
    tech_name = Column(String(45))
    user_name = Column(ForeignKey(u'user.user_name', ondelete=u'CASCADE'), index=True)

    user = relationship(u'User')

    def __init__(self,tech_name,user_name):
        self.tech_name = tech_name
        self.user_name = user_name


class User(Base):
    __tablename__ = 'user'

    user_name = Column(String(80), primary_key=True)
    user_fullname = Column(String(120))
    user_password = Column(String(80))
    user_organization = Column(String(120))
    user_email = Column(String(120))
    user_apikey = Column(String(45))
    user_about = Column(Text)
    user_cnty = Column(ForeignKey(u'country.cnty_cod'), nullable=False, index=True)
    user_sector = Column(ForeignKey(u'sector.sector_cod'), nullable=False, index=True)
    user_active = Column(Integer, server_default=text("'1'"))

    country = relationship(u'Country')
    sector = relationship(u'Sector')

    def __init__(self,user_name,user_fullname,user_password,user_organization,user_email,user_apikey,user_about,user_cnty,user_sector):
        self.user_name = user_name
        self.user_fullname = user_fullname
        self.user_password = user_password
        self.user_organization = user_organization
        self.user_email = user_email
        self.user_apikey = user_apikey
        self.user_about = user_about
        self.user_cnty = user_cnty
        self.user_sector = user_sector
        self.user_active = 1
