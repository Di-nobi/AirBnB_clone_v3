#!/usr/bin/python3
""" Starting a Flask Application """
from api.v1.views import app_views
from flask import jsonify
@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns Status as OK """
    return jsonify({"status": "OK"}), 200

@app_views.route('/stats', strict_slashes=False)
def stats():
    """ An end point for retrieval of objects """
    return jsonify({"amenities": storage.count("Amenity"),
                   "cities": storage.count("City"),
                   "users": storage.count("User"),
                   "places": storage.count("Place"),
                   "states": storage.count("State"),
                   "reviews": storage.count("Review")})
