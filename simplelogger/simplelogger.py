# Simple Log - very simple logging
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

import datetime

class Logger(object):
    """Basic logging class"""
    
    def __init__(self):
        logging = False
    
    def start(self):
        global logging
        logging = True
        self.timestamp("Logging Started")

    def end(self, exit_code=0, message=''):
        if logging:
            print "Exited with status: {code}. {msg}\n".format(code=exit_code,
                                                               msg=message
                                                               )

    def stop(self):
        if logging:
            logging = False

    def timestamp(self, message):
        if logging:
            print "{timestamp}: {message}".format(message=message,
                                                  timestamp=datetime.datetime.now()
                                                  )