# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask, render_template
from flask.ext.admin import Admin
from dragon_lite.settings import ProdConfig
from dragon_lite.assets import assets
from dragon_lite.extensions import (
    bcrypt,
    cache,
    db,
    login_manager,
    migrate,
    debug_toolbar,
)
from dragon_lite import public, user, user_group
from dragon_lite.admin.views import AdminView
from dragon_lite.user_group.models import UserGroup
from dragon_lite.user.models import User


def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_admin_window(app)
    return app


def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(user_group.views.blueprint)
    return None


def register_admin_window(app):
    admin = Admin(name='DragonLite Admin')
    admin.init_app(app)
    admin.add_view(AdminView
                   (UserGroup, db.session, columns=('name', 'users')))
    admin.add_view(AdminView(User, db.session, endpoint='all'))
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
