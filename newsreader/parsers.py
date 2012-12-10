from datetime import datetime

class Entry(object):
    keys = ('title', 'description', 'body', 'datetime')

    def __init__(self, **kwargs):
        for key in self.keys:
            value = kwargs.get(key, None)
            setattr(self, key, value)
        self.others = kwargs.get('others', {})

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(key)


class Parser(object):
    def parse(self, entry):
        return Entry(body=entry)
