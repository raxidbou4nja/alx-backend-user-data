from flask import request
from typing import List, TypeVar
from api.v1.views import app_views
from models.user import User
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

#!/usr/bin/env python3
"""
Module of Basic Auth views
"""

auth = Auth()

if os.getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()


@app_views.route('/auth_basic', methods=['GET'], strict_slashes=False)
def auth_basic() -> str:
    """ GET /auth_basic
    """
    if auth.require_auth(request.path, ['/api/v1/status/', '/api/v1/unauthorized/']):
        if auth.authorization_header(request) is None:
            return auth.access_error()
        if auth.authorization_header(request) != 'Basic YWxhZGRpbjpvcGVuc2VzYW1l':
            return auth.access_error()
        return auth.access_allowed()
    return auth.access_allowed()
