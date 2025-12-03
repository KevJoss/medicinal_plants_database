from flask import Blueprint, render_template, request, redirect, url_for
from models import Plant, Location, Use, db # ✨ Agregamos 'Use' a los imports

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    all_plants = Plant.query.all()
    return render_template("plant_list.html", plants=all_plants)

# --- RUTAS DE USOS (NUEVO) ---

@frontend_bp.route('/uses')
def uses_list():
    # Consultamos la tabla Use, pero hacemos JOIN con Plant y Location
    # para obtener los nombres en lugar de solo los IDs.
    # Esto devuelve una lista de tuplas: (Use, Plant, Location)
    results = db.session.query(Use, Plant, Location)\
        .join(Plant, Use.id_plant_pk == Plant.id_plant_pk)\
        .join(Location, Use.id_location_pk == Location.id_location_pk)\
        .order_by(Plant.current_name)\
        .all()
    
    return render_template("uses_list.html", uses_data=results)

# --- RUTAS DE CREACIÓN (YA EXISTENTES) ---

@frontend_bp.route('/create', methods=['GET'])
def create_plant_form():
    locations = Location.query.all()
    return render_template("create_plant.html", locations=locations)

@frontend_bp.route('/create', methods=['POST'])
def create_plant_submit():
    current_name = request.form.get('current_name')
    scientific_name = request.form.get('scientific_name')
    selected_location_ids = request.form.getlist('locations')

    try:
        new_plant = Plant(
            current_name=current_name,
            scientific_name=scientific_name
        )

        if selected_location_ids:
            locations_found = Location.query.filter(Location.id_location_pk.in_(selected_location_ids)).all()
            new_plant.locations.extend(locations_found)

        db.session.add(new_plant)
        db.session.commit()

        return redirect(url_for('frontend.index'))

    except Exception as e:
        db.session.rollback()
        return f"Hubo un error: {str(e)}"