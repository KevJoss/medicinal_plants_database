from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 1. Definir la tabla intermedia como un objeto db.Table (Asociación pura)
# Esto es mejor para relaciones Muchos a Muchos simples.
plants_locations = db.Table('plants_locations',
    db.Column('id_plant_pk', db.Integer, db.ForeignKey('plants.id_plant_pk'), primary_key=True),
    db.Column('id_location_pk', db.Integer, db.ForeignKey('locations.id_location_pk'), primary_key=True)
)

class Plant(db.Model):
    __tablename__ = 'plants'
    id_plant_pk = db.Column(db.Integer, primary_key=True)
    current_name = db.Column(db.String(100), nullable=False, unique=True) # Agregué unique=True aquí en vez de __table_args__
    scientific_name = db.Column(db.String(100), nullable=False)
    
    # 2. Relación Muchos a Muchos directa
    # 'secondary' apunta a la tabla intermedia definida arriba.
    # 'back_populates' conecta con la propiedad 'plants' en Location.
    locations = db.relationship('Location', secondary=plants_locations, back_populates='plants')

class Location(db.Model):
    __tablename__ = 'locations'
    id_location_pk = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    province_name = db.Column(db.String(100), nullable=False)
    
    # 3. Relación inversa
    plants = db.relationship('Plant', secondary=plants_locations, back_populates='locations')

# --- NOTA IMPORTANTE SOBRE EL MODELO 'Use' ---
# Como 'Use' tiene una clave foránea compuesta que apunta a la tabla intermedia,
# debemos asegurarnos de que la tabla 'plants_locations' exista físicamente.
# Al definirla con db.Table arriba, SQLAlchemy la creará correctamente.

class Use(db.Model):
    __tablename__ = 'uses'
    id_use_pk = db.Column(db.Integer, primary_key=True)
    
    # Claves foráneas apuntando a la tabla intermedia
    id_plant_pk = db.Column(db.Integer, nullable=False)
    id_location_pk = db.Column(db.Integer, nullable=False)
    
    description = db.Column(db.Text, nullable=False)
    type_use = db.Column(db.String(200), nullable=False)

    __table_args__ = (
        # FK compuesta apuntando a la tabla intermedia
        db.ForeignKeyConstraint(
            ['id_plant_pk', 'id_location_pk'],
            ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
        ),
    )