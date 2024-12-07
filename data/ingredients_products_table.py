from db import db
from sqlalchemy import Column, ForeignKey, Table


ingredients_products_table = Table(
    'ingredients_products',
    db.metadata,
    Column('ingredient_id', ForeignKey('ingredients.id'), primary_key=True),
    Column('product_id', ForeignKey('products.id'), primary_key=True)
)
