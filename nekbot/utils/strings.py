# coding=utf-8
import shlex
import re

__author__ = 'nekmo'



def long_message(message, newlines=1, length=140):
    if not isinstance(message, (str, unicode)):
        message = str(message)
    if len(message) > length:
        return True
    if len(message.split('\n')) - 1 > newlines:
        return True
    return False


def split_arguments(body):
    """Dividir una cadena de texto en un listado de argumentos como en un shell.
    """
    # Sustituyo todas las comillas sencillas entre palabras por car \x00 para luego
    # devolverlo a su original. Hago esto, porque seguramente sea un apóstrofe como
    # los usados en inglés.
    body = re.sub(r"([^\A ])\'([^\Z ])", "\\1\x00\\2", body)
    args = shlex.split(body)
    args = map(lambda x: x.replace('\x00', "'"), args)
    return args
