from flask import Blueprint, render_template, request, redirect, url_for
from models import Plant, Location, db # Importamos db para guardar

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    all_plants = Plant.query.all()
    return render_template("plant_list.html", plants=all_plants)

# --- NUEVAS RUTAS ---

# 1. Mostrar el formulario (GET)
@frontend_bp.route('/create', methods=['GET'])
def create_plant_form():
    # Obtenemos todas las ubicaciones para mostrarlas como opciones (checkboxes)
    locations = Location.query.all()
    return render_template("create_plant.html", locations=locations)

# 2. Procesar el formulario (POST)
@frontend_bp.route('/create', methods=['POST'])
def create_plant_submit():
    # Obtener datos del formulario HTML
    current_name = request.form.get('current_name')
    scientific_name = request.form.get('scientific_name')
    
    # Obtener lista de IDs seleccionados (checkboxes)
    selected_location_ids = request.form.getlist('locations')

    try:
        # 1. Crear la Planta
        new_plant = Plant(
            current_name=current_name,
            scientific_name=scientific_name
        )

        # 2. Buscar las ubicaciones seleccionadas en la BD
        if selected_location_ids:
            locations_found = Location.query.filter(Location.id_location_pk.in_(selected_location_ids)).all()
            
            # 3. ¡MAGIA! SQLAlchemy llena la tabla intermedia automáticamente aquí
            new_plant.locations.extend(locations_found)

        # 4. Guardar todo
        db.session.add(new_plant)
        db.session.commit()

        # Redirigir al inicio
        return redirect(url_for('frontend.index'))

    except Exception as e:
        db.session.rollback()
        return f"Hubo un error: {str(e)}"