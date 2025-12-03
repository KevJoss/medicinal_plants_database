from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.plant import plant_bp
from routes.location import location_bp
from routes.use import use_bp

# Importar configuración y registros de rutas
from config import Config
from models import db


# Crear la aplicación Flask
# app = Flask(__name__, template_folder='templates', static_folder='static')
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos
db.init_app(app)

# Register blueprints
app.register_blueprint(plant_bp, url_prefix='/plants')
app.register_blueprint(location_bp, url_prefix='/locations')
app.register_blueprint(use_bp, url_prefix='/uses')


# Crear tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


