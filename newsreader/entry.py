class Entry(dict):
    def __init__(self, *args, **kwargs):
        super(Entry, self).__init__(*args, **kwargs)
        self.formatter = None

    def format(self):
        return self.formatter.format(self)
