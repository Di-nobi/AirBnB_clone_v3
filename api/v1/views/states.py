#!/usr/bin/python3
""" Flask Application """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state():
    """ Lists all States """
    new_state = []
    for state in storage.all(State).values():
        new_state.append(state)

    return jsonify(new_state.to_dict()), 200
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Get a state """
    get_state = storage.get(State, state_id)
    if not get_state:
        abort(404)
    return jsonify(get_state.to_dict()), 200

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """ Delete a state """
    del_state = storage.get(State, state_id)
    if not del_state:
        abort(404)

    storage.delete(del_state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ Creates a state """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")

    param = request.get_json()
    data_ins = State(**param)
    data_ins.save()
    return jsonify(data_ins.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Updates a Styate """
    put_st = storage.get(State, state_id)
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
