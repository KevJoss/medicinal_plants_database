from flask import Blueprint, request, jsonify, make_response
from models import Location, db
from schemas import LocationSchema

location_bp = Blueprint('locations', __name__)

# ----------------------------------------------------------
# CREAR UNA NUEVA UBICACIÓN
# ----------------------------------------------------------
'''
curl -X POST http://127.0.0.1:5000/locations/ \
-H "Content-Type: application/json" \
-d '{
    "city_name": "Quito",
    "province_name": "Pichincha"
}'
'''
@location_bp.route('/', methods=['POST'])
def create_location():
    data = request.get_json()
    try:
        # load_instance=True crea la instancia del modelo automáticamente
        new_location = LocationSchema().load(data)
        
        db.session.add(new_location)
        db.session.commit()
        
        return jsonify(LocationSchema().dump(new_location)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# ----------------------------------------------------------
# OBTENER TODAS LAS UBICACIONES
# ----------------------------------------------------------
# curl -v http://127.0.0.1:5000/locations/
@location_bp.route('/', methods=['GET'])
def all_locations():
    try:
        locations = Location.query.all()
        # many=True para listas
        result = LocationSchema(many=True).dump(locations)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------------------------------------
# OBTENER UNA UBICACIÓN POR ID
# ----------------------------------------------------------
# curl -v http://127.0.0.1:5000/locations/1
@location_bp.route('/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get(id)
    if location:
        # Esto incluirá la lista de 'plants' gracias al Nested en schemas.py
        return jsonify(LocationSchema().dump(location)), 200
    else:
        return jsonify({'message': 'Location not found'}), 404

# ----------------------------------------------------------
# ACTUALIZAR UNA UBICACIÓN
# ----------------------------------------------------------
'''
curl -X PUT http://127.0.0.1:5000/locations/1 \
     -H "Content-Type: application/json" \
     -d '{"city_name": "Guayllambamba"}'
'''
@location_bp.route('/<int:id>', methods=['PUT'])
def update_location(id):
    location = Location.query.get(id)
    if not location:
        return jsonify({'message': 'Location not found'}), 404

    data = request.get_json()
    try:
        if 'city_name' in data:
            location.city_name = data['city_name']
        if 'province_name' in data:
            location.province_name = data['province_name']

        db.session.commit()
        return jsonify(LocationSchema().dump(location)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ----------------------------------------------------------
# ELIMINAR UNA UBICACIÓN
# ----------------------------------------------------------
# curl -X DELETE http://127.0.0.1:5000/locations/1
@location_bp.route('/<int:id>', methods=['DELETE'])
def delete_location(id):
    location = Location.query.get(id)
    if location:
        try:
            db.session.delete(location)
            db.session.commit()
            return jsonify({'message': 'Location deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
        return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Location not found'}), 404