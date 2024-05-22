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
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decodeit = base64.b64decode(base64_authorization_header)
            return decodeit.decode('utf-8')
        except Exception:
            return None
