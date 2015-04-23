from types import IntType
from nekbot.core.commands import command

__author__ = 'nekmo'

@command('argnumber', int)
def argnumber(msg, number):
    assert type(number) is IntType
    msg.reply('Entregado: %i' % number)

@command
def args(msg, *args):
    msg.reply('Entregado: %s' % ', '.join(args))