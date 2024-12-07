from models.product import Product
from enums.e_product_type import Product_Type


class Cup(Product):
    '''
    Representa una copa de helado.

    Attributes:
        id (int): El id del producto.
        name (str): El nombre del producto.
        price (int): El precio del producto.
        cup_type (Cup_Type): El tipo de copa.
        ingredients (list[Ingredient]): Lista de ingredientes del producto.

    Methods:
        calculate_calories() -> int: Calcula el número de calorías del producto.
        calculate_cost() -> int: Calcula el costo del producto.
        calculate_profit() -> int: Calcula la rentabilidad del producto.
        get_console_options() -> Dict[str, List[str] | str]: Obtiene las opciones de la consola.
        get_product_details() -> str: Obtiene los detalles del producto.
    '''

    __mapper_args__ = {
        'polymorphic_identity': Product_Type.CUP
    }

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type.to_dict(),
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients]
        }
