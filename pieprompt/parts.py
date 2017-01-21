# -*- coding: utf-8 -*-
from collections import namedtuple

# TODO: not do this
_REGISTRY = {}

Part = namedtuple('Part', ('colored_output', 'raw_length'))

def register(name, part):
    _REGISTRY[name] = part
