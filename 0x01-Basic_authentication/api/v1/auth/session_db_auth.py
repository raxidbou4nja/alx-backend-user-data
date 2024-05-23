#!/usr/bin/env python3
"""
Module of SessionDBAuth views
"""
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from os import getenv
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar


class SessionDBAuth(SessionAuth):
    """ SessionDBAuth class
    """
    def create_session(self, user_id: str = None) -> str:
        """ create_session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user = User.get(user_id)
        if user is None:
            return None
        user_id = user.id
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session = Session(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id_for_session_id
        """
        if session_id is None:
            return None
        try:
            session = Session.get(session_id)
        except NoResultFound:
            return None
        if session is None:
            return None
        return session.user_id

    def destroy_session(self, request=None):
        """ destroy_session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        try:
            session = Session.get(session_id)
        except NoResultFound:
            return False
        if session is None:
            return False
        session.delete()
        return True

    def session_cookie(self, request=None):
        """ session_cookie
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
