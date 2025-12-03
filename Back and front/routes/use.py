from flask import Blueprint, request, jsonify, make_response
from models import Use, Plant, Location, db
from schemas import UseSchema
from sqlalchemy import func

use_bp = Blueprint('uses', __name__)

'''
curl -v http://127.0.0.1:5000/uses/all_uses
'''
@use_bp.route('/all_uses', methods=['GET'])
def all_uses():
    try:
        get_uses = Use.query.all()
        use_schema = UseSchema(many=True)
        uses = use_schema.dump(get_uses)
        return make_response(jsonify({"uses": uses}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

'''
Retrieve a use by ID (Assuming id_use_pk is unique)
curl -v http://127.0.0.1:5000/uses/1
'''
@use_bp.route('/<int:id>', methods=['GET'])
def get_use(id):
    # Como la PK es compuesta, usamos filter_by en lugar de get() para buscar solo por el ID principal
    use = Use.query.filter_by(id_use_pk=id).first()
    
    if use:
        use_schema = UseSchema()
        use_json = use_schema.dump(use)
        return jsonify(use_json), 200
    else:
        return jsonify({'message': 'Use not found'}), 404

'''
Create a new Use
curl -X POST http://127.0.0.1:5000/uses/ \
-H "Content-Type: application/json" \
-d '{
    "id_plant_pk": 1,
    "id_location_pk": 1,
    "description": "Uso para el dolor de cabeza",
    "type_use": "Medicinal"
}'
'''
@use_bp.route('/', methods=['POST'])
def create_use():
    data = request.json
    
    # 1. Validar que la planta y la ubicación existan
    plant = Plant.query.get(data.get('id_plant_pk'))
    location = Location.query.get(data.get('id_location_pk'))

    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    # 2. Calcular el siguiente ID manualmente (Simulación Auto-Increment)
    max_id = db.session.query(func.max(Use.id_use_pk)).scalar()
    next_id = 1 if max_id is None else max_id + 1

    # 3. Crear el objeto
    try:
        new_use = Use(
            id_use_pk=next_id,
            id_plant_pk=data['id_plant_pk'],
            id_location_pk=data['id_location_pk'],
            description=data['description'],
            type_use=data['type_use']
        )
        
        db.session.add(new_use)
        db.session.commit()
        
        use_schema = UseSchema()
        return jsonify(use_schema.dump(new_use)), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

'''
Update a use by ID
curl -X PUT http://127.0.0.1:5000/uses/1 \
-H "Content-Type: application/json" \
-d '{
    "description": "Nueva descripcion actualizada",
    "type_use": "Ancestral"
}'
'''
@use_bp.route('/<int:id>', methods=['PUT'])
def update_use(id):
    use = Use.query.filter_by(id_use_pk=id).first()
    
    if use:
        data = request.get_json()
        
        # Actualizamos solo los campos permitidos (descripcion y tipo)
        use.description = data.get('description', use.description)
        use.type_use = data.get('type_use', use.type_use)
        
        # Nota: Generalmente no se recomienda actualizar las FK (plant/location) en un PUT simple
        # pero si lo necesitas, deberías validarlas igual que en el POST.

        try:
            db.session.commit()
            return jsonify({'message': 'Use updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Use not found'}), 404

'''
Delete a use by ID
curl -X DELETE http://127.0.0.1:5000/uses/1
'''
@use_bp.route('/<int:id>', methods=['DELETE'])
def delete_use(id):
    use = Use.query.filter_by(id_use_pk=id).first()
    
    if use:
        try:
            db.session.delete(use)
            db.session.commit()
            return jsonify({'message': 'Use successfully deleted'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Use not found'}), 404