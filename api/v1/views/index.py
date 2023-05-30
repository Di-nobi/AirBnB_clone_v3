#!/usr/bin/python3
""" Starting a Flask Application """
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns Status as OK """
    return jsonify({"status": "OK"}), 200
