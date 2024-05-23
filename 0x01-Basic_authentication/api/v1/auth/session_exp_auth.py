#!/usr/bin/env python3
"""
Module of SessionExpAuth views
"""
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from os import getenv
from datetime import datetime, timedelta
from typing import TypeVar


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth class
    """
    user_id_by_session_id = {}
    session_duration = 0

    def __init__(self):
        """ Constructor
        """
        self.session_duration = int(getenv('SESSION_DURATION'))

    def create_session(self, user_id: str = None) -> str:
        """ create_session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id_for_session_id
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if 'created_at' not in session_dictionary:
            return None
        if (datetime.now() - session_dictionary.get('created_at')
                > timedelta(seconds=self.session_duration)):
            return None
        return session_dictionary.get('user_id')
