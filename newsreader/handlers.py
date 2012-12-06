from smtplib import SMTP
from sys import stdout

from newsreader.formatters import Formatter, UnicodeFormatter, HTMLStripFormatter


class Handler(object):
    def __init__(self, formatters=[]):
        if not formatters:
            formatters = [Formatter()]
        self.formatters = formatters

    def _write(self, entries):
        for entry in entries:
            for formatter in self.formatters:
                entry = formatter.format(entry)
            yield entry

    def write(self, entries):
        self.handle(self._write(entries))

    def handle(self, entries):
        raise NotImplemented()


class ConsoleHandler(Handler):
    def __init__(self, formatters=[]):
        if not formatters:
            formatters = [
                    UnicodeFormatter(),
                    HTMLStripFormatter(),
                    ]
        super(ConsoleHandler, self).__init__(formatters)

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
