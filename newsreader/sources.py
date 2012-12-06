import feedparser

from newsreader.formatters import Formatter, FeedFormatter

class Source(object):
    def __init__(self, formatters=[]):
        if not formatters:
            formatters = [Formatter()]
        self.formatters = formatters

    def read(self):
        for entry in self.entries():
            for formatter in self.formatters:
                entry = formatter.format(entry)
            yield entry

    def entries(self):
        raise NotImplemented()


class FeedParserError(Exception):
    pass


class FeedSource(Source):
    def __init__(self, url, formatters=[]):
        if not formatters:
            formatters = [FeedFormatter()]
        super(FeedSource, self).__init__(formatters)
        self.url = url

    def entries(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
