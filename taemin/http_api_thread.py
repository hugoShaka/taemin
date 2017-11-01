#!/usr/bin/env python3
# -*- coding: utf8 -*-

from threading import Thread
from flask import Flask

class HttpApiThread(Thread):
    def __init__(self, endpoints):
        Thread.__init__(self)
        self.endpoints = endpoints
        self._continue = false
        self.app = Flask(__name__)

    def update_app(self):
        for endpoint in endpoints:
            complete_route = endpoint.generate_route()
            endpoint.callback = self.app.route(complete_route, endpoint.methods)(endpoint.callback)
        pass

    def set_endpoints(self, endpoints):
        self.endpoints = endpoints

    def run(self):
        self._continue = True
        """Some gevent black magic to expose the app""""
        self.app.run()

    def stop(self):
        self._continue = False
