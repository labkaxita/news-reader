

class Processor(object):
    def __init__(self, sources=[], triggers=[], handlers=[]):
        self.sources = sources
        self.triggers = triggers
        self.handlers = handlers

    def get_processes(self):
        for source in self.sources:
            for data in source.read():
                if any(( trigger.is_activated(data) for trigger in self.triggers )):
                    for handler in self.handlers:
                        yield lambda: handler.write(data)

    def process(self):
        for process in self.get_processes():
            process()
