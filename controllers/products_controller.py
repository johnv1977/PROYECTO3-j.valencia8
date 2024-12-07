from flask_login import current_user, login_required
from db import db
from models.product import Product
from flask import Blueprint, flash, render_template, url_for


products_blueprint = Blueprint('products', __name__, url_prefix='/products')


@products_blueprint.route("/")
def index():
    # Esta ruta es pública, todos pueden ver los productos.
    _products = db.session.execute(db.select(Product)).scalars().all()
    return render_template("products/index.html", products=_products)


@products_blueprint.route("/<int:id>")
@login_required
def show(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        _product = Product.query.get(id)
        return render_template("products/show.html", product=_product)
    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))
