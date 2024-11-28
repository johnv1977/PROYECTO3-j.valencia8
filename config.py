import os
from dotenv import load_dotenv
from flask import url_for


load_dotenv()


def app_config(app):
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    db_string_connection = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_string_connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def app_menu_items():
    return [
        {'name': 'Inicio', 'url': url_for('app.index')},
        {'name': 'Ingredientes', 'url': url_for('ingredients.index')},
        {'name': 'Productos', 'url': url_for('products.index')},
        {'name': 'Ventas', 'url': url_for('sales.index')},
        {'name': 'Logout', 'url': url_for('users.logout')},
    ]


def app_define_global_vars(app):
    @app.context_processor
    def inject_global_vars():
        return dict(
            site_name=os.getenv('APP_NAME'),
            menu_items=app_menu_items()
        )

    return app
