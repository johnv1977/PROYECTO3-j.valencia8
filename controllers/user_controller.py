from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from models.user import User


user_blueprint = Blueprint('users', __name__, url_prefix='/users')


@user_blueprint.route('/login', methods=["GET", "POST"])
def login():
    next_page = request.form.get('_next_page')

    if request.method == 'GET':
        return render_template("users/login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        _user = User.query.filter_by(username=username).first()

        if _user is None:
            flash('El usuario no existe.', 'error')
            return redirect(url_for('users.login'))

        elif not _user.check_password(password):
            flash('La contraseña es incorrecta.', 'error')
            return redirect(url_for('users.login'))

        else:
            login_user(_user)
            flash('Has iniciado sesión.', 'success')
            return redirect(next_page or url_for('app.index'))


@user_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('app.index'))
