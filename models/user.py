from db import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_employed = db.Column(db.Boolean, nullable=False, default=False)

    def check_password(self, password):
        return self.password == password
