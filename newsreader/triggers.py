import dateutil


class Trigger(object):
    def is_activated(self, entry):
        raise NotImplemented()


class And(objects):
    def __init__(self, subtriggers=[]):
        self.subtriggers = subtriggers

    def is_activated(self, entry):
        return all(( trigger.is_activated(entry) for trigger in \
                self.subtriggers ))


class Or(objects):
    def __init__(self, subtriggers=[]):
        self.subtriggers = subtriggers

    def is_activated(self, entry):
        return any(( trigger.is_activated(entry) for trigger in \
                self.subtriggers ))


class Contains(Trigger):
    def __init__(self, string, case_sensitive=False):
        self.string = string
        self.case_sensitive = case_sensitive

    def is_activated(self, entry):
        string = self.string
        if not self.case_sensitive:
            string = string.lower()
            entry = entry.lower()
        return string in entry
    

class TimeDelta(Trigger):
    def __init__(self, past=None, future=None):
        self.past = past
        self.future = future

    def is_activated(self, entry):
        dt = dateutil.parser.parse(entry, fuzzy=True)
        past = dt > self.past if self.past is not None else True
        future = dt < self.future if self.future is not None else True
        return past and future
