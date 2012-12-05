import feedparser


class Source(object):
    def get_data(self):
        raise NotImplemented()


class FeedParserError(Exception):
    pass


class FeedSource(Source):
    def __init__(self, url):
        self.url = url

    def get_data(self):
        feed = feedparser.parse(self.url)
        if feed.status != 200:
            raise FeedParserError('Status code: {}'.format(feed.status))
        else:
            for entry in feed['entries']:
                yield entry
