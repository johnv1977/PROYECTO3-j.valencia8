from db import db
from sqlalchemy import Column, Integer, String, text
from errors.product_not_available_error import ProductNotAvailableError
from models.product import Product


class Sale(db.Model):
    '''
    Representa una venta.
    Una venta es un registro de una compra de un producto.
    '''
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    product_name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    profit = Column(Integer, nullable=False)
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

    def __init__(self, product_id: int, product_name: str, price: int, cost: int):
        '''
        Constructor.
        Args:
            product_id (int): El id del producto usado vendido.
            product_name (string): El nombre del producto vendido.
            price (int): El precio del producto.
            cost (int): El costo del producto.
        '''
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.cost = cost
        self.profit = price - cost

    @staticmethod
    def register_sale(id: int) -> String:
        try:
            if not db.session.is_active:
                db.session.begin()
            _product = Product.query.get(id)

            if _product is None:
                raise ValueError('Producto no encontrado')

            _isAvailable = _product.is_available()
            if not _isAvailable:
                raise ProductNotAvailableError('¡No hay producto disponible para la venta!')

            _product.register_sale()
            db.session.add(_product)

            db.session.add(Sale(
                product_id=_product.id,
                product_name=_product.name,
                price=_product.price,
                cost=_product.calculate_cost()
            ))

            db.session.commit()

            return f'Se ha registrado una venta de {_product.name}'

        except Exception as e:
            db.session.rollback()
            return f'Error: {e}'
