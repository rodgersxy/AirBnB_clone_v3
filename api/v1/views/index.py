#!/usr/bin/python3
"""
Blueprint for index
"""

from api.v1.views import app_views
from flask import jsonify, Blueprint
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    json object with app status as return
    """
    return jsonify({"status": "OK"})
