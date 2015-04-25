from collections import defaultdict

__author__ = 'nekmo'

class GroupChat(object):

    def __init__(self, protocol, name):
        self.protocol, self.name = protocol, name

    def send_message(self, body):
        raise NotImplementedError("This protocol can't send public messages.")

    def send_message_to(self, body, to):
        raise NotImplementedError("This protocol can't send private messages to users.")

    def __str__(self):
        return self.name

class GroupChats(dict):
    def __init__(self, protocol):
        self.protocol = protocol
        super(GroupChats, self).__init__()
