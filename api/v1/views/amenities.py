#!/usr/bin/python3
""" Starts Flask Application """
from models import storage
from models.amenity import Amenity
from flask import jsonify
from flask import request
from flask import abort
from api.v1.views import app_views

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def list_amenity():
    """ Lists all amenities """
    new_amenity = []
    results = storage.all(Amenity).values()
    for amenity in results:
        new_amenity.append(amenity.to_dict())
    return jsonify(new_amenity), 200

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ Gets an amenity """
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict()), 200
@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def del_amenity(amenity_id):
    """ Deletes an amenity """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """ Creates an Amenity with POST """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    parameter = request.get_json()
    data = Amenity(**parameter)
    data.save()
    return jsonify(data.to_dict()), 201
@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """ Updates the amenity """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")

    para = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for k, v in para.items():
        if k not in ignore_keys:
            setattr(amenity, k, v)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
