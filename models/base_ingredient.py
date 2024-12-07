from enums.e_ingredient_type import Ingredient_Type
from models.ingredient import Ingredient


class Base_Ingredient(Ingredient):
    '''
    Representa una base.

    Attributes:
        id (int): El id de la base.
        name (str): El nombre de la base.
        price (int): El precio de la base.
        calories (int): El número de calorías de la base.
        is_vegetarian (bool): Si la base es vegetariana o no.
        units (float): La cantidad de unidades de la base.
        extra_data (dict): Datos adicionales de la base.

    Methods:
        get_console_options() -> Dict[str, List[str] | str]: Obtiene las opciones de la consola.
        is_available() -> bool: Comprueba si el elemento está disponible para vender.
        register_sale() -> None: Registra la venta de un elemento.
        supply() -> None: Abastecer el ingrediente.
    '''

    __mapper_args__ = {
        'polymorphic_identity': Ingredient_Type.BASE
    }

    def is_available(self) -> bool:
        return self.units >= 0.2

    def register_sale(self) -> None:
        self.units = round(self.units - 0.2, 2)

    def supply(self) -> None:
        return self.add_units(5.0)
