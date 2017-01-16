# -*- coding: utf-8 -*-
import os
import subprocess

from pieprompt.util import Color
from pieprompt.util import colorize
from pieprompt.util import Part
from pieprompt.util import run_command

def get_git_part():
    try:
        git_dir = run_command(('git', 'rev-parse', '--git-dir'))
    except subprocess.CalledProcessError:
        return None

    if not os.path.isdir(git_dir):
        return None

    branch_name = run_command(('git', 'symbolic-ref', '--short', '-q', 'HEAD'))

    branch_info = ''

    if os.path.isdir(os.path.join(git_dir, '..', '.dotest')):
        branch_info = '|AM/REBASE'
    elif os.path.isfile(os.path.join(git_dir, '.dotest-merge', 'interactive')):
        branch_info = '|REBASE-i'
    elif os.path.isdir(os.path.join(git_dir, '.dotest-merge')):
        branch_info = '|REBASE-m'
    elif os.path.isfile(os.path.join(git_dir, 'MERGE_HEAD')):
        branch_info = '|MERGING'
    elif os.path.isfile(os.path.join(git_dir, 'BISECT_LOG')):
        branch_info = '|BISECTING'

    git_status = run_command(('git', 'status'))
    is_clean = 'nothing to commit, working' in git_status.split('\n')[-1]

    bits = ['git:(', branch_name, ')']
    if not is_clean:
        bits.extend([' ', '✗'])

    colored_output = ''.join((
        colorize(Color.BLUE, bits[0]),
        colorize(Color.RED, bits[1]),
        colorize(Color.BLUE, bits[2]),
    ))

    if len(bits) > 3:
        colored_output += bits[3]
        colored_output += colorize(Color.UHOH, bits[4])

    return Part(
        colored_output=colored_output,
        raw_length=sum([len(bit) for bit in bits]),
    )
