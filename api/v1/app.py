#!/usr/bin/python3
""" Starting api """
from flask import Flask, render_template, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down():
    storage.close()
@app.error_handler(404)
def error():
    """ Handles error """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
