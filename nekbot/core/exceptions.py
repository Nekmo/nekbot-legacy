# coding=utf-8
__author__ = 'nekmo'

class ProtocolError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class InvalidArgument(Exception):
    def __init__(self, type, value, msg, pos=None):
        self.type, self.value, self.msg, self.pos = type, value, msg, pos

    def __str__(self):
        body = 'El argumento '
        if self.pos is not None:
            body += 'en la posición %s ' % (self.pos + 1)
        body += 'con valor "%s", no es válido. ' % self.value
        return body + self.msg

    def __repr__(self):
        return '<InvalidArgument "%s">' % str(self)