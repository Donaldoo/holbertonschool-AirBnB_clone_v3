#!/usr/bin/python3
"""New view for State objects to handle RestApi"""

from api.v1.views import app_views
from flask import jsonify, make_response, request
from flask.ext.restful import abort
from models.state import State
from models import storage


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def get_all():
    """gets state info for all states"""
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
    return jsonify(states)

@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_id(state_id):
    """gets a specific state with id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_id(state_id):
    """deletes a state from it's id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return (jsonify({}))

@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a new resource as State"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def update_state(state_id):
    """updates an existing state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for k, v in request.get_json().items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(state, k, v)
    state.save()
    return jsonify(state.to_dict())