#!/usr/bin/env python3
"""DB module
"""
import logging
from typing import Dict, Any

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User

logging.disable(logging.WARNING)


class DB:
    """DB class to manage the database connection and operations.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(new_user)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise Exception(f"Error adding user to database: {e}")
        return new_user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """Find a user
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound as e:
            raise NoResultFound(
                f"No user found with the given attributes: {kwargs}") from e
        except InvalidRequestError as e:
            raise InvalidRequestError(
                f"Invalid request with the given attributes: {kwargs}") from e
        return user

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """Updates a user
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        return user

        try:
            self._session.commit()
        except InvalidRequestError as e:
            self._session.rollback()
            raise ValueError(f"Invalid request: {e}") from e
