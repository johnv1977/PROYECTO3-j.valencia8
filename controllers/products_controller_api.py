from flask_login import current_user, login_required
from db import db
from models.product import Product
from flask import Blueprint, jsonify


api_products_blueprint = Blueprint('api_products', __name__, url_prefix='/api/products')


@api_products_blueprint.route("/", methods=['GET'])
@login_required
def index():
    user = current_user
    if user.is_admin or user.is_employed or user is not None:
        try:
            _products = db.session.execute(db.select(Product)).scalars().all()
            return jsonify([product.to_dict() for product in _products]), 200
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 401
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401


@api_products_blueprint.route("get_by_id/<int:id>", methods=['GET'])
@login_required
def get_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _product = Product.query.get(id)

            if _product is None:
                raise ValueError('Producto no encontrado')

            return jsonify(_product.to_dict()), 200
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401


@api_products_blueprint.route("/get_by_name/<string:name>", methods=['GET'])
@login_required
def get_by_name(name: str):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _product = Product.query.filter_by(name=name).first()

            if _product is None:
                raise ValueError('Producto no encontrado')

            return jsonify(_product.to_dict()), 200
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401


@api_products_blueprint.route("/calories_by_id/<int:id>", methods=['GET'])
@login_required
def calories_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed or user is not None:
        try:
            _product = Product.query.get(id)
            _calories = _product.calculate_calories()
            return jsonify({
                'id': id,
                'calories': _calories
            }), 200
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401


@api_products_blueprint.route('/calculate_profit_by_id/<int:id>', methods=['GET'])
@login_required
def calculate_profit_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _product = Product.query.get(id)
            if not _product:
                raise ValueError('Producto no encontrado')

            profit = _product.calculate_profit()

            return jsonify({
                'id': id,
                'profit': profit
            })
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401


@api_products_blueprint.route('/calculate_cost_by_id/<int:id>', methods=['GET'])
@login_required
def calculate_cost_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _product = Product.query.get(id)
            _cost = _product.calculate_cost()
            return jsonify({
                'id': id,
                'cost': _cost
            }), 201
        except ValueError as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            }), 404
        except Exception as error:
            # estraer el mensaje de error
            return jsonify({
                'error': str(error)
            })
    else:
        return jsonify({
            'message': 'No tienes acceso a esta ruta'
        }), 401
