from abc import abstractmethod
from db import db
from sqlalchemy import Column, Boolean, Enum, Float, Integer, JSON, String, text
from sqlalchemy.orm import relationship
from data.ingredients_products_table import ingredients_products_table
from enums.e_ingredient_type import Ingredient_Type


class Ingredient(db.Model):
    '''
    Representa un ingrediente.\n
    Según el tipo de ingrediente se puede abastecer o renovar inventario.

    Attributes:
        id (int): El id del ingrediente.
        name (str): El nombre del ingrediente.
        price (int): El precio del ingrediente.
        calories (int): El número de calorías del ingrediente.
        is_vegetarian (bool): Si el ingrediente es vegetariano o no.
        units (float): La cantidad de unidades del ingrediente.
        extra_data (dict): Datos adicionales del ingrediente.

    Methods:
        add_units(amount: float) -> None: Añade una cantidad de unidades al ingrediente.
        is_healthy() -> bool: Comprueba si el ingrediente es saludable.
        supply() -> None: Abastecer el ingrediente.
    '''

    __tablename__ = 'ingredients'

    # attributes - - - - - - - - - - - - - - - - - - - - - - -
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Ingredient_Type))
    name = Column(String(50))
    price = Column(Integer)
    calories = Column(Integer)
    is_vegetarian = Column(Boolean)
    units = Column(Float)
    extra_data = Column(JSON)
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
    products = relationship(
        'Product',
        secondary=ingredients_products_table,
        back_populates='ingredients'
    )

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'ingrediente'
    }

    # methods - - - - - - - - - - - - - - - - - - - - - - - -
    def add_units(self, amount: float) -> None:
        '''
        Añade una cantidad de unidades al ingrediente.
        Args:
            amount (float): La cantidad a añadir.
        Returns:
            None
        '''
        if amount <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        else:
            self.units = round(self.units + amount, 2)

    def is_healthy(self) -> bool:
        '''
        Comprueba si el ingrediente es saludable.\n
        Un ingrediente es sano si tiene menos de 100 calorías o es vegetariano.
        Returns:
            bool: True si el ingrediente es saludable, False en caso contrario.
        '''
        return self.calories < 100 or self.is_vegetarian

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'calories': self.calories,
            'is_vegetarian': self.is_vegetarian,
            'units': self.units,
            'extra_data': self.extra_data
        }

    # abstract methods - - - - - - - - - - - - - - - - - - - - - - - -
    @abstractmethod
    def is_available(self) -> bool:
        pass

    @abstractmethod
    def register_sale(self) -> None:
        pass

    @abstractmethod
    def supply(self) -> None:
        pass
