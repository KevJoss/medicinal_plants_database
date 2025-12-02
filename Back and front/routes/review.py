from flask import Blueprint, request, jsonify, make_response
from models import Review, db
from schemas import ReviewSchema

review_bp = Blueprint('reviews', __name__)

"""
curl -X POST http://127.0.0.1:5000/reviews/ \
-H "Content-Type: application/json" \
-d '{
  "plant_id": 1,
  "author": "María López",
  "content": "Muy buena para el dolor de cabeza.",
  "rating": 5
}'
"""

@review_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    try:
        new_data = ReviewSchema().load(data)
        review = Review(**new_data)
        db.session.add(review)
        db.session.commit()
        return jsonify(ReviewSchema().dump(review)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

"""curl -X GET http://127.0.0.1:5000/reviews/1"""


@review_bp.route('/<int:plant_id>', methods=['GET'])
def get_reviews(plant_id):
    reviews = Review.query.filter_by(plant_id=plant_id).all()
    return jsonify(ReviewSchema(many=True).dump(reviews)), 200


"""curl -X GET http://127.0.0.1:5000/reviews/review/3"""


@review_bp.route('/review/<int:id>', methods=['GET'])
def get_review_by_id(id):
    review = Review.query.get(id)
    if review:
        return jsonify(ReviewSchema().dump(review)), 200
    else:
        return jsonify({'error': 'Review not found'}), 404
    
"""
curl -X PUT http://127.0.0.1:5000/reviews/review/3 \
-H "Content-Type: application/json" \
-d '{
  "author": "María L.",
  "content": "Efectiva pero amarga.",
  "rating": 4
}'
 """


@review_bp.route('/review/<int:id>', methods=['PUT'])
def update_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data = request.get_json()
    review.author = data.get('author', review.author)
    review.content = data.get('content', review.content)
    review.rating = data.get('rating', review.rating)
    review.date = data.get('date', review.date)

    db.session.commit()
    return jsonify({'message': 'Review updated successfully'}), 200

"""
curl -X DELETE http://127.0.0.1:5000/reviews/review/3
"""

@review_bp.route('/review/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'}), 200