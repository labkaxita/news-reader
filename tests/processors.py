import unittest
import random

from newsreader.sources import RandomInt
from newsreader.triggers import Random
from newsreader.formatters import Unicode
from newsreader.handlers import Handler
from newsreader.processors import (Processor,
                                   SourceProcessor,
                                   TriggerProcessor,
                                   HandlerProcessor,
                                   )


class SourceProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.source_processor = SourceProcessor({
            RandomInt(10, 0, 10): None})

    def test_source_processor(self):
        random.seed(0)
        entries = self.source_processor.process()
        results = [9, 8, 4, 2, 5, 4, 8, 3, 5, 6]
        self.assertEqual(list(entries), results)


class TriggerProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.entries = range(10)
        self.trigger_processor = TriggerProcessor([])

    def test_single_trigger(self):
        random.seed(0)
        self.trigger_processor.triggers = [Random()]
        entries = self.trigger_processor.process(self.entries)
        results = [2, 3, 5, 7, 8]
        self.assertEqual(list(entries), results)

    def test_two_triggers(self):
        random.seed(0)
        self.trigger_processor.triggers = [Random(), Random()]
        entries = self.trigger_processor.process(self.entries)
        results = [1, 2, 3, 4, 5, 7, 9]
        self.assertEqual(list(entries), results)

    def test_no_trigger(self):
        self.trigger_processor.triggers = []
        entries = self.trigger_processor.process(self.entries)
        self.assertEqual(list(entries), self.entries)


class HandlerProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.entries = range(10)
        self.handler_processor = HandlerProcessor({})

    def test_single_handler(self):
        self.handler_processor.handlers = {Handler(): None}
        results = self.handler_processor.process(self.entries)
        handler, results = results.next()
        self.assertEqual(list(results), self.entries)

    def test_two_handlers(self):
        self.handler_processor.handlers = {Handler(): None, Handler(): None}
        results = self.handler_processor.process(self.entries)
        handler_0, results_0 = results.next()
        handler_1, results_1 = results.next()
        self.assertEqual(list(results_0), list(results_1), self.entries)

    def test_handler_with_formatter(self):
        self.handler_processor.handlers = {Handler(): Unicode()}
        results = self.handler_processor.process(self.entries)
        handler, results = results.next()
        expected = [ unicode(entry) for entry in self.entries ]
        self.assertEqual(list(results), expected)


class ProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.sources = {RandomInt(10, 0, 10): None}
        self.triggers = [Random()]
        self.handlers = {Handler(): Unicode()}

    def test_empty_processor(self):
        processor = Processor()
        self.assertEqual(list(processor.process()), [])
        self.assertEqual(processor.main(), {})

    def test_random_processor(self):
        random.seed(0)
        processor = Processor(self.sources, self.triggers, self.handlers)
        results = processor.main()
        self.assertEqual(results.keys(), self.handlers.keys())
        handler_results = results[self.handlers.keys()[0]]
        self.assertEqual(handler_results, ['4', '5', '8', '6'])
