from models.ingredient import Ingredient
from models.product import Product


class Ice_Cream_Shop():
    '''
    Representa la aplicación para una tienda de helados.\n
    Funciona con 3 módulos: Ingredientes, Productos y Ventas.\n

    Attributes:
        name (str): El nombre de la tienda.
        location (str): La ubicación de la tienda.
        ingredients_module (Ingredients_Module): Módulo de ingredientes.
        products_module (Products_Module): Módulo de productos.
        sales_module (Sales_Module): Módulo de ventas.
    '''
    def __init__(self, name: str, location: str):
        '''
        Constructor.
        Args:
            name (str): El nombre de la tienda.
            location (str): La ubicación de la tienda.
        '''
        self.name = name
        self.location = location
        self._products = []
        self._ingredients = []

    # properties - - - - - - - - - - - - - - - - - - - - - - -
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if name == '':
            raise ValueError('El nombre no puede estar vacío')
        else:
            self.__name = name

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        if location == '':
            raise ValueError('La ubicación no puede estar vacía')
        else:
            self.__location = location

    def add_product(self, product: Product):
        # verificar que no existan más de 4 productos
        if len(self._products) >= 4:
            raise ValueError('¡No se puede añadir más de 4 productos!')
        else:
            self._products.append(product)

    def add_ingredient(self, ingredient: Ingredient):
        self._ingredients.append(ingredient)
    
    def products(self):
        return self._products

    def ingredients(self):
        return self._ingredients
    
    def get_most_profitable_product(self) -> Product:
        '''
        Obtiene el producto más rentable de los productos disponibles en la tienda.
        Returns:
            Product: El producto más rentable.
        '''

        max_value = 0
        most_profitable_product = None

        for product in self._products:
            profit = product.calculate_profit()
            if profit > max_value:
                max_value = profit
                most_profitable_product = product

        return most_profitable_product
