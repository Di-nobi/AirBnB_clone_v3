#!/usr/bin/python3
""" Creates a new view for state """
from flask import jsonify, make_response
from models.state import State
from models import storage

@app_views.route('/api/v1/states/<state_id>', method=['GET'])
def state_retrieval(state_id):
    """ Retrieve state """
    find_state = storage(State, state_id)
    if find_state is None:
        abort(404)
    else:
        return jsonify(find_state.to_dict())

@app_views.route('/api/v1/states/
