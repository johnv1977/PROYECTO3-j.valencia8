import os
from dotenv import load_dotenv
from flask import url_for


load_dotenv()


def app_config(app):
    db_type = os.getenv('DB_TYPE', 'sqlite')  # Default to SQLite if DB_TYPE is not set

    if db_type == 'sqlite':
        db_path = os.getenv('DB_PATH', 'sqlite:///mydatabase.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    else:
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        
        # Conexión MySQL
        db_string_connection_mysql = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        
        # Conexión PostgreSQL
        db_string_connection_postgres = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        
        # Configuración de la base de datos (puedes elegir una de las dos)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_string_connection_mysql if (db_type == 'mysql') else db_string_connection_postgres

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
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
