# coding=utf-8
import inspect
from nekbot.core.exceptions import InvalidArgument, PrintableException
from nekbot.core.types.argparse import ArgParseType
from nekbot.utils.iter import append_or_update
from nekbot.utils.survey import InspectFunction

__author__ = 'nekmo'


class AllTypes(object):
    pass


ERRORS = {
    ValueError: {
        int: 'El valor debe ser un número.',
        AllTypes: 'Debe ser de tipo {type}',
    },
}


class ArgParse(InspectFunction):
    def parse_arg(self, type, value, pos=None):
        try:
            if hasattr(type, '__call__'):
                value = type(value)
        except Exception as e:
            if isinstance(e, InvalidArgument):
                # ¡Es una excepción creada por nosotros. Le damos por si lo necesitase
                # información adicional y lo lanzamos tal cual
                e.give_info(value, pos)
                raise e
            err_class = e.__class__
            # No es un tipo de excepción conocida.
            if not ERRORS.get(err_class): raise e
            # Es conocida, pero no tenemos tipo para el mismo, y no hay por defecto
            if not ERRORS[err_class].get(type) and not ERRORS[err_class].get(AllTypes):
                raise e
            # No tenemos tipo para él, pero sí por defecto
            if not ERRORS[err_class].get(type) and ERRORS[err_class].get(AllTypes):
                raise InvalidArgument(ERRORS[err_class][AllTypes], value, pos)
            # ¡Hemos triunfado! Hay para excepción->tipo
            raise InvalidArgument(ERRORS[err_class][type], value, pos)
        return value

    def parse(self, args, msg=None):
        if len(self.arg_types) > len(args):
            raise PrintableException('Not enough arguments for this command. Missing %i argument%s.' % \
                                     (len(self.arg_types), 's' if len(self.arg_types) > 1 else ''))
        args = list(args)  # Listado de argumentos que me han entregado
        final_args = []
        all_types = list(self.arg_types) + list(self.kwarg_types)  # Todos los tipos conocidos
        i = 0  # Argumento posicional
        while True:
            if not args:
                break
            if all_types:
                type_now = all_types.pop(0)  # Tomo el tipo que me toca ahora
            else:
                type_now = str  # No hay más tipos disponibles. Uso str por defecto
            word_now = args.pop(0)  # Tomo el elemento que me toca ahora
            if not isinstance(type_now, ArgParseType):
                arg = self.parse_arg(type_now, word_now, i)
            else:
                arg = type_now.parse(word_now, args, msg, i)
            final_args.append(arg)
            i += 1
        return final_args