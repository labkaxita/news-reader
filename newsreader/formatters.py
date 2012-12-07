import re


class Formatter(object):
    def format(self, entry):
        return entry


class Unicode(Formatter):
    def format(self, entry):
        return unicode(entry)

class Feed(Formatter):
    def format(self, entry):
        return entry


class HTMLStrip(Formatter):
    tags = re.compile(r'<[^>]*?>')
    def format(self, entry):
        return re.sub(self.tags, '', entry)


class FeedTitleDescription(Formatter):
    def format(self, entry):
        return u'{title}\n\n{description}'.format(
                title=entry['title'],
                description=entry['description'],
                )
