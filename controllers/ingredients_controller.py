# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/
from flask_login import current_user, login_required
from db import db
from flask import Blueprint, flash, redirect, render_template, url_for
from models.ingredient import Ingredient


ingredients_blueprint = Blueprint('ingredients', __name__, url_prefix='/ingredients')


@ingredients_blueprint.route("/")
@login_required
def index():
    user = current_user
    if user.is_admin or user.is_employed:
        _ingredients = db.session.execute(db.select(Ingredient)).scalars().all()
        return render_template("ingredients/index.html", ingredients=_ingredients)
    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))


@ingredients_blueprint.route("/<int:id>")
@login_required
def show(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        _ingredient = db.one_or_404(
            db.select(Ingredient).filter_by(id=id),
            description='Ingrediente no encontrado'
        )
        return render_template("ingredients/show.html", ingredient=_ingredient)
    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))


@ingredients_blueprint.route("/abastecer/<int:id>")
@login_required
def supply(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = db.one_or_404(
                db.select(Ingredient).filter_by(id=id),
                description='Ingrediente no encontrado'
            )
            _ingredient.supply()

            db.session.add(_ingredient)
            db.session.commit()

            flash(f'Se abasteción el ingrediente {_ingredient.name}', 'success')
            _ingredients = db.session.execute(db.select(Ingredient)).scalars().all()
            return render_template("ingredients/index.html", ingredients=_ingredients)

        except Exception as error:
            flash(str(error), 'error')
            return redirect(url_for('ingredients.index'))
    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))
