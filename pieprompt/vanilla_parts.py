# -*- coding: utf-8 -*-
import os
import subprocess
import sys
from collections import namedtuple
from functools import lru_cache
from getpass import getuser
from socket import gethostname

from colors import color as ansicolor

from pieprompt.git_part import get_git_part
from pieprompt.parts import Part
from pieprompt.parts import register
from pieprompt.util import Color
from pieprompt.util import colorize


def get_cwd_part():
    home_dir = os.path.expanduser('~')
    curr_dir = os.getcwd().replace(home_dir, '~')

    return Part(
        colored_output=colorize(Color.GREY, curr_dir),
        raw_length=len(curr_dir),
    )


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


def get_userathost_part():
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


def get_u2253():
    return Part(
        colored_output=colorize(Color.WHITE, '≓'),
        raw_length=1,
    )


def register_vanilla_parts():
    register('cwd', get_cwd_part)
    register('venv', get_venv_part)
    register('userathost', get_userathost_part)
    register('git', get_git_part)
    register('u2253', get_u2253)
