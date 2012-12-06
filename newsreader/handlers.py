from smtplib import SMTP
from sys import stdout

from newsreader.formatters import Formatter


class Handler(object):
    def __init__(self, formatter=None):
        if formatter is None:
            formatter = Formatter()
        self.formatter = formatter

    def _write(self, entries):
        for entry in entries:
            entry = self.formatter.format(entry)
            yield entry

    def write(self, entries):
        self.handle(self._write(entries))

    def handle(self, entries):
        raise NotImplemented()


class ConsoleHandler(Handler):
    def handle(self, entries):
        for entry in entries:
            stdout.write(entry)


class EmailHandler(Handler):
    def __init__(self, server, sender, recipients=[]):
        self.recipiends = recipiends
        self.host, self.port = server
        self.smtp = SMTP(self.host, self.port)

    def handle(self, entries):
        for entry in entries:
            self.smtp.sendmail(sender, recipients, entry)
