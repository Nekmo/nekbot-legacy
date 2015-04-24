# coding=utf-8
from logging import getLogger

from nekbot.core.modular import Modular
from .base.message import Message
from .base.user import User
from .base.group_chat import GroupChat
from .base import Protocol

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

__author__ = 'nekmo'

logger = getLogger('nekbot.protocols')


class Protocols(Modular):
    module_path = 'nekbot.protocols.%s'

    def __init__(self, nekbot, protocols):
        Modular.__init__(self, nekbot, protocols)

    def start(self, protocol):
        logger.info('Starting %s protocol', protocol)
        Modular.start(self, protocol)