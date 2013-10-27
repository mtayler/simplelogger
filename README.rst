=============
SimpleLogger
=============

SimpleLogger is a simple logging utility for Python. I find the default Python logging module powerful, but extremely clunky and difficult to setup quickly. SimpleLogger supports basics such as output redirection, custom logging format, and logging levels.

Usage:
======
Log Levels and Threshold:
--------------------------
The current threshold that determines what level of log entries can be seen is set through ``Logger.set_threshold``, passing a constant as the argument. Level constants include DEBUG, INFO, WARNING, ERROR, and CRITICAL. Changing the threshold only affects future entries.

Logging Formats:
----------------
Logging formats are set through ``Logger.set_format``, passing a string of valid characters and substitution directives as arguments.

Valid subsitution directives include:

+------------+-----------------------------+
|  Directive | Substitution                |
+============+=============================+
| {time}     | The current time            |
+------------+-----------------------------+
| {datetime} | The current date and time   |
+------------+-----------------------------+
| {date}     | The current date            |
+------------+-----------------------------+
| {level}    | The level of the entry      |
+------------+-----------------------------+
| {text}     | The text to be logged       |
+------------+-----------------------------+

Installation:
=============
**Recommended:** ::

    pip install simplelogger

**The Hard Way:** ::

    python setup.py install


Examples:
=========
**Basic usage:**::

    import simplelogger

    # make a new logger that outputs to output_file.log, has a threshold of DEBUG, and the entry format is just the text to be logged
    logger = simplelogger.Logger(stream=output_file.log, threshold=simplelogger.DEBUG, format="{text}")

    logger.info("Log at the info level")
    logger.warning("Log at the warning level")

    if (foo > bar):
        # change the logging threshold to INFO
        logger.set_threshold(simplelogger.INFO)
    else:
        # change the format to output the logged text, the date and time, and the time separated by characters
        logger.set_format("{text}: {datetime} - {time}")

License
-------
Copyright (C) 2013  Tayler Mulligan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
