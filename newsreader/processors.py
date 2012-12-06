import itertools


class Processor(object):
    def __init__(self, sources=[], triggers=[], handlers=[]):
        self.sources = sources
        self.triggers = triggers
        self.handlers = handlers

    def triggered_entries(self):
        for source in self.sources:
            for entry in source.read():
                if any(( trigger.is_activated(entry) for trigger in self.triggers )):
                    yield entry

    def process(self):
        cached_entries = itertools.tee(
                self.triggered_entries(),
                len(self.handlers),
                )
        for handler, entries in zip(self.handlers, cached_entries):
            handler.write(entries)
