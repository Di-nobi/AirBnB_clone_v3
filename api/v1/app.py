#!/usr/bin/python3
""" Starting api """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

#registers a blueprint
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(e):
    """ Closes the storage """
    storage.close()

@app.errorhandler(404)
def error():
    """ Handles error and displays the json format """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
