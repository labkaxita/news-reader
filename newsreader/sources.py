import feedparser

from newsreader.parsers import FeedParser


class Source(object):
    def read(self):
        return self.entries()

    def entries(self):
        raise NotImplemented()


class FeedParserError(Exception):
    pass


class Feed(Source):
    def __init__(self, url):
        self.url = url

    def entries(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
