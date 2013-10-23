SimpleLogger
============

[![PyPI version](https://badge.fury.io/py/SimpleLogger.png)](http://badge.fury.io/py/SimpleLogger)

Small, simple, easy to use logging for Python.

I felt the defualt Python logging module was too bulky for most of the scripts I write. So I decided to write my own, incredibly simple logging utility. It supports many basic options such as output redirection to custom objects, logging to file (through output redirection), and format customization!

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
    logger.warning("This is logged with level 'warning'")


To log at custom log levels:

    import simplelogger

    logger = simplelogger.Logger()
    logger.log("custom_log_level","text to log")


To change log level threshold:

    import simplelogger

    // to log 'debug' level logs and up
    logger = simplelogger.Logger(threshold=simplelogger.INFO)
    logger.debug("this will log now!")

    // to log 'error' level logs and up
    logger = simplelogger.Logger(threshold=simplelogger.ERROR)
    logger.info("this won't log now")


To log to file:

    import simplelogger

    logger = simplelogger.Logger(stream="/path/to/file")
    logger.warning("this is logged to file")
