from nekbot.core.commands import cmds, command

__author__ = 'nekmo'

@command
def commands(msg):
    return 'Available commands: %s. Tip!! Use <command> -h for help.' % ' '.join(sorted(cmds.keys()))
