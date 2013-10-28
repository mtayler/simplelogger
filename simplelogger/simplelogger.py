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
    Logger([stream[, threshold[, format[]]]) -> Logger object

    Provides a basic logging object.
    """
    def __init__(self, stream=None, threshold=None, format=None, log_errors=True):
        """
        Args:
            stream: string - full file path OR object - object implementing
                write and flush methods

            threshold: simplelogger constant - minimum level to log
                (eg simplelogger.INFO)

            format: string - custom logging format. See set_format for
                more details

            log_errors: boolean - set whether or not errors are logged
                to the stream object
        """

        self._levels = [DEBUG, INFO, WARNING, ERROR, CRITICAL]

        if threshold == None:
            self.set_threshold(INFO)
        else:
            self.set_threshold(threshold)

        if format is None:
            self._format = '{datetime}: {level}: {text}'
        else:
            self._format = format

        if stream is not None:
            if isinstance(stream, basestring):
                if not os.path.isdir(os.path.dirname(stream)):
                    os.makedirs(os.path.dirname(stream))

                try:
                    self._stream = open(stream, 'a+')

                except IOError as e:
                    raise IOError("Could not open {file}".format(file=e.filename))

                try:
                    self._stream.write('')
                    self._stream.flush()
                except AttributeError as e:
                    raise IOError("Cannot write to {file}.".format(file=e.filename))

            else:
                try:
                    stream.write('')
                    stream.flush()
                except AttributeError:
                    raise AttributeError("Provided stream object is invalid, must implement write and flush methods")
                except IOError:
                    raise IOError("Cannot write to provided stream object")

                self._stream = stream

            if log_errors:
                sys.stderr = self._stream

        else:
            self._stream = sys.__stdout__

        self._new("Logging Started")


    def _write(self, text):
        self._stream.write(text+'\n')
        self._stream.flush()

    def _above_threshold(self, level):
        if level in self._loggable_levels or level not in self._levels:
            return True
        else:
            return False

    def set_threshold(self, threshold):
        """
        Set the threshold for log entries

        Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
        """
        self._threshold = threshold

        for i in range(len(self._levels)):
            if self._levels[i] == self._threshold:
                break;

        self._loggable_levels = self._levels[i:]

    def set_format(self, format):
        """
        Set custom log format

        Valid directives: {time}, {datetime}, {date}, {level}, {text}

        Eg. '{time}: {level} - {text}'

        Args:
            format: string - custom format used for logging.
        """
        self._format = format

    def log(self, log_level, text):
        """
        Logs text to file or standard _output

        For custom logging levels. It is recommended to use provided
        the provided functions for logging various levels:
        debug(), info(), warning(), error(), and critical().
        
        Custom logging levels are always over the threshold, and therefore
        always logged.

        Args:
            text: string - message to be displayed
            log_level: string - custom log level to be displayed
        """
        if self._above_threshold(log_level):
            now = datetime.now()
            self._write(self._format.format(time=now.time(), datetime=now,
                                            date=date.today(),
                                            level=log_level.upper(),
                                            text=text
                                            ))

    def _new(self,text):
        now = datetime.now()
        self._write("\n"+self._format.format(time=now.time(), datetime=now,
                                            date=date.today(),
                                            level=self._threshold.upper(),
                                            text=text
                                            ))

    def debug(self, text):
        """
        Logs with "debug" level

        Detailed information (primarily used for debugging)

        Args:
            text: string - text to log
        """
        self.log(DEBUG,text)

    def info(self, text):
        """
        Logs with "info" level

        For general info relating to standard behaviour

        Args:
            text: string - text to log
        """
        self.log(INFO,text)

    def warning(self, text):
        """
        Logs with "warning" level

        For errors that may change default behaviour

        Args:
            text: string - text to log
        """
        self.log(WARNING,text)

    def error(self, text):
        """
        Logs with "error" level

        For errors that may alter the program's behaviour

        Args:
            text: string - text to log
        """
        self.log(ERROR,text)

    def critical(self, text):
        """
        Logs with "critical" level (this is bad)

        For errors that require the program to halt

        Args:
            text: string - text to log
        """
        self.log(CRITICAL,text)
