import datetime
import re

import numpy as np


def parse_date(value, format):
    try:
        return datetime.datetime.strptime(value, format).strftime('%Y-%m-%d')
    except ValueError:
        return None


def parse_comma_separated_integer_list(value, n):
    regexp = r'.{' + str(n) + r'}'
    matches = map(str.strip, re.findall(regexp, value))
    return [int(m) if m.isdigit() else 0 for m in matches]


def parse_int_or(value: str, default=None):
    return int(value) if value.isdigit() else default


def filter_na(obj: dict):
    return {k: v for k, v in obj.items() if v not in [None, np.nan]}