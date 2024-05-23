#!/usr/bin/env python3
"""
User session module
"""
from models.base import Base
from models.user import User
from typing import TypeVar
import hashlib
import uuid


class UserSession(Base):
    """ UserSession class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a UserSession instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.session_id = kwargs.get('session_id', "")
        self.session_token = kwargs.get('session_token', "")

    def create_session_token(self) -> str:
        """ Create a session token
        """
        token = str(uuid.uuid4())
        self.session_token = hashlib.md5(token.encode()).hexdigest()
        return self.session_token

    def get_user(self) -> TypeVar('User'):
        """ Get the User instance
        """
        return User.get(self.user_id)
