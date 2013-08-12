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

import datetime

class Logger(object):
    """Basic logging class"""
    
    def __init__(self):
        self.logging = False
    
    
    def start(self):
        """Begin logging"""
            
        self.logging = True
        self.timestamp("Logging Started")


    def end(self, exit_code=0, message=''):
        """
            Stops logging, logs provided exit code and optional message
        """
        if self.logging:
            self.logging = False
            print "Exited with status: {code}. {msg}\n".format(code=exit_code,
                                                               msg=message
                                                               )

    def halt(self):
        """Stop logging, doesn't print exit code"""
        
        if self.logging:
            self.logging = False
    
    
    def resume(self):
        """Resume logging"""
        
        self.logging = True


    def timestamp(self, message):
        """Logs with an added timestamp to the message"""
        if self.logging:
            print "{timestamp}: {message}".format(message=message,
                                                  timestamp=datetime.datetime.now()
                                                  )

    def exit_code(self, function, exit_code=0, message=''):
        """Logs provided exit code and optional message, continues logging"""
