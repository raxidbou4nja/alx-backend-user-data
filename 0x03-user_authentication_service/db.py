#!/usr/bin/env python3
"""
DB class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
import bcrypt
import uuid


class DB:
    """
    DB class
    """

    def __init__(self):
        """
        Constructor
        """
        self._engine = create_engine('sqlite:///a.db', echo=True)
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user
        """
        session = self._session()
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user
