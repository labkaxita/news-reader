import re


class Formatter(object):
    def format(self, entry):
        return entry


class UnicodeFormatter(Formatter):
    def format(self, entry):
        return unicode(entry)

class FeedFormatter(Formatter):
    def format(self, entry):
        return entry


class HTMLStripFormatter(Formatter):
    tags = re.compile(r'<[^>]*?>')
    def format(self, entry):
        return re.sub(self.tags, '', entry)


class FeedTitleDescriptionFormatter(Formatter):
    def format(self, entry):
        return u'{title}\n\n{description}'.format(
                title=entry['title'],
                description=entry['description'],
                )
