#!/usr/bin/env python3
"""
Main file
"""

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(?<=^|\{})(?:{}=\S*?)(?={}|\Z)'.format(separator, '|'.join(fields), separator), redaction, message)
