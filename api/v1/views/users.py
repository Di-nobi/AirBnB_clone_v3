#!/usr/bin/python3
""" Starts Flask Application """
from models import storage
from models.user import User
from flask import jsonify
from flask import request
from flask import abort
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_user():
    """ Lists all users """
    new_user = []
    results = storage.all(User).values()
    for user in results:
        new_user.append(user.to_dict())
    return jsonify(new_user), 200

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Gets an user """
    user = storage.get(Amenity, amenity_id)

    if not user:
        abort(404)

    return jsonify(user.to_dict()), 200
@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def del_user(user_id):
    """ Deletes an user """
    user = storage.get(Amenity, amenity_id)
    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates an User with POST """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'email' not in request.get_json():
        abort(400, "Missing email")
    if 'password' not in request.get_json():
        abort(400, "Missing password")
    parameter = request.get_json()
    data = User(**parameter)
    data.save()
    return jsonify(data.to_dict()), 201
@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Updates the user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")

    para = request.get_json()
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for k, v in para.items():
        if k not in ignore_keys:
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict()), 200
