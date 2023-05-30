#!/usr/bin/python3
""" Starts a flask application """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(e):
    """ Closes Storage """
    storage.close()

@app.errorhandler(404)
def error(e):
    """ Handles error """
    return jsonify({'error': 'Not found'}), 404

if __name__ == "__main__":
    """ Function """
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
