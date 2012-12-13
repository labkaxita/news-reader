from smtplib import SMTP
from sys import stdout


class Handler(object):
    def write(self, entries):
        return entries


class Console(Handler):
    def write(self, entries):
        for entry in entries:
            stdout.write(entry)


class Email(Handler):
    def __init__(self, server, sender, recipients=[]):
        self.recipiends = recipiends
        self.host, self.port = server
        self.smtp = SMTP(self.host, self.port)

    def write(self, entries):
        for entry in entries:
            self.smtp.sendmail(sender, recipients, entry)
