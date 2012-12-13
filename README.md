news-reader
===========


Overall structure
-----------------

    sources:        web              feed           Get news from many sources
                     |                 | 
                     +--------+--------+
                              |
                     +--------+--------+
                     |                 |
    triggers:       date           contains         Filter it depending on certain conditions
                     |                 |   
                     +-------any-------+
                              | 
                        web   |  feed
                     +-source-+-source-+
                     |                 |
    formatters:   web-digest      feed-digest       Format entries (depending on their source)
                     |                 |
                     +--------+--------+
                              |         
                     +--------+--------+
                     |                 |
    handlers:       mail            console         Handle the formatted entries
