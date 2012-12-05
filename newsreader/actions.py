from smtplib import SMTP
from sys import stdout


class Action(object):
    def do(self, data):
        raise NotImplemented()


class PrintConsoleAction(Action):
    def format_data(self, data):
        return data['description']

    def do(self, data):
        data = self.format_data(data)
        stdout.write(data)


class SendEmailAction(Action):
    def __init__(self, server, sender, recipients=[]):
        self.recipiends = recipiends
        self.host, self.port = server
        self.smtp = SMTP(self.host, self.port)

    def format_data(self, data):
        return data['description']

    def do(self, data):
        data = self.format_data(data)
        self.smtp.sendmail(sender, recipients, data)
