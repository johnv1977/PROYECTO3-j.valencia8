from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=BaseModel)


def load_models():
    from models.ingredient import Ingredient
    from models.product import Product
    from models.base_ingredient import Base_Ingredient
    from models.complement import Complement
    from models.cup import Cup
    from models.milk_shake import Milk_Shake

    return [
        Ingredient,
        Base_Ingredient,
        Complement,
        Product,
        Cup,
        Milk_Shake,
    ]


def create_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
