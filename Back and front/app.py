from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.plant import plant_bp
from routes.location import location_bp
<<<<<<< HEAD
from routes.use import use_bp
=======
from routes.frontend import frontend_bp  
>>>>>>> 09af10be9d8c740487d77cd3fecc88d30b84e0db

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
<<<<<<< HEAD
app.register_blueprint(use_bp, url_prefix='/uses')
=======
app.register_blueprint(frontend_bp, url_prefix='/')
>>>>>>> 09af10be9d8c740487d77cd3fecc88d30b84e0db


# Crear tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


