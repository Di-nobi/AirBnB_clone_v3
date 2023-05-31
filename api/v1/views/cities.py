#!/usr/bin/python3
""" Flask Application """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State
from models.city import City
@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def city():
    """ Lists all cities """
    new_city = []
    for state in storage.all(State).values():
        new_state.append(state)

    return jsonify(new_state.to_dict()), 200
@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """ Get a city """
    get_city= storage.get(City, city_id)
    if not get_city:
        abort(404)
    return jsonify(get_city.to_dict()), 200

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """ Delete a state """
    del_city = storage.get(City, city_id)
    if not del_city:
        abort(404)

    storage.delete(del_city)
    storage.save()
    return jsonify({}), 200

@app_views.route('/cities', methods=['POST'], strict_slashes=False)
def post_city():
    """ Creates a city """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")

    param = request.get_json()
    data_ins = State(**param)
    data_ins.save()
    return jsonify(data_ins.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """ Updates a City """
    put_st = storage.get(City, city_id)
    if put_st is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a Json")
    param = request.get_json()
    ignore_key = ['id', 'created_at', 'updated_at']

    for k, v in param.items():
        if k not in ignore_key:
            setattr(put_st, k, v)
    storage.save()

    return jsonify(put_st.to_dict()), 200
