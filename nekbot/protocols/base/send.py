from nekbot.utils.strings import long_message

__author__ = 'nekmo'


class Send(object):
    def send_message(self, body, notice=False):
        raise NotImplementedError("This protocol can't send messages.")

    def short_message(self, body):
        self.send_method(body, not long_message(body))

    def send_warning(self, body):
        self.send_method('Warning: %s' % body, not long_message(body))

    def send_error(self, body):
        self.send_method('Error: %s' % body, not long_message(body))

    send_method = send_message


class MessageSend(object):
    def reply(self, body, notice=False):
        raise NotImplementedError("This protocol can't reply messages.")

    send_method = reply
    reply_warning = Send.send_warning
    reply_error= Send.send_error