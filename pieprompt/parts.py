import os
import pwd
import subprocess
import sys
from functools import lru_cache
from getpass import getuser
from socket import gethostname

from colors import color as ansicolor

from pieprompt.util import run_command
from pieprompt.util import colorize
from pieprompt.util import Color
from pieprompt.util import Part
from pieprompt.git_part import get_git_part

def get_venv_part():
    if not os.environ.get('VIRTUAL_ENV'):
        return None

    venv = os.path.basename(os.environ.get('VIRTUAL_ENV'))
    bits = ('virtualenv:(', venv, ')')

    colored_output = ''.join((
        colorize(Color.BLUE, bits[0]),
        colorize(Color.RED, bits[1]),
        colorize(Color.BLUE, bits[2]),
    ))

    return Part(
        colored_output=colored_output,
        raw_length=sum([len(bit) for bit in bits]),
    )


def get_top_line_part():
    raw_user = getuser()
    raw_host = gethostname()

    top_brace = colorize(Color.PURPLE, '╔═') + ' '
    user = colorize(Color.BLUE, raw_user)
    at = colorize(Color.WHITE, '@', False)
    host = colorize(Color.GREEN, raw_host)

    combined = top_brace + user + at + host + ':'
    raw_length = len(raw_user) + len(raw_host) + 5

    return Part(
        colored_output=combined,
        raw_length=raw_length,
    )


def get_dir_part():
    home_dir = os.path.expanduser('~')
    curr_dir = os.getcwd().replace(home_dir, '~')
    return Part(
        colored_output=colorize(Color.GREY, curr_dir),
        raw_length=len(curr_dir),
    )


def get_parts():
    parts = [
        get_top_line_part(),
        get_dir_part(),
    ]

    git_part = get_git_part()
    if git_part:
        parts.append(git_part)

    venv_part = get_venv_part()
    if venv_part:
        parts.append(venv_part)


    test_part = Part(
        colored_output="You've got mail!",
        raw_length=16,
    )

    parts.append(test_part)

    return parts

