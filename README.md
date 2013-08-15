SimpleLogger
============

[![PyPI version](https://badge.fury.io/py/SimpleLogger.png)](http://badge.fury.io/py/SimpleLogger)

Very simple Python logging

A small module used for basic logging purposes.

Installation:
-------------
Use included setup.py (`python setup.py install`)

Usage:
------
Create a new `Logger` object, and log away!

Eg.

    import simplelogger

    logger = simplelogger.Logger(threshold=simplelogger.INFO)   // INFO level implicit
    logger.info("'This is logged with level info'")
    logger.warning("This is logged with level 'warning'")


To log custom log levels:

    import simplelogger
    
    logger = simplelogger.Logger()
    logger.log("custom_log_level","text")


To show lower log level threshold:

    import simplelogger

    // to log 'debug' level logs and up
    logger = simplelogger.Logger(threshold=simplelogger.DEBUG)   // INFO level implicit
    logger.info("this has always logged")
    logger.debug("but this logs now")

    // to change threshold to 'error' level logs and up
    logger.set_threshold(simplelogger.ERROR)
    logger.debug("this won't log now")
    logger.info("neither will this")
    logger.error("this will log!")
    logger.log("custom","and so will this!")    // log with 'custom' logging level


To log to file:

    import simplelogger

    logger = simplelogger.Logger(stream="/path/to/file")
    logger.warning("this is logged to file")
