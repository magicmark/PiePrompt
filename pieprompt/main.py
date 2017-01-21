#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates the PS1 string for zsh.
"""
import configparser
import os
import sys

from pieprompt.gather_parts import get_parts
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





def construct_line(parts, seperator):
    line = seperator.join(
        [part.colored_output for part in parts]
    )

    return line


def print_top(parts, window_width):
    top_line_length = sum([part.raw_length for part in parts]) + 3

    if top_line_length >= window_width:
        seperator = '\n' + colorize(Color.PURPLE, '╠═') + ' '
    else:
        seperator = ' '

    print('\n' + construct_line(parts, seperator))


def print_bottom(parts):
    sys.stdout.write(colorize(Color.PURPLE, '╚═') + ' ')
    sys.stdout.write(construct_line(parts, ' ') + ' ')
    sys.stdout.flush()


def main():
    cols = int(sys.argv[2])

    config = get_config()
    top_parts, bottom_parts = get_parts(config)

    if sys.argv[1] == 'top':
        print_top(top_parts, cols)
    elif sys.argv[1] == 'bottom':
        print_bottom(bottom_parts)


if __name__ == '__main__':
    exit(main())
