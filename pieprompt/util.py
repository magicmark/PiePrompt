# -*- coding: utf-8 -*-
import subprocess
from collections import namedtuple

from colors import color as ansicolor

Part = namedtuple('Part', ('colored_output', 'raw_length'))

class Color:
    WHITE = 0
    RED = 9
    GREY = 6
    YELLOW = 82
    BLUE = 4
    GREEN = 3
    CYAN = 36
    PURPLE = 139
    UHOH = 202


def run_command(command):
    process = subprocess.check_output(
        command,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    return process.decode('UTF-8').strip()


def colorize(color, text, bold=True):
    params = {}
    if bold:
        params['style'] = 'bold'

    return ansicolor(text, fg=color, **params)
