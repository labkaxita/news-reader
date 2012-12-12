import dateutil


class Trigger(object):
    def is_activated(self, entry):
        return True


class And(object):
    def __init__(self, subtriggers=[]):
        self.subtriggers = subtriggers

    def is_activated(self, entry):
        return all(( trigger.is_activated(entry) for trigger in \
                self.subtriggers ))


class Or(object):
    def __init__(self, subtriggers=[]):
        self.subtriggers = subtriggers

    def is_activated(self, entry):
        return any(( trigger.is_activated(entry) for trigger in \
                self.subtriggers ))


class Contains(Trigger):
    def __init__(self, key, match, case_sensitive=False):
        self.key = key
        self.match = match
        self.case_sensitive = case_sensitive

    def is_activated(self, entry):
        match = self.match
        text = entry[self.key]
        if not self.case_sensitive:
            match = match.lower()
            text = text.lower()
        return match in text
    

class TimeDelta(Trigger):
    def __init__(self, key, past=None, future=None):
        self.key = key
        self.past = past
        self.future = future

    def is_activated(self, entry):
        text = entry[key]
        dt = dateutil.parser.parse(text, fuzzy=True)
        past = dt > self.past if self.past is not None else True
        future = dt < self.future if self.future is not None else True
        return past and future
