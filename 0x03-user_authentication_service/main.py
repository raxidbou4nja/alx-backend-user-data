#!/usr/bin/env python3
"""simple app to test the authentication module.
"""

import requests
from app import AUTH

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """Test the registration of a user.
    """


def log_in_wrong_password(email: str, password: str) -> None:
    """Test logging in with wrong password.
    """


def profile_unlogged() -> None:
    """Tests behavior of trying to retrieve profile information
    while being logged out.
    """


def profile_logged(session_id: str) -> None:
    """Tests retrieving profile information whilst logged in.
    """


def log_out(session_id: str) -> None:
    """Tests tests the process of logging out from a session.
    """


def reset_password_token(email: str) -> str:
    """Tests the process of requesting a password reset.
    """


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests updating a user's password.
    """


def log_in(email: str, password: str) -> str:
    """Tests logging in.
    """


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
