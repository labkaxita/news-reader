class Parser(object):
    def parse(self, entries):
        return entries


class FeedParser(Parser):
    def parse(self, entries):
        for entry in entries:
            parsed = {
                    'title': entry['title'],
                    'description': entry['description'],
                    'body': entry['description'],
                    'url': entry['link'],
                    }
            yield parsed
