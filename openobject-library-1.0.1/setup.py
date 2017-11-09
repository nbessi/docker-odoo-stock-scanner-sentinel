# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenObject Library
#    Copyright (C) 2009-2012 Syleam (<http://syleam.fr>). Christophe Chauvet
#                  All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

"""
SetupTools configuration file
"""
from setuptools import setup
import os

if os.path.exists("README.rst"):
    import codecs
    LONG_DESCRIPTION = codecs.open('README.rst', "r", "utf-8").read()
else:
    LONG_DESCRIPTION = "port of unmaintained openobject library v1.01"

def find_packages(base):
    """Find all package for this application

    :param base: root path of source.
    :return: Returns a list of subpackages suitable for setup() packages keyword.
    """
    ret = [base]
    for path in os.listdir(base):
        if path.startswith('.'):
            continue
        full_path = os.path.join(base, path)
        if os.path.isdir(full_path):
            ret += find_packages(full_path)
    return ret



setup(
    name='openobject-library',
    version='1.0.1',
    description=LONG_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Mr. Chauvet',
    author_email='none',
    license='GPLv3',
    packages=find_packages('oobjlib'))

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
