from flask import Flask
from config import app_config, app_define_global_vars
from db import db, load_models, create_db
from login import app_config_login
# Api Controllers
from controllers.ingredients_controller_api import api_ingredients_blueprint
from controllers.products_controller_api import api_products_blueprint
from controllers.sales_controller_api import api_sales_blueprint
# Controllers
from controllers.app_controller import app_blueprint, define_error_handlers
from controllers.ingredients_controller import ingredients_blueprint
from controllers.products_controller import products_blueprint
from controllers.sales_controller import sales_blueprint
from controllers.user_controller import user_blueprint
# Data generators
from data.example_data import data_ingredients, data_products, data_users


# Iniciar y configurar la aplicación
app = Flask(__name__, template_folder="views")
app_config(app)
app_config_login(app)

# Iniciar la base de datos
db.init_app(app)
load_models()
create_db(app)

# Insertar datos de ejemplos
data_ingredients(app, db)
data_products(app, db)
data_users(app, db)

# Registrar las apis
app.register_blueprint(api_ingredients_blueprint)
app.register_blueprint(api_products_blueprint)
app.register_blueprint(api_sales_blueprint)
# Registrar las rutas
app.register_blueprint(app_blueprint)
app.register_blueprint(ingredients_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(sales_blueprint)
app.register_blueprint(user_blueprint)

# Definir manejadores de errores en las rutas
define_error_handlers(app)

# Definir variables globales
app_define_global_vars(app)


if __name__ == "__main__":
    app.run()
