#!/usr/bin/python3

"""The flask api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = getenv('HBNB_API_PORT', 5000)
    app.run(host=HOST, port=PORT, threaded=True)
