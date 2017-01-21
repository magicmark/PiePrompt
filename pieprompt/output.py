# -*- coding: utf-8 -*-
import sys

from pieprompt.util import Color
from pieprompt.util import colorize


def get_executed_parts(parts, config):
    parts = [part() for part in parts]
    return [part for part in parts if part is not None]


def construct_line(parts, seperator):
    line = seperator.join(
        [part.colored_output for part in parts]
    )

    return line


def get_top(parts, window_width):
    top_line_length = sum([part.raw_length for part in parts]) + 3

    if top_line_length >= window_width:
        seperator = '\n' + colorize(Color.PURPLE, '╠═') + ' '
    else:
        seperator = ' '

    return '\n' + construct_line(parts, seperator)


def get_bottom(parts, window_width):
    return (
        colorize(Color.PURPLE, '╚═') + ' ' +
        construct_line(parts, ' ') + ' '
    )
