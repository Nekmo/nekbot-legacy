# coding=utf-8
import re
from nekbot.core.exceptions import InvalidArgument
from nekbot.utils.strings import split_arguments

__author__ = 'nekmo'

class ArgParseType(object):
    def parse(self, arg, args, msg, position):
        return arg

class Text(ArgParseType):
    def __init__(self, min_length=1, max_length=None):
        self.max_length = max_length
        self.min_length = min_length

    def parse(self, arg, args, msg, position):
        # Cojo el mensaje original, incluyendo comillas, con los argumentos que quedan
        # hasta el momento
        args.insert(0, arg) # Me han dado como primer argumento parte de la frase. La reintroduzco
        new_args = map(lambda x: '["\']?%s["\']?' % x, args)
        last_body = re.match(".*" + "(%s)$" % ' '.join(new_args), msg.body)
        if not last_body and self.min_length:
            raise InvalidArgument('The argument of type text is required.', last_body, position)
        last_body = last_body.group(1)
        if self.min_length > len(last_body):
            raise InvalidArgument('The text argument type must have at least %i characters.' % self.min_length,
                                  last_body, position)
        if self.max_length is not None:
            try:
                args[:] = split_arguments(last_body[self.max_length:])
            except ValueError:
                raise InvalidArgument('Failed to Divide up the argument of type text.'
                                      'Surely there are unmatched quotes.', last_body[self.max_length:], position)
            last_body = last_body[:self.max_length]
        else:
            # Al no haber límite de caracteres, se toma el resto de la frase. No quedan argumentos.
            args[:] = []
        return last_body