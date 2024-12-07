from enums.e_ingredient_type import Ingredient_Type
from models.ingredient import Ingredient


class Complement(Ingredient):
    '''
    Representa un complemento.

    Attributes:
        id (int): El id del complemento.
        name (str): El nombre del complemento.
        price (int): El precio del complemento.
        calories (int): El número de calorías del complemento.
        is_vegetarian (bool): Si el complemento es vegetariano o no.
        units (float): La cantidad de unidades del complemento.

    Methods:
        reset_units() -> None: Establece en 0 la cantidad de unidades del complemento.
        supply() -> None: Abastecer el ingrediente.
    '''

    __mapper_args__ = {
        'polymorphic_identity': Ingredient_Type.COMPLEMENT
    }

    def is_available(self) -> bool:
        return self.units >= 1

    def register_sale(self) -> None:
        self.units = round(self.units - 1, 2)

    def reset_units(self) -> None:
        '''
        Establece en 0 la cantidad de unidades del complemento.
        Returns:
            None
        '''
        self.units = 0.0

    def supply(self) -> None:
        return self.add_units(10.0)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'calories': self.calories,
            'is_vegetarian': self.is_vegetarian,
            'units': self.units,
            'extra_data': self.extra_data or {}
        }
