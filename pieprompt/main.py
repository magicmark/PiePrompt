#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates the PS1 string for zsh.
"""
import sys
from pieprompt.parts import get_parts
from pieprompt.util import colorize
from pieprompt.util import Color

def construct_ps1(parts, seperator):
    ps1 = '\n' + seperator.join(
        [part.colored_output for part in parts]
    )

    return ps1


def print_top(window_width):
    parts = get_parts()
    top_line_length = sum([part.raw_length for part in parts]) + 3

    if top_line_length >= window_width:
        seperator = '\n' + colorize(Color.PURPLE, '╠═') + ' '
    else:
        seperator = ' '

    print(construct_ps1(parts, seperator))


def print_bottom():
    ps1_bottom = '{bottom_brace} {u2253} '.format(
        bottom_brace=colorize(Color.PURPLE, '╚═'),
        u2253=colorize(Color.WHITE, '≓'),
    )

    sys.stdout.write(ps1_bottom)
    sys.stdout.flush()


def main():
    cols = int(sys.argv[2])

    if sys.argv[1] == 'top':
        print_top(cols)
    elif sys.argv[1] == 'bottom':
        print_bottom()


if __name__ == '__main__':
    exit(main())
