news-reader
===========


Processors
----------

Processors are the binding between sources, triggers and handlers. They can hold 
several of them. For every source, data is gotten, and every peace of data is
passed to the triggers. If one of them is activated, the peace of data is passed
to all the defined handlers, so that they be executated with the given data.

                                   PROCESSOR
                  +------------------------------------------+
                  |                                          |
                  | sources ------> triggers -----> handlers |
                  |                                          |
                  +------------------------------------------+

Several processors can be instantiated, every one of them with their associated
sources, triggers and actions.
