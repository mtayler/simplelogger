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
import datetime
import os

class Logger(object):
    """Basic logging class"""

    def __init__(self, logging_file=None, start_on_create=False):
        if start_on_create:
            self.logging = True
        elif not start_on_create:
            self.logging = False
        else:
            raise TypeError("start_on_create must be boolean")

        if logging_file:
            if not os.path.exists(os.path.dirname(logging_file)):
                os.makedirs(logging_file)

            self.output = open(logging_file, 'a+')
            sys.stderr = open(logging_file, 'a+')

        else:
            self.output = sys.stdout


    def _write(self,text):
        self.output.write(text+'\n')
        self.output.flush()


    def start(self):
        """Begin logging"""

        self.logging = True
        self.timestamp("Logging Started")


    def end(self, exit_code=0, message=''):
        """Stops logging, logs provided exit code and optional message"""

        if self.logging:
            self.logging = False
            self._write("Exited with status: {code}. {msg}\n".format(code=exit_code,
                                                               msg=message
                                                               ))
            sys.stderr.close()
            sys.stderr = sys.__stderr__


    def halt(self):
        """Stop logging, doesn't print exit code"""

        if self.logging:
            self.timestamp("Logging halted")
            self.logging = False


    def resume(self):
        """Resume logging"""

        self.logging = True
        self.timestamp("Logging resumed")


    def timestamp(self, message):
        """Logs with an added timestamp to the message"""
        if self.logging:
            self._write("{timestamp}: {message}".format(message=message,
                                                  timestamp=datetime.datetime.now()
                                                  ))


    def exit_code(self, function, exit_code=0, message=''):
        """Logs provided exit code and optional message, continues logging"""
        #TODO
