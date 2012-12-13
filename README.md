news-reader
===========


Overall structure
-----------------

    sources:        web              feed           Get news form many sources
                     |                 | 
                     +--------+--------+
                              |
                     +--------+--------+
                     |                 |
    triggers:       date           contains         Filter it on certain stuff
                     |                 |   
                     +-------any-------+
                              | 
                        web   |  feed
                     +-source-+-source-+
                     |                 |
    formatters:   web-digest      feed-digest       Format entries depending on their source
                     |                 |
                     +--------+--------+
                              |         
                     +--------+--------+
                     |                 |
    handlers:       mail            console         Handle the formatted entries
