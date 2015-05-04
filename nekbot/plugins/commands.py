from nekbot.core.commands import cmds, command
from nekbot.core.types.argparse import Text, SetBool

__author__ = 'nekmo'

@command('commands', search=Text, by_plugin=SetBool('-p'))
def commands(msg, search='', by_plugin=False):
    print(by_plugin)
    return 'Available commands: %s. Tip!! Use <command> -h for help.' % ' '.join(sorted(cmds.keys()))

