from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Importar configuración y registros de rutas
from config import Config
from models import db



# Crear la aplicación Flask
# app = Flask(__name__, template_folder='templates', static_folder='static')
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos
db.init_app(app)


# app.register_blueprint(review_ui)

# Crear tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


