#!/usr/bin/env python3
"""
Module of Auth views
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """ require_auth
    """
    if path is None:
        return True

    if excluded_paths is None or not excluded_paths:
        return True

    for excluded_path in excluded_paths:
        if fnmatch.fnmatch(path, excluded_path):
            return False

    return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
