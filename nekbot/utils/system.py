from logging import getLogger
import sys
import os

__author__ = 'nekmo'

logger = getLogger('utils.system')

def reboot():
    args = sys.argv[:]
    logger.info('Re-spawning %s' % ' '.join(args))

    args.insert(0, sys.executable)
    if sys.platform == 'win32':
        args = ['"%s"' % arg for arg in args]

    _startup_cwd = os.getcwd()
    os.chdir(_startup_cwd)
    os.execv(sys.executable, args)