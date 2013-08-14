"""
SimpleLogger

Simple, easy to use Python logging package

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

A basic, easy to use Python logging module

Provides 5 logging levels, custom log formats, and the ability to log to
stdout or a file.
"""

import sys
import os

from datetime import datetime, date, time

DEBUG = 'debug'
INFO = 'info'
WARNING = 'warning'
ERROR = 'error'
CRITICAL = 'critical'


class Logger(object):
    """
    Logger([log_file[, threshold[, format]]]) -> Logger object

    Provides a basic logging object.

    Args:
        log_file: string - full path to log file
        threshold: simplelogger constant - minimum level to log (eg simplelogger.INFO)
        format: string - custom logging format. See logging_format for more details
    """
    def __init__(self, log_file=None, threshold=None, format=None):
        self.__levels__ = ['debug', 'info', 'warning', 'error', 'critical']

        if threshold == None:
            self.__threshold__ = 'info'
        else:
            self.__threshold__ = threshold

        if format == None:
            self.__format__ = '{datetime}: {level}: {text}'
        else:
            self.__format__ = logging_format

        if log_file:
            if not os.path.exists(os.path.dirname(log_file)):
                os.makedirs(os.path.dirname(log_file))

            try:
                self.output = open(log_file, 'a+')
                sys.stderr = open(log_file, 'a+')
            except IOError as e:
                raise IOError("Could not open {log_file}".format(log_file=e.filename))
        else:
            self.output = sys.stdout

        self.info("Logging Started")


    def __write__(self, text):
        self.output.write(text+'\n')
        self.output.flush()

    def __above_threshold__(self, level):
        for j in range(0,len(self.__levels__)-1):
            if self.__levels__[j] == self.__threshold__:
                break;
        for i in range(0,len(self.__levels__)-1):
            if self.__levels__[i] == level:
                break

        if i >= j:
            return True
        else:
            return False

    def set_threshold(self, threshold):
        self.__threshold__ = threshold

    def logging_format(self, format):
        """
        Set custom log format

        Valid directives: {time}, {datetime}, {date}, {level}, {text}

        Eg. '{time}: {level} - {text}'

        Args:
            format: string - custom format used for logging.
        """
        self.__format__ = format


    def log(self, text, log_level):
        """
        Logs text to file or standard output

        For custom logging levels. It is recommended to use provided the provided
        functions for logging various levels:
        debug(), info(), warning(), error(), and critical().

        Args:
            text: string - message to be displayed
            log_level: string - custom log level to be displayed
        """
        if self.__above_threshold__(log_level):
            now = datetime.now()
            self.__write__(self.__format__.format(time=now.time(), datetime=now,
                                                  date=date.today(),
                                                  level=log_level.upper(),
                                                  text=text
                                                 ))


    def debug(self, text):
        """
        Logs with "debug" level

        Detailed information (primarily used for debugging)

        Args:
            text: string - text to log
        """
        self.log(text,"debug")


    def info(self, text):
        """
        Logs with "info" level

        For general info relating to standard behaviour

        Args:
            text: string - text to log
        """
        self.log(text,"info")


    def warning(self, text):
        """
        Logs with "warning" level

        For errors that may change default behaviour

        Args:
            text: string - text to log
        """
        self.log(text,"warning")


    def error(self, text):
        """
        Logs with "error" level

        For errors that may alter the program's behaviour

        Args:
            text: string - text to log
        """
        self.log(text,"error")


    def critical(self, text):
        """
        Logs with "critical" level (this is bad)

        For errors that require the program to halt

        Args:
            text: string - text to log
        """
        self.log(text,"critical")


class FormatError(Exception):
    pass
