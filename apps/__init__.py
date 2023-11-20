from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from importlib import import_module
from flask_minify import Minify
import os
from apps.models.base_model import BaseModel

login_manager = LoginManager()
db = SQLAlchemy(model_class=BaseModel)


def register_extensions(app):
    db.init_app(app)
    app.app_context().push()
    login_manager.login_view = "auth_bp.login"
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ("auth", "home", "customers"):
        module = False
        files = os.listdir("apps/{}".format(module_name))
        for f in files:
            if f.startswith("routes"):
                module = import_module("apps.{}.{}".format(module_name, f.strip(".py")))
        if module:
            app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    Minify(app=app, html=False, js=True, cssless=True)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    with app.app_context():
        from apps.models.db_models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(Users).get(int(user_id))

    return app
