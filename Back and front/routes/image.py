from flask import Blueprint, request, jsonify, make_response
from models import Image, Plant, db
from schemas import ImageSchema

image_bp = Blueprint('images', __name__)

# Crear imagen
@image_bp.route('/', methods=['POST'])
def create_image():
    data = request.json
    try:
        new_data = ImageSchema().load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Verifica que la planta exista
    plant = Plant.query.get(new_data['id_plant_pk'])
    if not plant:
        return jsonify({'error': 'Invalid id_plant_pk. Plant not found.'}), 404

    # Se recomienda verificar también la existencia de la ubicación si es necesario

    new_image = Image(**new_data)

    try:
        db.session.add(new_image)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    image_schema = ImageSchema()
    image_json = image_schema.dump(new_image)
    return jsonify(image_json), 201

# Eliminar imagen (requiere los 3 IDs)
@image_bp.route('/<int:id_image_pk>/<int:id_plant_pk>/<int:id_location_pk>', methods=['DELETE'])
def delete_image(id_image_pk, id_plant_pk, id_location_pk):
    image = Image.query.filter_by(
        id_image_pk=id_image_pk,
        id_plant_pk=id_plant_pk,
        id_location_pk=id_location_pk
    ).first()
    if image:
        db.session.delete(image)
        db.session.commit()
        return jsonify({'message': 'Image successfully deleted'}), 200
    else:
        return jsonify({'error': 'Image not found'}), 404

# Obtener todas las imágenes
@image_bp.route('/all_images', methods=['GET'])
def all_images():
    try:
        get_images = Image.query.all()
        image_schema = ImageSchema(many=True)
        images = image_schema.dump(get_images)
        return make_response(jsonify({"images": images}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

# Obtener una imagen por sus 3 IDs
@image_bp.route('/<int:id_image_pk>/<int:id_plant_pk>/<int:id_location_pk>', methods=['GET'])
def get_image(id_image_pk, id_plant_pk, id_location_pk):
    image = Image.query.filter_by(
        id_image_pk=id_image_pk,
        id_plant_pk=id_plant_pk,
        id_location_pk=id_location_pk
    ).first()
    if image:
        image_schema = ImageSchema()
        image_json = image_schema.dump(image)
        return jsonify(image_json), 200
    else:
        return jsonify({'message': 'Image not found'}), 404

# Actualizar imagen por sus 3 IDs
@image_bp.route('/<int:id_image_pk>/<int:id_plant_pk>/<int:id_location_pk>', methods=['PUT'])
def update_image(id_image_pk, id_plant_pk, id_location_pk):
    image = Image.query.filter_by(
        id_image_pk=id_image_pk,
        id_plant_pk=id_plant_pk,
        id_location_pk=id_location_pk
    ).first()
    if image:
        data = request.get_json()

        # Validar si se quiere cambiar la planta
        new_plant_id = data.get('id_plant_pk')
        if new_plant_id:
            plant = Plant.query.get(new_plant_id)
            if not plant:
                return jsonify({'error': 'Invalid id_plant_pk. Plant not found.'}), 400
            image.id_plant_pk = new_plant_id

        image.date = data.get('date', image.date)
        image.place = data.get('place', image.place)
        image.link = data.get('link', image.link)
        # Si se permite cambiar id_location_pk, agregar lógica similar

        db.session.commit()
        return jsonify({'message': 'Image updated successfully'}), 200
    else:
        return jsonify({'message': 'Image not found'}), 404