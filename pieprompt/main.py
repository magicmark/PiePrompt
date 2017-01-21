#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates the PS1 string for zsh.
"""
import configparser
import os
import sys

from pieprompt.communication import ask_daemon
from pieprompt.gather_parts import get_parts
from pieprompt.gather_parts import serve_parts
from pieprompt.output import get_bottom
from pieprompt.output import get_executed_parts
from pieprompt.output import get_top
from pieprompt.util import Color
from pieprompt.util import colorize


def get_config():
    parser = configparser.SafeConfigParser()

    # This is the default configuration
    parser.read_dict({
        'main': {
            'top_line': 'userathost cwd git venv',
            'bottom_line': 'u2253',
        },
    })

    config_file = os.path.expanduser(os.path.join(
        '~', '.config', 'pieprompt', 'pieprompt.conf',
    ))

    if os.path.exists(config_file):
        parser.read(config_file)

    return {
        section:dict(parser.items(section))
        for section in parser.sections()
    }


def main():
    config = get_config()

    if 'daemon' in sys.argv:
        serve_parts(config)

    cols = int(sys.argv[2])

    top_parts, bottom_parts = get_parts(config)

    top_parts = get_executed_parts(top_parts, config)
    bottom_parts = get_executed_parts(bottom_parts, config)


    if sys.argv[1] == 'top':
        with ask_daemon('top {}'.format(cols)) as response:
            print(response)

    elif sys.argv[1] == 'bottom':
        with ask_daemon('bottom {}'.format(cols)) as response:
            print(response)


if __name__ == '__main__':
    exit(main())
