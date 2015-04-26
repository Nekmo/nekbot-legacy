# coding=utf-8
from nekbot.protocols.base.event import Event

__author__ = 'nekmo'

class Message(Event):
    event_name = 'message'

    def __init__(self, protocol, body, user, groupchat=None):
        """Un nuevo mensaje entrante
        :param protocol: Instancia del protocol
        :param body: String con el mensaje recibido.
        :param user: Instancia de User del usuario que envía el mensaje.
        :param groupchat: Instancia de GroupChat
        """
        self.protocol, self.body, self.user, self.groupchat = protocol, body, user, groupchat

    def reply(self, body):
        if self.is_groupchat and self.is_public:
            self.groupchat.send_message(body)
        else:
            self.user.send_message(body)

    @property
    def is_from_me(self):
        if self.user.id:
            property = 'id'
        else:
            property = 'username'
        if self.is_groupchat:
            return getattr(self.groupchat.bot, property) == getattr(self.user.username, property)
        else:
            return getattr(self.protocol.bot, property) == getattr(self.user, property)

    @property
    def is_groupchat(self):
        raise NotImplementedError("This protocol doesn't know if the message is from a groupchat.")

    @property
    def is_public(self):
        raise NotImplementedError("This protocol doesn't know if the message is public.")

    @property
    def is_private(self):
        raise NotImplementedError("This protocol doesn't know if the message is private.")

    def _copy(self):
        return self.__class__(self.protocol, self.body, self.user, self.groupchat)

    def copy(self):
        return self._copy()

    def __str__(self):
        return self.body