SimpleLogger
============

[![PyPI version](https://badge.fury.io/py/SimpleLogger.png)](http://badge.fury.io/py/SimpleLogger)

Very simple Python logging

A small module used for basic logging purposes. Logs to console.

Installation:
-------------
Use included setup.py (`python setup.py install`)

Usage:
------
Create a new `Logger` object, and log away!

Eg.

    import simplelogger

    logger = simplelogger.Logger(threshold=simplelogger.INFO)

    logger.info("'This is logged with level info'")
    logger.warning("This is logged with level 'warning'"



To show lower log levels:

    import simplelogger

    // to log 'info' level logs and up
    logger = simplelogger.Logger(threshold=simplelogger.INFO)
    logger.info("this will log")

    // to log 'debug' level logs and up
    logger = simplelogger.Logger(threshold=simplelogger.DEBUG)
    logger.debug("this will log now too!")



To log to file:

    import simplelogger

    logger = simplelogger.Logger(stream="path/to/file")

    logger.warning("this is logged to file")
