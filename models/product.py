from db import db
from sqlalchemy import Column, Enum, Integer, JSON, String, text
from sqlalchemy.orm import relationship
from data.ingredients_products_table import ingredients_products_table
from enums.e_product_type import Product_Type
from models.ingredient import Ingredient


class Product(db.Model):
    '''
    Representa un producto.
    Un producto es un elemento que se vende en una tienda,
    máximo la tienda puede vender 4 productos.\n

    Attributes:
        id (int): El id del producto.
        name (str): El nombre del producto.
        price (int): El precio del producto.

    Methods:
        calculate_calories() -> int: Calcula el número de calorías del producto.
        calculate_cost() -> int: Calcula el costo del producto.
        calculate_profit() -> int: Calcula la rentabilidad del producto.
        get_console_options() -> Dict[str, List[str] | str]: Obtiene las opciones de la consola.
        get_product_details() -> str: Obtiene los detalles del producto.
    '''

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(Product_Type))
    name = Column(String(50))
    price = Column(Integer)
    extra_data = Column(JSON, nullable=True)
    created_at = Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        server_default=text('CURRENT_TIMESTAMP'),
        onupdate=db.func.current_timestamp())
    ingredients = relationship(
        'Ingredient',
        secondary=ingredients_products_table,
        back_populates='products'
    )

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'product'
    }

    # methdos - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def add_ingredient(self, ingredient: Ingredient) -> None:
        count = len(self.ingredients)
        if count >= 3:
            raise ValueError('¡No se puede añadir más de 3 ingredientes al producto!')
        else:
            self.ingredients.append(ingredient)

    def calculate_calories(self) -> int:
        '''
        Calcula el total de calorías de un producto.

        Suma las calorías de los ingredientes y aplica un factor de reducción del 5%.

        Args:
            calories (list[int]): Lista de enteros con las calorías de cada ingrediente.

        Returns:
            float: Calorías totales del producto, redondeadas a dos decimales.
        '''
        calories = [ingredient.calories for ingredient in self.ingredients]
        total_calories = sum(calories) * 0.95
        return round(total_calories, 2)

    def calculate_cost(self) -> int:
        """
        Calcula el costo total de los ingredients.

        Args:
            ingredients (list): Lista de diccionarios, cada uno con las llaves 'nombre' y 'precio'.

        Returns:
            int: Costo total.
        """

        total_cost = 0
        for ingredient in self.ingredients:
            total_cost += ingredient.price
        return total_cost

    def calculate_profit(self) -> int:
        return self.price - self.calculate_cost()

    def is_available(self) -> bool:
        for ingredient in self.ingredients:
            if not ingredient.is_available():
                return False
        return True

    def register_sale(self) -> None:
        if self.is_available():
            for ingredient in self.ingredients:
                ingredient.register_sale()
        else:
            raise ValueError(f'¡Oh no! Nos hemos quedado sin {self.name} :(')
