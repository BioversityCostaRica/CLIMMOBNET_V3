#Authorization framework
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
# from auth import groupfinder
# from auth import Root
import os

#Configurator and SQLAlchemy
from pyramid.config import Configurator
from sqlalchemy import create_engine

from .models import (
    DBSession,
    Base
    )

#Jinja2 Extensions
from jinja_extensions import jinjaEnv
from jinja_extensions import setLoader
from jinja_extensions import loadHelpers

#from dbfunctions import loadUsers

from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('b@HdX5Y6nF')

def main(global_config, **settings):

    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth.secret'],
    )

    authz_policy = ACLAuthorizationPolicy()

    #Configure SQLAlchemy
    engine = create_engine("mysql://" + settings['mysql.user'] + ":" + settings['mysql.password'] + "@" + settings['mysql.host'] + "/" + settings['mysql.schema'],
                           pool_size=20, max_overflow=0, pool_recycle=3600)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine


    #loadUsers()

    #Configure the application
    config = Configurator(settings=settings,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          )
    config.set_session_factory(my_session_factory)
    #Add jinja2 and FanStatic
    config.include('pyramid_jinja2')
    config.include('pyramid_fanstatic')
    #Set Jinja2 Template render and static directory for images, etc
    config.add_jinja2_renderer('.html')
    config.add_static_view('static', 'static', cache_max_age=3600)

    #Set Views
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('policy', '/policy')
    config.add_route('register', '/register')
    config.add_route('logout', '/logout')

    #User routes
    config.add_route('profile', '/user')
    config.add_route('userinfo', '/user/info/{userid}')
    config.add_route('editprofile', '/user/edit')
    config.add_route('useractivity', '/user/activity')


    templatesPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

    #Set Jinja2 Template path
    config.add_jinja2_search_path(templatesPath)
    config.scan()
    #Configure Jinja2 Environment
    jinjaEnv = config.get_jinja2_environment()
    setLoader(templatesPath)
    loadHelpers()
    return config.make_wsgi_app()