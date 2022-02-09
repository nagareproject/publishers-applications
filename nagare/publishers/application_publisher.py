# Encoding: utf-8

# --
# Copyright (c) 2008-2022 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from functools import partial
from nagare.server import http_publisher


class Publisher(http_publisher.Publisher):
    CONFIG_SPEC = dict(
        http_publisher.Publisher.CONFIG_SPEC,
        has_multi_processes='boolean',
        has_multi_threads='boolean'
    )

    def __init__(self, name, dist, has_multi_processes, has_multi_threads, **config):
        super(Publisher, self).__init__(
            name, dist,
            has_multi_processes=has_multi_processes, has_multi_threads=has_multi_threads,
            **config
        )

        self.has_multi_processes = has_multi_processes
        self.has_multi_threads = has_multi_threads

    def _serve(self, app, services_service, **params):
        return partial(services_service, self.start_handle_request, app)
