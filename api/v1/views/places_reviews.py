#!/usr/bin/python3
""" Creates a new view for Review """
from models import storage
from models.review import Review
from models.place import Place
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request
@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_review(place_id):
    """ Gets all review of a place """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    get_review = []
    for review in place.reviews:
        get_review.append(review.to_dict())
    return jsonify(get_review)
@app_views.route('/reviews/review_id>', methods=['GET'], strict_slashes=False)
def a_review(review_id):
    """ Retrieves a single review of a place """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict), 200
@app_views.route('/reviews/review_id>', methods=['DELETE'], strict_slashes=False)
def del_review(review_id):
    """ Deletes a review of a place """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)

    storage.delete(review)
    storage.save()
    return jsonify({}), 200
@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def post_review(place_id):
    """ Creates a new review for a place """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    param = request.get_json()
    user = storage.get(User, param['user_id'])
    if not user:
        abort(404)

    if 'text' not in request.get_json():
        abort(400, "Missing text")

    param[place_id] = place_id
    ins = Review(**param)
    ins.save()
    return jsonify(ins.to_dict()), 201

@app_views.route('/reviews/review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """ Puts in Review """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    param = request.get_json()
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in param.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
