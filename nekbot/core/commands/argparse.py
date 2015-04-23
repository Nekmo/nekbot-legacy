# coding=utf-8
import inspect
from nekbot.core.exceptions import InvalidArgument

__author__ = 'nekmo'

class AllTypes(object):
    pass

ERRORS = {
    ValueError: {
        int: 'El valor debe ser un número.',
        AllTypes: 'Debe ser de tipo {type}',
    },
}

class ArgParse(object):
    def __init__(self):
        self.arg_types = []

    def set_arg_types(self, arg_types):
        self.arg_types = arg_types

    def parse_arg(self, type, value, pos=None):
        try:
            if hasattr(type, '__call__'):
                value = type(value)
        except Exception as e:
            err_class = e.__class__
            # No es un tipo de excepción conocida.
            if not ERRORS.get(err_class): raise e
            # Es conocida, pero no tenemos tipo para el mismo, y no hay por defecto
            if not ERRORS[err_class].get(type) and not ERRORS[err_class].get(AllTypes):
                raise e
            # No tenemos tipo para él, pero sí por defecto
            if not ERRORS[err_class].get(type) and ERRORS[err_class].get(AllTypes):
                raise InvalidArgument(type, value, ERRORS[err_class][AllTypes], pos)
            # ¡Hemos triunfado! Hay para excepción->tipo
            raise InvalidArgument(type, value, ERRORS[err_class][type], pos)
        return value

    def parse(self, args):
        for i, arg in enumerate(args):
            if len(self.arg_types) <= i: break
            arg = self.parse_arg(self.arg_types[i], arg, i)
            args[i] = arg
        return args