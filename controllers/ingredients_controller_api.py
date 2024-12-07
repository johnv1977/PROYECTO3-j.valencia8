from flask_login import current_user, login_required
from db import db
from enums.e_ingredient_type import Ingredient_Type
from errors.method_does_not_apply import MethodDoesNotApplyError
from models.ingredient import Ingredient
from flask import Blueprint, jsonify


api_ingredients_blueprint = Blueprint('api_ingredients', __name__, url_prefix='/api/ingredients')


@api_ingredients_blueprint.route("/", methods=['GET'])
@login_required
def index():
    user = current_user

    if user.is_admin or user.is_employed:
        try:
            _ingredients = db.session.execute(db.select(Ingredient)).scalars().all()
            return jsonify([ingredient.to_dict() for ingredient in _ingredients]), 200
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


@api_ingredients_blueprint.route("get_by_id/<int:id>", methods=['GET'])
@login_required
def get_by_id(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = Ingredient.query.get(id)

            if _ingredient is None:
                raise ValueError('Ingrediento no encontrado')

            return jsonify(_ingredient.to_dict()), 200
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


@api_ingredients_blueprint.route("/get_by_name/<string:name>", methods=['GET'])
@login_required
def get_by_name(name: str):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = Ingredient.query.filter_by(name=name).first()

            if _ingredient is None:
                raise ValueError('Ingrediento no encontrado')

            return jsonify(_ingredient.to_dict()), 200
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


@api_ingredients_blueprint.route("/is_healthy/<int:id>", methods=['GET'])
@login_required
def is_healthy(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = Ingredient.query.get(id)
            _is_healthy = _ingredient.is_healthy()
            return jsonify({
                'id': id,
                '_is_healthy': _is_healthy
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


@api_ingredients_blueprint.route('/supply/<int:id>', methods=['GET'])
@login_required
def supply(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = Ingredient.query.get(id)
            if not _ingredient:
                raise ValueError('Ingrediento no encontrado')

            _old_units = _ingredient.units
            _ingredient.supply()
            _ingredient.units

            db.session.add(_ingredient)
            db.session.commit()

            return jsonify({
                'id': id,
                'old_units': _old_units,
                'new_units': _ingredient.units
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


@api_ingredients_blueprint.route('/reset_units/<int:id>', methods=['GET'])
@login_required
def reset_units(id: int):
    user = current_user
    if user.is_admin or user.is_employed:
        try:
            _ingredient = Ingredient.query.get(id)

            if _ingredient.type != Ingredient_Type.COMPLEMENT:
                raise MethodDoesNotApplyError('¡Sólo se puede abastecer un ingrediente del tipo complemento!')

            _old_units = _ingredient.units
            _ingredient.reset_units()

            return jsonify({
                'id': id,
                'old_units': _old_units,
                'new_units': _ingredient.units
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
