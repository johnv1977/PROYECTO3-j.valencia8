from models.product import Product
from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException


app_blueprint = Blueprint('app', __name__)


@app_blueprint.route("/")
def index():
    _products = Product.query.all()
    return render_template("index.html", products=_products)


def define_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('errors/401.html', title='401', error_message='No puedes acceder a esta página'), 401

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/errors.html', title='404', error_message='La página que buscas no existe'), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('errors/errors.html', title='405', error_message='El método que intentas utilizar no está permitido'), 405

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/errors.html', title='500', error_message='Ha ocurrido un error interno del servidor'), 500

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        return render_template('errors/errors.html', title='500', error_message=f'Ha ocurrido un error interno del servidor: {e}'), 500
