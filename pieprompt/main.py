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
    ps1 = '\n{top_brace}{user}{at}{host}:{seperator}{dir}'.format(
        top_brace=parts.get('top_brace').colored_output,
        seperator=seperator,
        user=parts.get('user').colored_output,
        at=parts.get('at').colored_output,
        host=parts.get('host').colored_output,
        dir=parts.get('dir').colored_output,
    )

    seen_parts = ('user', 'at', 'host', 'dir', 'top_brace')

    for part_name, part in parts.items():
        if part_name not in seen_parts:
            ps1 += seperator + part.colored_output

    return ps1


def print_top(window_width):
    parts = get_parts()
    top_line_length = sum([part.raw_length for part in parts.values()]) + 3

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