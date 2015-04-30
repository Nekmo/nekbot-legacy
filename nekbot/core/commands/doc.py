# coding=utf-8
import inspect
from textwrap import dedent
import re
from nekbot.utils.iter import append_or_update
from nekbot.utils.survey import InspectFunction

__author__ = 'nekmo'


class Doc(InspectFunction):
    msg = 'Usage for command {name}: {command} {args_doc}'
    msg_base  = 'Usage: {command} {args_doc}'

    def __init__(self, name, command):
        super(Doc, self).__init__()
        self.name = name
        self.command = command
        self.arg_names = []

    def process_doc_msg(self, text):
        return re.sub(' +', ' ', dedent(text).replace('\n', ' '))

    def set_from_function(self, function):
        super(Doc, self).set_from_function(function)
        self.arg_names = inspect.getargspec(function).args[1:]  # Ignoro el primero, que es el Msg
        if function.__doc__:
            self.msg = self.process_doc_msg(function.__doc__)

    def args_doc(self):
        print(self.arg_names)
        args = [('<%s (%s)>' % (self.arg_names[i], self.get_type_name(type))) for i, type
                in enumerate(self.arg_types)]
        return ' '.join(args)

    def __str__(self):
        return self.msg.format(**{
            'name': self.name, 'command': self.command, 'msg_base': self.msg_base,
            'args_doc': self.args_doc()
        })