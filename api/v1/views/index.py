#!/usr/bin/python3

"""
creaate flask app view
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def api_status():
    """
    return the status of the api

    """
    res = jsonify({'status': 'OK'})
    return res
