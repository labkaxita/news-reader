from smtplib import SMTP
from sys import stdout


class Handler(object):
    def __init__(self, formatter=None):
        if formatter is None:
            formatter = Formatter()
        self.formatter = formatter

    def write(self, data):
        self.handle(self.formatter.format(data))

    def handle(self, data):
        raise NotImplemented()


class ConsoleHandler(Handler):
    def handle(self, data):
        stdout.write(data)


class EmailHandler(Handler):
    def __init__(self, server, sender, recipients=[]):
        self.recipiends = recipiends
        self.host, self.port = server
        self.smtp = SMTP(self.host, self.port)

    def handle(self, data):
        self.smtp.sendmail(sender, recipients, data)
