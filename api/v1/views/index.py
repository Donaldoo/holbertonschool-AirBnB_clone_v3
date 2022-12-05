#!/usr/bin/python3
""" index """

from api.v1.views import app_views
from flask import jsonify
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ returns a json """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """ retrives the number of each class objects """
    classes = [Amenity, City, Place, Review, States, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    stats = {}

    for index in range(len(classes)):
        stats[names[index]] = self.storage.count(classes[index])

    return jsonify(stats)