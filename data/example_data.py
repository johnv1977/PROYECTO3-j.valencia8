from enums.e_cup_type import Cup_Type
from models.base_ingredient import Base_Ingredient
from models.complement import Complement
from models.cup import Cup
from models.ingredient import Ingredient
from models.milk_shake import Milk_Shake
from models.product import Product
from models.user import User


_ingredients = [
    # name: str, price: int, calories: int, is_vegetarian: bool, units: float = 0.0, extra_data: dict = None
    Base_Ingredient(
        name="Base Café",
        price=300,
        calories=30,
        is_vegetarian=True,
        units=0.2,
        extra_data={'flavor': 'Café'}),
    Base_Ingredient(
        name="Base Chocolate",
        price=320,
        calories=40,
        is_vegetarian=True,
        units=0.4,
        extra_data={'flavor': 'Chocolate'}),
    Base_Ingredient(
        name="Base Limón",
        price=350,
        calories=55,
        is_vegetarian=True,
        units=0.6,
        extra_data={'flavor': 'Limón'}),
    Base_Ingredient(
        name="Base Mango",
        price=360,
        calories=60,
        is_vegetarian=True,
        units=0.8,
        extra_data={'flavor': 'Mango'}),
    Base_Ingredient(
        name="Base Vainilla",
        price=390,
        calories=75,
        is_vegetarian=True,
        units=1.2,
        extra_data={'flavor': 'Vainilla'}),
    # name: str, price: int, calories: int, is_vegetarian: bool, units: float):
    Complement(
        name="Chips de Chocolate",
        price=200,
        calories=99,
        is_vegetarian=True,
        units=1.0),
    Complement(
        name="Caramelo Líquido",
        price=230,
        calories=99,
        is_vegetarian=True,
        units=2.0),
    Complement(
        name="Galletas Troceadas",
        price=240,
        calories=55,
        is_vegetarian=True,
        units=3.0),
    Complement(
        name="Crema Batida",
        price=250,
        calories=80,
        is_vegetarian=True,
        units=4.0),
    Complement(
        name="Cerezas",
        price=260,
        calories=60,
        is_vegetarian=True,
        units=5.0),
    Complement(
        name="Almendras",
        price=290,
        calories=25,
        is_vegetarian=True,
        units=6.0),
]

_products = [
    Cup(name="Helado de vainilla", price=10000, extra_data={'cup_type': Cup_Type.MEDIUM.value}),
    Cup(name="Helado de limón", price=15000, extra_data={'cup_type': Cup_Type.LARGE.value}),
    Milk_Shake(name="Malteada de chocolate", price=8500, extra_data={'ounces': 10}),
    Milk_Shake(name="Malteada de café", price=9500, extra_data={'ounces': 10})
]


def data_ingredients(app, db):
    global _ingredients
    global _ingredients_instances

    with app.app_context():
        for ingredient in _ingredients:
            db.session.add(ingredient)
            db.session.commit()


def data_products(app, db):
    global _products

    with app.app_context():
        for product in _products:
            db.session.add(product)
            db.session.commit()

        _ingredient_instances = db.session.execute(db.select(Ingredient)).scalars().all()
        ingredients_products = [
            [_ingredient_instances[4], _ingredient_instances[8], _ingredient_instances[5]],
            [_ingredient_instances[3], _ingredient_instances[2], _ingredient_instances[10]],
            [_ingredient_instances[1], _ingredient_instances[7], _ingredient_instances[8]],
            [_ingredient_instances[0], _ingredient_instances[6], _ingredient_instances[9]]
        ]

        _products_instances = db.session.execute(db.select(Product)).scalars().all()

        index = 0
        for product in _products_instances:
            _ingredients_for_product = ingredients_products[index]

            for ingredient in _ingredients_for_product:
                product.ingredients.append(ingredient)

            db.session.add(product)
            db.session.commit()
            index += 1


def data_users(app, db):
    with app.app_context():
        # Usuarios
        users = [
            User(
                username='catalina',
                password='123',
                is_admin=False,
                is_employed=True
            ),
            User(
                username='juan.pablo',
                password='123',
                is_admin=False,
                is_employed=True
            ),
            User(
                username='admin',
                password='123',
                is_admin=True,
                is_employed=True
            )
        ]
        for user in users:
            db.session.add(user)
            db.session.commit()
