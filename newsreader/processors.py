import itertools


class Processor(object):
    def __init__(self, sources=[], triggers=[], handlers=[]):
        self.sources = sources
        self.triggers = triggers
        self.handlers = handlers

    def triggered_data(self):
        for source in self.sources:
            for data in source.read():
                if any(( trigger.is_activated(data) for trigger in self.triggers )):
                    yield data

    def process(self):
        cached_data = itertools.tee(self.triggered_data(), len(self.handlers))
        for handler, data in zip(self.handlers, cached_data):
            handler.write(data)
