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


class PIIFormatter(logging.Formatter):
    """Formatter to redact PII fields."""

    REDACTION = "***"
    FORMAT = "[SENSITIVE_DATA] %(asctime)s - %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method."""
        super(PIIFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats log records by redacting PII fields."""
        return obfuscate_fields(self.fields, self.REDACTION,
                                super(PIIFormatter, self).format(record),
                                self.SEPARATOR)


def setup_logger() -> logging.Logger:
    '''Creates a logger with custom formatting for redacting PII.'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = PIIFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def connect_to_database() -> mysql.connector.connection.MySQLConnection:
    '''Connects to a secure database.'''
    connection = mysql.connector.connection.MySQLConnection(
        user=getenv('DB_USERNAME', 'root'),
        password=getenv('DB_PASSWORD', ''),
        host=getenv('DB_HOST', 'localhost'),
        database=getenv('DB_NAME'))

    return connection


def main():
    '''Retrieves sensitive data from a secure database and logs it with PII redacted.'''
    database = connect_to_database()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM sensitive_data;")
    fields = [i[0] for i in cursor.description]

    logger = setup_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        logger.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
