import os

from db import db
from flask_login import LoginManager
from models.user import User


def app_config_login(app):
    global login_manager
    app.config['SECRET_KEY'] = os.urandom(24)

    login_manager = LoginManager(app)
    login_manager.login_view = 'users.login'

    @login_manager.user_loader
    def load_user(user_id):
        _users = db.session.query(User).all()
        for user in _users:
            if user.id == int(user_id):
                return user
        return None
