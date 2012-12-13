import feedparser
import random

from newsreader.entry import Entry


class Source(object):
    def read(self):
        raise StopIteration()


class RandomInt(Source):
    def __init__(self, quantity, minimum, maximum):
        self.quantity = quantity
        self.minimum = minimum
        self.maximum = maximum

    def read(self):
        for i in range(self.quantity):
            yield Entry(int=random.randint(self.minimum, self.maximum))


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
                yield Entry(entry)
