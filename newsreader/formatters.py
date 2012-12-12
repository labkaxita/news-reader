import re

class Formatter(object):
    def format(self, entries):
        return entries


class FeedMailFormatter(Formatter):
    def format(self, entries):
        for entry in entries:
            yield str(entry)
