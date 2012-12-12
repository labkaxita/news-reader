import itertools


class SourceProcessor(object):
    def __init__(self, sources):
        self.sources = sources

    def process(self):
        for source, parser in self.sources.items():
            entries = source.read()
            for entry in parser.parse(entries):
                yield entry


class TriggerProcessor(object):
    def __init__(self, triggers):
        self.triggers = triggers

    def process(self, entries):
        for entry in entries:
            if any(( trigger.is_activated(entry) for trigger in self.triggers )):
                yield entry


class HandlerProcessor(dict):
    def __init__(self, handlers):
        self.handlers = handlers

    def process(self, entries):
        cached_entries = itertools.tee(entries, len(self.handlers))
        joins = zip(
                self.handlers.keys(), 
                self.handlers.values(), 
                cached_entries)

        for handler, formatter, entries in joins:
            entries = formatter.format(entries)
            yield handler.write(entries)
                


class Processor(object):
    @property
    def source_processor(self):
        try:
            return SourceProcessor(self.sources)
        except AttributeError:
            raise AttributeError('either define sources or source_processor')

    @property
    def trigger_processor(self):
        try:
            return TriggerProcessor(self.triggers)
        except AttributeError:
            raise AttributeError('either define triggers or trigger_processor')

    @property
    def handler_processor(self):
        try:
            return HandlerProcessor(self.handlers)
        except AttributeError:
            raise AttributeError('either define handlers or handler_processor')

    def process(self):
        entries = self.source_processor.process()
        entries = self.trigger_processor.process(entries)
        results = self.handler_processor.process(entries)
        return results

    def main(self):
        results = list(self.process())
        return results
