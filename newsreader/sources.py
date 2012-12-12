import feedparser


class Source(object):
    def read(self):
        raise NotImplemented


class FeedParserError(Exception):
    pass


class Feed(Source):
    def __init__(self, url):
        self.url = url

    def read(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
