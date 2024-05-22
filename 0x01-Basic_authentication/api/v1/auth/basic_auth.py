#!/usr/bin/env python3
"""
Module of Basic Auth views
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract_base64_authorization_header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decodeit = base64.b64decode(base64_authorization_header)
            return decodeit.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))
