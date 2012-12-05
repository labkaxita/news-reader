
class Trigger(object):
    def is_activated(self, data):
        raise NotImplemented()


class TitleTrigger(Trigger):
    def __init__(self, title, case_sensitive=False):
        self.title = title
        self.case_sensitive = case_sensitive

    def is_activated(self, data):
        data = data['title']
        title = self.title
        if not self.case_sensitive:
            title = title.lower()
            data = data.lower()
        return title in data
