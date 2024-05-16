#!/usr/bin/env python3
"""
Main file
"""

import re
from typing import List
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''Obfuscates PII fields in log messages.'''
    pattern = '|'.join(fields
    return re.sub(
        r'(' + pattern + r')=\S*?' + re.escape(separator),
        r'\1=' + redaction + separator,
        message
    )


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor Method"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)
