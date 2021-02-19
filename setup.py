# Encoding: utf-8

# --
# Copyright (c) 2008-2020 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as long_description:
    LONG_DESCRIPTION = long_description.readline().rstrip()

setup(
    name='nagare-publishers-application',
    author='Net-ng',
    author_email='alain.poirier@net-ng.com',
    description='Raw WSGI application publisher',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords='',
    url='https://github.com/nagareproject/publishers-application',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=('nagare-server-http',),
    entry_points='''
        [nagare.publishers]
        application = nagare.publishers.application_publisher:Publisher
    '''
)
