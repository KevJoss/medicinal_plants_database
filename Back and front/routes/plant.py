from flask import Blueprint, request, jsonify
from models import Plant, Location, db
from schemas import PlantSchema

plant_bp = Blueprint('plants', __name__)

# ----------------------------------------------------------
# OBTENER TODAS LAS PLANTAS
# ----------------------------------------------------------
# curl -v http://127.0.0.1:5000/plants/
@plant_bp.route('/', methods=['GET'])
def get_all_plants():
    try:
        plants = Plant.query.all()
        # El esquema debe estar configurado para mostrar 'locations' si lo deseas
        result = PlantSchema(many=True).dump(plants)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------------------------------------------
# OBTENER UNA PLANTA POR ID
# ----------------------------------------------------------
# curl -v http://127.0.0.1:5000/plants/1
@plant_bp.route('/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'message': 'Plant not found'}), 404
    
    result = PlantSchema().dump(plant)
    return jsonify(result), 200

# ----------------------------------------------------------
# CREAR UNA NUEVA PLANTA
# ----------------------------------------------------------
'''
curl -X POST http://127.0.0.1:5000/plants/ \
-H "Content-Type: application/json" \
-d '{
    "current_name": "Nueva Planta Mágica",
    "scientific_name": "Magicus Plantus",
    "location_ids": [1, 3] 
}'
'''
# Nota: "location_ids" es una lista de IDs de las ciudades donde existe la planta
@plant_bp.route('/', methods=['POST'])
def create_plant():
    data = request.get_json()

    # 1. Validar datos básicos
    if not data or not data.get('current_name'):
        return jsonify({'error': 'El nombre común (current_name) es obligatorio'}), 400

    try:
        # 2. Crear instancia de Planta
        new_plant = Plant(
            current_name=data.get('current_name'),
            scientific_name=data.get('scientific_name')
        )

        # 3. Asociar Ubicaciones (Relación Muchos a Muchos)
        # Buscamos las ubicaciones por los IDs que nos envían en la lista "location_ids"
        location_ids = data.get('location_ids', [])
        if location_ids:
            locations_found = Location.query.filter(Location.id_location_pk.in_(location_ids)).all()
            new_plant.locations.extend(locations_found)

        # 4. Guardar en BD
        db.session.add(new_plant)
        db.session.commit()

        return jsonify(PlantSchema().dump(new_plant)), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ----------------------------------------------------------
# ACTUALIZAR UNA PLANTA
# ----------------------------------------------------------
'''
curl -X PUT http://127.0.0.1:5000/plants/1 \
-H "Content-Type: application/json" \
-d '{
    "current_name": "Manzanilla Editada",
    "location_ids": [2, 5]
}'
'''
@plant_bp.route('/<int:id>', methods=['PUT'])
def update_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'message': 'Plant not found'}), 404

    data = request.get_json()

    try:
        # Actualizar campos simples
        plant.current_name = data.get('current_name', plant.current_name)
        plant.scientific_name = data.get('scientific_name', plant.scientific_name)

        # Actualizar relaciones (Si envían location_ids, reemplazamos las anteriores)
        if 'location_ids' in data:
            location_ids = data['location_ids']
            locations_found = Location.query.filter(Location.id_location_pk.in_(location_ids)).all()
            plant.locations = locations_found # Esto actualiza la tabla intermedia automáticamente

        db.session.commit()
        return jsonify(PlantSchema().dump(plant)), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ----------------------------------------------------------
# ELIMINAR UNA PLANTA
# ----------------------------------------------------------
# curl -X DELETE http://127.0.0.1:5000/plants/1
@plant_bp.route('/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'message': 'Plant not found'}), 404

    try:
        db.session.delete(plant)
        db.session.commit()
        return jsonify({'message': 'Plant deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500