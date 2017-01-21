# -*- coding: utf-8 -*-
import importlib.util
import os

import pieprompt.parts
from pieprompt.vanilla_parts import register_vanilla_parts


def load_external_parts(config):
    if config['main'].get('extra_parts'):
        extra_parts_path = os.path.expanduser(
            config['main']['extra_parts']
        )

        spec = importlib.util.spec_from_file_location(
            "piepromp.extra_parts", extra_parts_path,
        )
        extra_parts = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(extra_parts)


def get_parts(config):
    register_vanilla_parts()
    load_external_parts(config)

    top_parts = [
        pieprompt.parts._REGISTRY[part]()
        for part in config['main']['top_line'].split()
    ]

    bottom_parts = [
        pieprompt.parts._REGISTRY[part]()
        for part in config['main']['bottom_line'].split()
    ]

    top_parts = list(filter(None, top_parts))
    bottom_parts = list(filter(None, bottom_parts))

    return top_parts, bottom_parts
