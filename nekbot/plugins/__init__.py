from logging import getLogger
from nekbot.core.modular import Modular

logger = getLogger('nekbot.plugins')

if '__path__' in globals():
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)

class Plugins(Modular):
    module_path = 'nekbot.plugins.%s'
    fail_on_not_instance = False

    def __init__(self, nekbot, protocols):
        Modular.__init__(self, nekbot, protocols)

    def start(self, protocol):
        logger.info('Loading %s plugin', protocol)
        Modular.start(self, protocol)