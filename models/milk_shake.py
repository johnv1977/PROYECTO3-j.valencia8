from models.product import Product
from enums.e_product_type import Product_Type


class Milk_Shake(Product):
    '''
    Representa una malteada.

    attributes:
        id (int): El id del producto.
        name (str): El nombre del producto.
        price (int): El precio del producto.
        ingredients (list[Ingredient]): Lista de ingredientes del producto.

    Methods:
        calculate_calories() -> int: Calcula el número de calorías del producto.
        calculate_cost() -> int: Calcula el costo del producto.
        calculate_profit() -> int: Calcula la rentabilidad del producto.
        is_available() -> bool: Comprueba si el elemento está disponible para vender.
        register_sale() -> None: Registra la venta de un elemento.
    '''

    __mapper_args__ = {
        'polymorphic_identity': Product_Type.MILK_SHAKE
    }

    # methods - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def calculate_calories(self) -> int:
        return super().calculate_calories() + 200

    def calculate_cost(self) -> int:
        return super().calculate_cost() + 500

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type.to_dict(),
            'name': self.name,
            'price': self.price,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients]
        }
