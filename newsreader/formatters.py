import re


class Formatter(object):
    def format(self, entry):
        return entry


class Unicode(Formatter):
    def format(self, entry):
        return unicode(entry)

class HTMLStrip(Formatter):
    tags = re.compile(r'<[^>]*?>')
    def format(self, entry):
        return re.sub(self.tags, '', entry)
