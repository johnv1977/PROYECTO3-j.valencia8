from flask_login import current_user, login_required
from db import db
from models.sale import Sale
from flask import Blueprint, flash, redirect, render_template, url_for


sales_blueprint = Blueprint('sales', __name__, url_prefix='/sales')


@sales_blueprint.route("/", methods=['GET'])
def index():
    _sales = db.session.execute(db.select(Sale)).scalars().all()
    return render_template("sales/index.html", sales=_sales)


@sales_blueprint.route("sale_product_by_id/<int:id>", methods=['GET'])
@login_required
def sale_product_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _response = Sale.register_sale(id)
            flash(_response, 'success')
            return redirect(url_for('app.index'))

        except Exception as error:
            flash(str(error), 'error')
            return redirect(url_for('app.index'))
    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))


@sales_blueprint.route("view_profit_report", methods=['GET'])
@login_required
def view_profit_report():
    user = current_user
    if user.is_admin:
        _response = Sale.register_sale(id)
        flash(_response, 'success')
        return redirect(url_for('sales/report'))

    else:
        flash('No tienes acceso a esta ruta', 'error')
        return render_template(url_for('app.index'))
