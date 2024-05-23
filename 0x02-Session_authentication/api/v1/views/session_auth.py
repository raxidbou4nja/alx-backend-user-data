#!/usr/bin/env python3
"""
SessionAuth views
"""
from api.v1.views import app_views
from models.user import User
import uuid
from flask import request, jsonify
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return jsonify({"error": "email or password missing"}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = sa.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie('session_id', session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    """
    if sa.destroy_session(request):
        return jsonify({}), 200
    abort(404)
