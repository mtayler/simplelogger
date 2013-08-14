# Simple Logger - very simple logging
# Copyright (C) 2013  Tayler Mulligan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

from datetime import datetime, date, time

class Logger(object):
    """Basic logging class"""

    def __init__(self, log_file=None, default_log_level=None, _format_string_=None):
        """
        Construct new logger

        self.Logger(default_log_level='info', log_file=None)

        default_log_level sets the default logging level
        log_file sets the file to log to if provided. Default is standard output
        """
        if default_log_level == None:
            self._default_log_level_ = 'info'
        else:
            self._default_log_level_ = default_log_level

        if _format_string_ == None:
            self._format_string_ = '{datetime}: {level}: {text}'
        else:
            self._format_string_ = _format_string_

        if log_file:
            if '/' in log_file or '\\' in log_file:
                if not os.path.exists(os.path.dirname(log_file)):
                    os.makedirs(os.path.dirname(log_file))
            else:
                current_dir = os.path.dirname(__file__)
                log_file = os.path.join(current_dir, log_file)


            try:
                self.output = open(log_file, 'a+')
                sys.stderr = open(log_file, 'a+')
            except IOError as e:
                raise IOError("Could not open {log_file}".format(log_file=e.filename))
        else:
            self.output = sys.stdout

        self.log("Logging Started")


    def _write(self, text):
        self.output.write(text+'\n')
        self.output.flush()


    def log_format(self, _format_string_):
        """
        Set custom log format

        Valid format directives:
        {time}, {datetime}, {date}, {level}, and {text}
        """
        self._format_string_ = _format_string_




    def log(self, text, log_level=None):
        """
        Logs text to file or standard output


        Defaults to Logger object's default level, for other standard levels, it is
        recommended to use provided the provided functions for logging various levels:
        debug(), info(), warning(), error(), and critical().

        Can be provided with custom logging levels.
        """
        if log_level is None:
            log_level = self._default_log_level_

        now = datetime.now()
        self._write(self._format_string_.format(time=now.time(), datetime=now,
                                           date=date.today(), level=log_level.upper(),
                                           text=text
                                          ))


    def end(self, exit_code=0,text=''):
        """Stops logging, logs provided exit code and optional text"""
        self.logging = False
        self._write("Exited with status: {code}. {msg}\n".format(code=exit_code,
                                                                 msg=text
                                                                ))
        sys.stderr.close()
        sys.stderr = sys.__stderr__


    def exit_code(self, function, exit_code=0, text=''):
        """Logs provided exit code and optional text, continues logging"""
        #TODO
        raise NotImplementedError("Function not yet implemented")


    def debug(self, text):
        """
        Logs with "debug" level

        Detailed information (primarily used for debugging)
        """
        self.log(text,"debug")


    def info(self, text):
       """
       Logs with "info" level

       For general info relating to standard behaviour
       """
       self.log(text,"info")


    def warning(self, text):
        """
        Logs with "warning" level

        For errors that may change default behaviour
        """
        self.log(text,"warning")


    def error(self, text):
        """
        Logs with "error" level

        For errors that may alter the program's behaviour
        """
        self.log(text,"error")


    def critical(self, text):
        """
        Logs with "critical" level (this is bad)

        For errors that require the program to halt
        """
        self.log(text,"critical")


class FormatError(Exception):
    pass
