import unittest
from enums.e_cup_type import Cup_Type
from models.ice_cream_shop import Ice_Cream_Shop
from models.product import Product
from models.ingredient import Ingredient
from models.cup import Cup
from models.milk_shake import Milk_Shake

class TestApp(unittest.TestCase):
    def get_ingredients(self) -> list[Ingredient]:
        '''
        Obtiene los ingredientes para el producto
        con un total de 100 calorías y 1000 precio.
        '''
        ingredient_1 = Ingredient(
            name='Ingrediente 1',
            price=200,
            calories=20,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient_2 = Ingredient(
            name='Ingrediente 2',
            price=300,
            calories=30,
            is_vegetarian=True,
            units=2.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient_3 = Ingredient(
            name='Ingrediente 3',
            price=500,
            calories=50,
            is_vegetarian=True,
            units=3.0,
            extra_data={'flavor': 'Chocolate'}
        )

        return [ingredient_1, ingredient_2, ingredient_3]

    def get_products(self) -> list[Product]:
        ''' Obtiene 4 productos'''
        product_1 = Cup(name='Copa de 10.000', price=10000, extra_data={'cup_type': Cup_Type.MEDIUM.value})
        product_2 = Cup(name='Copa de 15.000', price=15000, extra_data={'cup_type': Cup_Type.LARGE.value})
        product_3 = Milk_Shake(name='Malteada de 10.000', price=10000, extra_data={'ounces': 10})
        product_4 = Milk_Shake(name='Malteada de 15.000', price=15000, extra_data={'ounces': 10})

        return [product_1, product_2, product_3, product_4]
    
    def test_most_profitable_product(self):
        ice_cream_shop = Ice_Cream_Shop('Ice Cream Shop', 'San Francisco')
        ingredients = self.get_ingredients()
        products = self.get_products()
        
        for product in products:
            for ingredient in ingredients:
                ice_cream_shop.add_ingredient(ingredient)
                product.add_ingredient(ingredient)
            ice_cream_shop.add_product(product)

        '''
        Copa de 10.000      venta: 10.000 - costo: 1.000 = rentabilidad  9.000
        Copa de 15.000      venta: 15.000 - costo: 1.000 = rentabilidad 14.000
        Malteada de 10.000  venta: 10.000 - costo: 1.500 = rentabilidad  8.500
        Malteada de 15.000  venta: 15.000 - costo: 1.500 = rentabilidad 13.500
        '''
        most_profitable_product = ice_cream_shop.get_most_profitable_product()

        self.assertEqual(most_profitable_product.name, 'Copa de 15.000')

if __name__ == '__main__':
    unittest.main()
