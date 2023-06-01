#!/usr/bin/python3
""" Starts Flask Application """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_place(city_id):
    """ gets a place """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    get_place = []
    for result in city.places():
        get_place.append(result.to_dict())
    return jsonify(get_place), 200
@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def a_place(place_id):
    """ Gets a single place """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict()), 200
@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def del_place(place_id):
    """ Deltes a place """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()

    return jsonify({}), 200
@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Creates a place """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    param = request.get_json()
    user = storage.get(User, param['user_id'])
    if not user:
        abort(404)
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    param['city_id'] = city_id
    ins = Place(**param)
    ins.save()
    return jsonify(ins.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """ Updates a place """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")

    param = request.get_json()
    ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    for k, v in param.items():
        if k not in ignore_keys:
            setattr(place, k, v)
    storage.save()
    return jsonify(place.to_dict), 200
