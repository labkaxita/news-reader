registry = []

def register(processor):
    if processor not in registry:
        registry.append(processor)


def main():
    while True:
        for processor in registry:
            processor.main()
