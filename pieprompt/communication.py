# -*- coding: utf-8 -*-
import errno
import os
from contextlib import contextmanager

PIPE_C = os.path.join('/tmp/pieprompt-client')
PIPE_D = os.path.join('/tmp/pieprompt-daemon')


def send_to_daemon(part):
    try:
        os.mkfifo(PIPE_D)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    with open(PIPE_D, 'w') as f:
        f.write(part)


def send_to_client(part):
    try:
        os.mkfifo(PIPE_C)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    with open(PIPE_C, 'w') as f:
        f.write(part)


@contextmanager
def listen(pipe):
    """
    try:
        os.mkfifo(pipe)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise
    """
    with open(pipe) as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                break

            yield data


@contextmanager
def ask_daemon(data):
    send_to_daemon(data)
    with listen(PIPE_C) as response:
        yield response
