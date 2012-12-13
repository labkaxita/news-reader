import itertools

from newsreader.formatters import Formatter


class SourceProcessor(object):
    def __init__(self, sources):
        self.sources = sources

    def process(self):
        for source, formatter in self.sources.items():
            entries = source.read()
            if formatter is None:
                formatter = Formatter()
            for entry in entries:
                entry.formatter = formatter
                yield entry


class TriggerProcessor(object):
    def __init__(self, triggers):
        self.triggers = triggers

    def process(self, entries):
        empty = len(self.triggers) == 0
        for entry in entries:
            if empty or any(( trigger.is_activated(entry) \
                    for trigger in self.triggers )):
                yield entry


class HandlerProcessor(dict):
    def __init__(self, handlers):
        self.handlers = handlers

    def process(self, entries):
        cached_entries = itertools.tee(entries, len(self.handlers))
        joined = zip(self.handlers, cached_entries)

        for handler, entries in joined:
            entries = ( entry.format() for entry in entries )
            yield (handler, handler.write(entries))
                

class Processor(object):
    def __init__(self, sources={}, triggers=[], handlers=[]):
        self.sources = sources
        self.triggers = triggers
        self.handlers = handlers

    @property
    def source_processor(self):
        return SourceProcessor(self.sources)

    @property
    def trigger_processor(self):
        return TriggerProcessor(self.triggers)

    @property
    def handler_processor(self):
        return HandlerProcessor(self.handlers)

    def process(self):
        entries = self.source_processor.process()
        entries = self.trigger_processor.process(entries)
        results = self.handler_processor.process(entries)
        return results

    def main(self):
        return { handler: list(results) for handler, results in self.process() }
