from collections import defaultdict

__author__ = 'nekmo'

class User(object):

    def __init__(self, protocol, username, id=None, groupchat=None):
        self.protocol, self.username, self.id, self.groupchat = protocol, username, id, groupchat

    def send_message(self, body, notice=False):
        raise NotImplementedError("This protocol can't send messages to users.")

    def __repr__(self):
        return '<%s %s id:%s>' % (self.__class__, self.username, self.id)

    def __str__(self):
        return self.username

class Users(dict):
    def __init__(self, protocol):
        dict.__init__(self)
