#!/usr/bin/env python3
"""
Main file
"""

import re
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = '|'.join(fields)
    return re.sub(
        r'(' + pattern + r')=\S*?' + re.escape(separator),
        r'\1=' + redaction + separator,
        message
    )
