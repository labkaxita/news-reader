news-reader
===========


Processors
----------

Processors are the binding between sources, triggers and actions. They can hold 
several of them. For every source, data is gotten, and every peace of data is
passed to the triggers. If one of them is activated, the peace of data is passed
to all the defined actions, so that they be executated with the given data.

                                   PROCESSOR
                  +-----------------------------------------+
                  |                                         |
                  | sources ------> triggers -----> actions |
                  |                                         |
                  +-----------------------------------------+

Several processors can be instantiated, every one of them with their associated
sources, triggers and actions.
