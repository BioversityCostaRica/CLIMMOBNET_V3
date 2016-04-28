# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, text
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


class Activitylog(Base):
    __tablename__ = 'activitylog'

    log_id = Column(Integer, primary_key=True)
    log_user = Column(ForeignKey(u'user.user_name'), nullable=False, index=True)
    log_datetime = Column(DateTime)
    log_type = Column(String(3))
    log_message = Column(Text)
    user = relationship(u'User')


class Apilog(Base):
    __tablename__ = 'apilog'

    log_id = Column(Integer, primary_key=True)
    log_datetime = Column(DateTime)
    log_ip = Column(String(45))
    log_user = Column(ForeignKey(u'user.user_name'), nullable=False, index=True)
    log_uuid = Column(String(80))

    user = relationship(u'User')


class Assessment(Base):
    __tablename__ = 'assessment'
    __table_args__ = (
        ForeignKeyConstraint(['section_user', 'section_project', 'section_id'], [u'asssection.user_name', u'asssection.project_cod', u'asssection.section_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
        Index('fk_assessment_asssection1_idx', 'section_user', 'section_project', 'section_id')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    section_user = Column(String(80), nullable=False)
    section_project = Column(String(80), nullable=False)
    section_id = Column(Integer, nullable=False)

    question = relationship(u'Question')
    asssection = relationship(u'Asssection')
    project = relationship(u'Project')


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

    project = relationship(u'Project')


class Country(Base):
    __tablename__ = 'country'

    cnty_cod = Column(String(3), primary_key=True)
    cnty_name = Column(String(120))


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


class I18n(Base):
    __tablename__ = 'i18n'

    lang_code = Column(String(5), primary_key=True)
    lang_name = Column(String(120))


class Package(Base):
    __tablename__ = 'package'
    __table_args__ = (
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    package_id = Column(Integer, primary_key=True, nullable=False)

    project = relationship(u'Project')


class Pkgcomb(Base):
    __tablename__ = 'pkgcomb'
    __table_args__ = (
        ForeignKeyConstraint(['comb_user', 'comb_project', 'comb_code'], [u'prjcombination.user_name', u'prjcombination.project_cod', u'prjcombination.comb_code'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['user_name', 'project_cod', 'package_id'], [u'package.user_name', u'package.project_cod', u'package.package_id'], ondelete=u'CASCADE'),
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

    prjcombination = relationship(u'Prjcombination')
    package = relationship(u'Package')


class Prjalia(Base):
    __tablename__ = 'prjalias'
    __table_args__ = (
        ForeignKeyConstraint(['tech_used', 'alias_used'], [u'techalias.tech_id', u'techalias.alias_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['user_name', 'project_cod', 'tech_id'], [u'prjtech.user_name', u'prjtech.project_cod', u'prjtech.tech_id'], ondelete=u'CASCADE'),
        Index('fk_prjalias_prjtech1_idx', 'user_name', 'project_cod', 'tech_id'),
        Index('fk_prjalias_techalias1_idx', 'tech_used', 'alias_used')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    tech_id = Column(Integer, primary_key=True, nullable=False)
    alias_id = Column(Integer, primary_key=True, nullable=False)
    alias_name = Column(String(120))
    tech_used = Column(Integer, nullable=False)
    alias_used = Column(Integer, nullable=False)

    techalia = relationship(u'Techalia')
    prjtech = relationship(u'Prjtech')


t_prjcombdet = Table(
    'prjcombdet', metadata,
    Column('prjcomb_user', String(80), primary_key=True, nullable=False),
    Column('prjcomb_project', String(80), primary_key=True, nullable=False),
    Column('comb_code', Integer, primary_key=True, nullable=False),
    Column('user_name', String(80), primary_key=True, nullable=False),
    Column('project_cod', String(80), primary_key=True, nullable=False),
    Column('tech_id', Integer, primary_key=True, nullable=False),
    Column('alias_id', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['prjcomb_user', 'prjcomb_project', 'comb_code'], [u'prjcombination.user_name', u'prjcombination.project_cod', u'prjcombination.comb_code'], ondelete=u'CASCADE'),
    ForeignKeyConstraint(['user_name', 'project_cod', 'tech_id', 'alias_id'], [u'prjalias.user_name', u'prjalias.project_cod', u'prjalias.tech_id', u'prjalias.alias_id'], ondelete=u'CASCADE'),
    Index('fk_prjcombdet_prjalias1_idx', 'user_name', 'project_cod', 'tech_id', 'alias_id')
)


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
    prjalias = relationship(u'Prjalia', secondary='prjcombdet')


t_prjtech = Table(
    'prjtech', metadata,
    Column('user_name', String(80), primary_key=True, nullable=False),
    Column('project_cod', String(80), primary_key=True, nullable=False),
    Column('tech_id', ForeignKey(u'technology.tech_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE')
)


class Project(Base):
    __tablename__ = 'project'

    user_name = Column(ForeignKey(u'user.user_name'), primary_key=True, nullable=False, index=True)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    project_name = Column(String(120))
    project_abstract = Column(Text)
    project_tags = Column(Text)
    project_pi = Column(String(120))
    project_piemail = Column(String(120))

    user = relationship(u'User')


class Qstoption(Base):
    __tablename__ = 'qstoption'

    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False)
    value_code = Column(Integer, primary_key=True, nullable=False)
    value_desc = Column(String(120))

    question = relationship(u'Question')


class Qstprjopt(Base):
    __tablename__ = 'qstprjopt'
    __table_args__ = (
        ForeignKeyConstraint(['parent_user', 'parent_project', 'parent_question', 'parent_value'], [u'qstprjopt.project_user', u'qstprjopt.project_cod', u'qstprjopt.question_id', u'qstprjopt.value_code'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['project_user', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
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

    parent = relationship(u'Qstprjopt', remote_side=[project_user, project_cod, question_id, value_code])
    project = relationship(u'Project')
    question = relationship(u'Question')


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
    parent_question = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), index=True)
    user_name = Column(ForeignKey(u'user.user_name'), index=True)

    parent = relationship(u'Question', remote_side=[question_id])
    user = relationship(u'User')


class Registry(Base):
    __tablename__ = 'registry'
    __table_args__ = (
        ForeignKeyConstraint(['section_user', 'section_project', 'section_id'], [u'regsection.user_name', u'regsection.project_cod', u'regsection.section_id'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['user_name', 'project_cod'], [u'project.user_name', u'project.project_cod'], ondelete=u'CASCADE'),
        Index('fk_registry_regsection1_idx', 'section_user', 'section_project', 'section_id')
    )

    user_name = Column(String(80), primary_key=True, nullable=False)
    project_cod = Column(String(80), primary_key=True, nullable=False)
    question_id = Column(ForeignKey(u'question.question_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    section_user = Column(String(80))
    section_project = Column(String(80))
    section_id = Column(Integer)

    question = relationship(u'Question')
    regsection = relationship(u'Regsection')
    project = relationship(u'Project')


class Registryresp(Base):
    __tablename__ = 'registryresp'
    __table_args__ = (
        ForeignKeyConstraint(['qstprjopt_user', 'qstprjopt_project', 'qstprjopt_question', 'qstprjopt_value'], [u'qstprjopt.project_user', u'qstprjopt.project_cod', u'qstprjopt.question_id', u'qstprjopt.value_code'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['resp_question', 'resp_value'], [u'qstoption.question_id', u'qstoption.value_code'], ondelete=u'CASCADE'),
        ForeignKeyConstraint(['user_name', 'project_cod', 'question_id'], [u'registry.user_name', u'registry.project_cod', u'registry.question_id'], ondelete=u'CASCADE'),
        Index('fk_registryresp_registry1_idx', 'user_name', 'project_cod', 'question_id'),
        Index('fk_response_qstoption1_idx', 'resp_question', 'resp_value'),
        Index('fk_registryresp_qstprjopt1_idx', 'qstprjopt_user', 'qstprjopt_project', 'qstprjopt_question', 'qstprjopt_value')
    )

    submission_uuid = Column(ForeignKey(u'submission.submission_uuid', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    resp_uuid = Column(String(80), primary_key=True, nullable=False)
    user_name = Column(String(80), nullable=False)
    project_cod = Column(String(80), nullable=False)
    question_id = Column(Integer, nullable=False)
    resp_intvalue = Column(Integer)
    resp_decvalue = Column(Numeric(11, 3))
    resp_datevalue = Column(DateTime)
    resp_txtvalue = Column(Text)
    resp_question = Column(Integer)
    resp_value = Column(Integer)
    qstprjopt_user = Column(String(80))
    qstprjopt_project = Column(String(80))
    qstprjopt_question = Column(Integer)
    qstprjopt_value = Column(Integer)

    qstprjopt = relationship(u'Qstprjopt')
    qstoption = relationship(u'Qstoption')
    submission = relationship(u'Submission')
    registry = relationship(u'Registry')


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

    project = relationship(u'Project')


class Sector(Base):
    __tablename__ = 'sector'

    sector_cod = Column(Integer, primary_key=True)
    sector_name = Column(String(120))


class Submission(Base):
    __tablename__ = 'submission'

    submission_uuid = Column(String(80), primary_key=True)
    submission_date = Column(DateTime)
    submission_type = Column(Integer)


class Techalia(Base):
    __tablename__ = 'techalias'

    tech_id = Column(ForeignKey(u'technology.tech_id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True)
    alias_id = Column(Integer, primary_key=True, nullable=False)
    alias_name = Column(String(120))

    tech = relationship(u'Technology')


class Technology(Base):
    __tablename__ = 'technology'

    tech_id = Column(Integer, primary_key=True)
    tech_name = Column(String(45))
    user_name = Column(ForeignKey(u'user.user_name', ondelete=u'CASCADE'), index=True)

    user = relationship(u'User')
    project = relationship(u'Project', secondary='prjtech')


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
