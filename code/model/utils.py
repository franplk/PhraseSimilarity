#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-04
# @Author Franplk

import numpy as np
from numpy.linalg import norm


def any2utf8(text, errors='strict', encoding='utf8'):
    """Convert a string (unicode or bytestring in `encoding`), to bytestring in utf8."""
    if isinstance(text, str):
        return text.encode('utf8')
    return str(text, encoding, errors=errors).encode('utf8')


def similarity_smooth(x, y, z, u):
    return (x * y) + z - u


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def cosine(vec1, vec2):
    if isinstance(vec1, float) or isinstance(vec2, float):
        return 0.0
    return np.dot(vec1, vec2)/(norm(vec1)*norm(vec2))
