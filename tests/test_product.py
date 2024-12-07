import unittest
from enums.e_cup_type import Cup_Type
from models.base_ingredient import Base_Ingredient
from models.complement import Complement
from models.ingredient import Ingredient
from models.cup import Cup
from models.milk_shake import Milk_Shake
from models.product import Product


class TestProduct(unittest.TestCase):
    def get_ingredients(self) -> list[Ingredient]:
        '''
        Obtiene los ingredientes para el producto
        con un total de 100 calorías y 1000 precio.
        '''
        ingredient_1 = Base_Ingredient(
            name='Ingrediente 1',
            price=200,
            calories=20,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient_2 = Base_Ingredient(
            name='Ingrediente 2',
            price=300,
            calories=30,
            is_vegetarian=True,
            units=2.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient_3 = Complement(
            name='Ingrediente 3',
            price=500,
            calories=50,
            is_vegetarian=True,
            units=3.0,
            extra_data={'flavor': 'Chocolate'}
        )
        return [ingredient_1, ingredient_2, ingredient_3]

    def append_products(self, product: Product,  ingredients: list[Ingredient]) -> None:
        ''' Agrega ingredientes a un producto '''
        product.ingredients.append(ingredients[0])
        product.ingredients.append(ingredients[1])
        product.ingredients.append(ingredients[2])

    def test_calculate_calories_in_cup_product(self):
        cup_product = Cup(
            name='Producto',
            price=10000,
            extra_data={'cup_type': Cup_Type.MEDIUM.value}
        )

        ingredients = self.get_ingredients()
        self.append_products(cup_product, ingredients)

        self.assertEqual(cup_product.calculate_calories(), 95)
    
    def test_calculate_calories_in_milk_shake_product(self):
        milk_shake_product = Milk_Shake(
            name='Producto',
            price=10000,
            extra_data={'ounces': 10}
        )

        ingredients = self.get_ingredients()
        self.append_products(milk_shake_product, ingredients)

        self.assertEqual(milk_shake_product.calculate_calories(), 295)
    
    def test_calculate_cost_in_cup_product(self):
        cup_product = Cup(
            name='Producto',
            price=10000,
            extra_data={'cup_type': Cup_Type.MEDIUM.value}
        )

        ingredients = self.get_ingredients()
        self.append_products(cup_product, ingredients)

        self.assertEqual(cup_product.calculate_cost(), 1000)
    
    def test_calculate_cost_in_milk_shake_product(self):
        milk_shake_product = Milk_Shake(
            name='Producto',
            price=10000,
            extra_data={'ounces': 10}
        )

        ingredients = self.get_ingredients()
        self.append_products(milk_shake_product, ingredients)

        self.assertEqual(milk_shake_product.calculate_cost(), 1500)

    def test_calculate_profit_in_cup_product(self):
        cup_product = Cup(
            name='Producto',
            price=10000,
            extra_data={'cup_type': Cup_Type.MEDIUM.value}
        )

        ingredients = self.get_ingredients()
        self.append_products(cup_product, ingredients)

        self.assertEqual(cup_product.calculate_profit(), 9000)
    
    def test_calculate_profit_in_milk_shake_product(self):
        milk_shake_product = Milk_Shake(
            name='Producto',
            price=10000,
            extra_data={'ounces': 10}
        )

        ingredients = self.get_ingredients()
        self.append_products(milk_shake_product, ingredients)

        self.assertEqual(milk_shake_product.calculate_profit(), 8500)
    
    def test_register_sale(self):
        cup_product = Cup(
            name='Producto',
            price=10000,
            extra_data={'cup_type': Cup_Type.MEDIUM.value}
        )

        ingredients = self.get_ingredients()
        self.append_products(cup_product, ingredients)

        self.assertEqual(cup_product.is_available(), True)

        cup_product.register_sale()
        cup_product.register_sale()
        cup_product.register_sale()

        self.assertEqual(cup_product.is_available(), False)

        # generar un error del tipo ValueError
        with self.assertRaises(ValueError):
            cup_product.register_sale()

if __name__ == '__main__':
    unittest.main()
