#!/usr/bin/env/python
# coding=utf-8

__version__ = 'Mirai 0.1'
__author__ = 'nekmo'

from nekbot.conf import settings
from nekbot.core import NekBot
from nekbot.protocols import Protocols

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    nekbot = NekBot().start()
    try:
        nekbot.loop()
    except (KeyboardInterrupt, SystemExit):
        nekbot.close()