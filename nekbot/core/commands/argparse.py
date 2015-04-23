import inspect

__author__ = 'nekmo'

class ArgParse(object):
    def __init__(self):
        self.arg_types = []

    def set_arg_types(self, arg_types):
        self.arg_types = arg_types

    def parse_arg(self, type, value):
        try:
            if hasattr(type, '__call__'):
                value = type(value)
        except Exception as e:
            raise e
        return value

    def parse(self, args):
        for i, arg in enumerate(args):
            if len(self.arg_types) <= i: break
            args[i] = self.parse_arg(self.arg_types[i], arg)
        return args


    # def get_from_function(self, function):
    #     args = inspect.getargspec(function)
    #