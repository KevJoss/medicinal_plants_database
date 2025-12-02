from flask_sqlalchemy import SQLAlchemy
from datetime import date as dt_date

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'plants'
    id_plant_pk = db.Column(db.Integer, primary_key=True)
    current_name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100), nullable=False)
#   Many2many relation between plants and PlantsLocations
    locations = db.relationship('PlantsLocations', back_populates='plant')
    
    __table_args__ = (
        db.UniqueConstraint('current_name', name='PK_current_name'),
    )
    

class Location(db.Model):
    __tablename__ = 'locations'
    id_location_pk = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    province_name = db.Column(db.String(100), nullable=False)
#   Many2many relation between locations and PlantsLocations
    plants = db.relationship('PlantsLocations', back_populates='location')

class PlantsLocations(db.Model):
    __tablename__ = 'plants_locations'
    id_plant_pk = db.Column(db.Integer, db.ForeignKey('plants.id_plant_pk'), primary_key=True)
    id_location_pk = db.Column(db.Integer, db.ForeignKey('locations.id_location_pk'), primary_key=True)
#   Bidirectional conexion with Plant and Location models
    plant = db.relationship('Plant', back_populates='locations')
    location = db.relationship('Location', back_populates='plants')

# Use Model
class Use(db.Model):
    __tablename__ = 'uses'
    id_use_pk = db.Column(db.Integer, primary_key=True)
    id_plant_pk = db.Column(db.Integer, primary_key=True)
    id_location_pk = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    type_use = db.Column(db.String(200), nullable=False)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['id_plant_pk', 'id_location_pk'],
            ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
        ),
    )

    def __init__(self, id_use_pk, id_plant_pk, id_location_pk, description, type_use):
        self.id_use_pk = id_use_pk
        self.id_plant_pk = id_plant_pk
        self.id_location_pk = id_location_pk
        self.description = description
        self.type_use = type_use

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Use {self.id_use_pk}, Plant {self.id_plant_pk}, Location {self.id_location_pk}: {self.description}>'