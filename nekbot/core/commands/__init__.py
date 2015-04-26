# coding=utf-8
from collections import defaultdict
from logging import getLogger
import shlex
import traceback
from nekbot import settings
from nekbot.core.commands.argparse import ArgParse
from nekbot.core.exceptions import PrintableException
from nekbot.utils.decorators import optional_args

__author__ = 'nekmo'

logger = getLogger('nekbot.core.commands')

def get_arguments(body):
    """Dividir una cadena de texto en un listado de argumentos como en un shell.
    """
    return shlex.split(body)

class Command(object):
    symbol = True

    def __init__(self, name=None, function=None, symbol=None, *args):
        self.name = name
        self.function = function
        self.symbol = symbol if symbol is not None else self.symbol
        self.argparse = self.get_argparse(args, function)

    def get_argparse(self, arg_types, function):
        argparse = ArgParse()
        argparse.set_arg_types(arg_types)
        argparse.set_from_function(function)
        # argparse.get_from_function(self.function)
        return argparse

    def execute(self, msg):
        if not hasattr(msg, 'args'):
            msg.args = get_arguments(msg.body)[1:]
        try:
            args = self.argparse.parse(msg.args)
        except Exception as e:
            return msg.reply(str(e))
        try:
            response = self.function(msg, *args)
        except PrintableException as e:
            response = str(e)
        except Exception:
            logger.error(traceback.format_exc())
            msg.reply('El comando %s no finalizó correctamente.' % repr(self))
            return
        if response is not None:
            msg.reply(response)

    def __repr__(self):
        if self.symbol:
            return settings.SYMBOL + self.name
        else:
            return self.name


class Commands(defaultdict):
    def __init__(self):
        super(Commands, self).__init__(list)

    def incoming(self, msg):
        if msg.is_groupchat and msg.groupchat.bot.username == msg.user.username:
            return
        if not msg.body.startswith(settings.SYMBOL):
            return
        args = get_arguments(msg.body)
        if not args[0] in self:
            # No es un comando, se ignora
            return
        cmd, args = args[0], args[1:]
        msg.args = args
        for command in self[cmd]:
            command.execute(msg)

    def add_command(self, name, function, *args, **kwargs):
        cmd = Command(name, function, *args, **kwargs)
        self[repr(cmd)].append(cmd)

cmds = Commands()


@optional_args
def command(func, *args, **kwargs):
    return func(*args, **kwargs)


@optional_args
class command:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        if len(args) > 1:
            name = args[1]
        else:
            name = args[0].func_name
        cmds.add_command(name, args[0], *args[1:], **kwargs)

    def __call__(self, func):
        return func(*self.args, **self.kwargs)