import feedparser

from newsreader.formatters import Formatter

class Source(object):
    def __init__(self, formatter=None):
        if formatter is None:
            formatter = Formatter()
        self.formatter = formatter

    def read(self):
        for entry in self.entries():
            yield self.formatter.format(entry)

    def entries(self):
        raise NotImplemented()


class FeedParserError(Exception):
    pass


class FeedSource(Source):
    def __init__(self, url, formatter=None):
        if formatter is None:
            formatter = FeedFormatter()
        super(FeedSource, self).__init__(formatter)
        self.url = url

    def entries(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
