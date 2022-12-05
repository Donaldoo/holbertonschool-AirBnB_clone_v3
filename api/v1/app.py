#!/usr/bin/python3
""" task 4 """
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ closes current sqlalchemy session """
    storage.close()

@app.errorhandler(404)
def error_404(self):
    """ handles not found error """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', '5000'), threaded=True)
