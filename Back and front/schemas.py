from marshmallow import fields
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from models import Location, Plant, db


class LocationSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Location
        sqla_session = db.session
        load_instance = True

    id_location_pk = fields.Int(dump_only=True)
    city_name = fields.String(required=True)
    province_name = fields.String(required=True)

    plants = fields.Nested('PlantSchema', many=True, exclude=('locations',))

#Setting the schemas for serialization of all tables (Begin)
class PlantSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Plant
        sqla_session = db.session
        load_instance = True

    id_plant_pk = fields.Int(dump_only=True)
    current_name = fields.String(required=True)
    scientific_name = fields.String(required=True)

    # AGREGA ESTO:
    # 'LocationSchema' va entre comillas porque la clase se define más abajo.
    # many=True: Una planta puede estar en muchas ciudades.
    # exclude=('plants',): Evita un bucle infinito (Planta -> Ubicación -> Planta...).
    locations = fields.Nested('LocationSchema', many=True, exclude=('plants',))


