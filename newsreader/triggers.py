
class Trigger(object):
    def is_activated(self, entry):
        raise NotImplemented()


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
