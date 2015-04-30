from textwrap import dedent
import re

__author__ = 'nekmo'


class Doc(object):
    msg = 'Usage for command {name}: {command}'
    msg_base  = 'Usage: {command}'

    def __init__(self, name, command):
        self.name = name
        self.command = command

    def set_args_types(self, args):
        pass

    def process_doc_msg(self, text):
        return re.sub(' +', ' ', dedent(text).replace('\n', ' '))

    def set_from_function(self, function):
        if function.__doc__:
            self.msg = self.process_doc_msg(function.__doc__)

    def __str__(self):
        return self.msg.format(**{
            'name': self.name, 'command': self.command, 'msg_base': self.msg_base
        })