# -*- coding: utf-8 -*-
import errno
import importlib.util
import os

import pieprompt.parts
from pieprompt.communication import listen
from pieprompt.communication import PIPE_D
from pieprompt.communication import send_to_client
from pieprompt.output import get_bottom
from pieprompt.output import get_executed_parts
from pieprompt.output import get_top
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
        pieprompt.parts._REGISTRY[part]
        for part in config['main']['top_line'].split()
    ]

    bottom_parts = [
        pieprompt.parts._REGISTRY[part]
        for part in config['main']['bottom_line'].split()
    ]

    return top_parts, bottom_parts


def serve_parts(config):
    top_parts, bottom_parts = get_parts(config)

    while True:
        print('sdf')
        with listen(PIPE_D) as data:
            print('got: {0}'.format(data))
            part, cols = str(data).split()
            cols = int(cols)

            if (part == 'top'):
                executed_top_parts = get_executed_parts(top_parts, config)
                send_to_client(get_top(executed_top_parts, cols))

            if (part == 'bottom'):
                executed_bottom_parts = get_executed_parts(bottom_parts, config)
                send_to_client(get_bottom(executed_bottom_parts, cols))
