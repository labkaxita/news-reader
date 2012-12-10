import feedparser

from newsreader.parsers import FeedParser


class Source(object):
    def __init__(self, parser=None):
        if parser is None:
            parser = Parser()
        self.parser = parser

    def read(self):
        for entry in self.entries():
            yield self.parser.parse(entry)

    def entries(self):
        raise NotImplemented()


class FeedParserError(Exception):
    pass


class Feed(Source):
    def __init__(self, url, parser=None):
        if parser is None:
            parser = FeedParser
        super(Feed, self).__init__(parser)
        self.url = url

    def entries(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
