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


def get_parts():
    parts = {}
    parts['top_brace'] = Part(
        colored_output=colorize(Color.PURPLE, '╔═') + ' ',
        raw_length=3,
    )

    username = getuser()
    parts['user'] = Part(
        colored_output=colorize(Color.BLUE, username),
        raw_length=len(username),
    )

    hostname = gethostname()
    parts['host'] = Part(
        colored_output=colorize(Color.GREEN, hostname),
        raw_length=len(hostname),
    )

    parts['at'] = Part(
        colored_output=colorize(Color.WHITE, '@', False),
        raw_length=1,
    )

    home_dir = os.path.expanduser('~')
    curr_dir = os.getcwd().replace(home_dir, '~')
    parts['dir'] = Part(
        colored_output=colorize(Color.GREY, curr_dir),
        raw_length=len(curr_dir),
    )

    git_part = get_git_part()
    if git_part:
        parts['git'] = git_part

    venv_part = get_venv_part()
    if venv_part:
        parts['venv'] = venv_part


    parts['test'] = Part(
        colored_output="This is b test hello",
        raw_length=20,
    )

    return parts

