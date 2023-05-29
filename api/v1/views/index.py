#!/usr/bin/python3
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models.base_model import BaseModel
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status return OK """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Retrieves number of each of the object """
    return jsonify({"amenities": storage.count("Amenity"),
                   "cities": storage.count("City"),
                   "places": storage.count("Place"),
                   "reviews": storage.count("Review"),
                   "states": storage.count("State"),
                   "users": storage.count("User")
                   })
