from itertool import repeat
from multiprocessing import Pool


registry = []

def register(processor):
    if processor not in registry:
        registry.append(processor)


def main():
    while True:
        for processor in registry:
            processor.main()


def async_main():
    pool = Pool()
    while True:
        for processor in registry:
            iterator = processor.process()
            func = lambda x: iterator.next()
            always = repeat(True)

            process = pool.imap_unordered(func, always, chunksize=2)
            results = { handler: list(results) for handler, results in process }
            yield results
