import unittest
from models.ingredient import Ingredient
from models.base_ingredient import Base_Ingredient
from models.complement import Complement


class TestIngredient(unittest.TestCase):
    def test_is_healthy(self):
        ingredient = Ingredient(
            name='Ingrediente',
            price=100,
            calories=99,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )

        self.assertTrue(ingredient.is_healthy())

    def test_is_not_healthy_with_high_calories(self):
        ingredient = Ingredient(
            name='Ingrediente',
            price=100,
            calories=100,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )

        self.assertTrue(ingredient.is_healthy())

    def test_is_not_healthy_because_is_not_vegetarian(self):
        ingredient = Ingredient(
            name='Ingrediente',
            price=100,
            calories=99,
            is_vegetarian=False,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )

        self.assertTrue(ingredient.is_healthy())
    
    def test_base_ingredient_supply(self):
        ''' abastecer un Base_Ingrediente debe sumar 5.0 unidades '''
        ingredient = Base_Ingredient(
            name='Ingrediente',
            price=100,
            calories=99,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient.supply()

        self.assertEqual(ingredient.units, 6.0)
    
    def test_complement_supply(self):
        ''' abastecer un Complement debe sumar 10.0 unidades '''
        ingredient = Complement(
            name='Ingrediente',
            price=100,
            calories=99,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient.supply()

        self.assertEqual(ingredient.units, 11.0)
    
    def test_complement_reset_units(self):
        ''' reset_units debe establecer en 0.0 las unidades del complemento '''
        ingredient = Complement(
            name='Ingrediente',
            price=100,
            calories=99,
            is_vegetarian=True,
            units=1.0,
            extra_data={'flavor': 'Chocolate'}
        )
        ingredient.reset_units()

        self.assertEqual(ingredient.units, 0.0)

if __name__ == '__main__':
    unittest.main()
