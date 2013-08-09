Title: README
Author: Tayler Mulligan
Date: August 9, 2013

simplelog
=========

Very simple Python logging

A small module used for basic logging purposes. Logs to console.

Installation:
-------------
Use included setup.py (`python setup.py install`)

Usage:
------
Create a new `Logger` object, and call `start` to begin logging.

Eg.
    import simplelogger

    def main():

    logger = simplelogger.Logger()

    logger.start()					// Begin logging
    logger.timestamp("Log this message with a timestamp")
    logger.end(2, "An error has occured")		// Prints timestamped exit code 2 with an error message
