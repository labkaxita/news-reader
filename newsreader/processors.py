

class Processor(object):
    def __init__(self, sources=[], triggers=[], actions=[]):
        self.sources = sources
        self.triggers = triggers
        self.actions = actions

    def get_processes(self):
        for source in self.sources:
            for data in source.get_data():
                if any(( trigger.is_activated(data) for trigger in self.triggers )):
                    for action in self.actions:
                        yield lambda: action.do(data)

    def process(self):
        for process in self.get_processes():
            process()
