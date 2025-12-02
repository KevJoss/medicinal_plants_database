from flask import render_template
from flask import Blueprint

review_ui = Blueprint('review_ui', __name__)

@review_ui.route('/review_form/<int:plant_id>')
def review_form(plant_id):
    return render_template("review_form.html", plant_id=plant_id)
