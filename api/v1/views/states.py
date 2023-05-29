#!/usr/bin/python3
""" Creates a new view for state """
from flask import jsonify, make_response, abort
from models.state import State
from models import storage

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state():
    """ Gets all states """
    new_state = []
    for state in storage.all(State).values():
        new_state.append(state)
    return jsonify(new_state.to_dict()), 200
@app_views.route('/states/<state_id>', method=['GET'], strict_slashes=False)
def state_retrieval(state_id):
    """ Retrieve state """
    find_state = storage.get(State, state_id)
    if find_state is None:
        abort(404)
    else:
        return jsonify(find_state.to_dict())

@app_views.route('/states/<state_id>' method=['DELETE'], strict_slashes=False)
def delete():
    """ deletes a state """
    del_state = storage.get(State, state_id)
    storage.delete(del_state)
    storage.save()
    if not del_state:
        abort(404)
    return jsonify({}), 200

