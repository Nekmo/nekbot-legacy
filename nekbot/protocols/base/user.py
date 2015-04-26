# coding=utf-8

__author__ = 'nekmo'

class User(object):

    def __init__(self, protocol, username, id=None, groupchat=None):
        self.protocol, self.username, self.groupchat = protocol, username, groupchat
        if hasattr(self, 'id') and id is not None:
            # id puede ser un método. No queremos entonces sobrescribirlo.
            self.id = id

    def send_message(self, body, notice=False):
        raise NotImplementedError("This protocol can't send messages to users.")

    @property
    def permissions(self):
        pass

    def __repr__(self):
        return '<%s %s id:%s>' % (self.__class__, self.username, self.id)

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return self.id == other.id

class Users(dict):
    def __init__(self, protocol):
        self.protocol = protocol
        dict.__init__(self)
