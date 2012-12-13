import re

class Formatter(object):
    def format(self, entries):
        return entries


class Unicode(Formatter):
    def format(self, entries):
        for entry in entries:
            yield unicode(entry)


class FeedDigest(Formatter):
    def format(self, entries):
        mail = ''
        for entry in entries:
            mail += str(entry)
        yield mail
