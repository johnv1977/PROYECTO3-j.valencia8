from flask_login import current_user, login_required
from models.sale import Sale
from flask import Blueprint, jsonify
from errors.product_not_available_error import ProductNotAvailableError


api_sales_blueprint = Blueprint('api_sales', __name__, url_prefix='/api/sales')


@api_sales_blueprint.route("sale_product_by_id/<int:id>", methods=['GET'])
@login_required
def sale_product_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _response = Sale.register_sale(id)
            return jsonify({
                'message': _response
            }), 200

        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404

        except ProductNotAvailableError as error:
            # extraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 409

        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 500
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401
