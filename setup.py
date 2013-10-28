#!/usr/bin/env python
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

from distutils.core import setup

__version__ = '1.4.9'

readme = open('README.rst').read(),

setup(name='SimpleLogger',
      version=__version__,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
          ],
      packages=['simplelogger'],
      description='Simple Logging Utility',
      long_description = readme,
      author='Tayler Mulligan',
      author_email='mulligantayler@gmail.com',
      url='https://github.com/tamul/simplelogger',
      license='GNU GPL v3'
     )
