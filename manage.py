from flask import Flask, make_response
from pulsar.apps import wsgi
import logging
from logging.config import fileConfig
import yaml
import os

#print(logging.Logger.manager.loggerDict)

with open(os.path.dirname(os.path.realpath(__file__)) + '/logging.yml') as f:
    conf = yaml.load(f)
    conf.setdefault('version', 1)
    logging.config.dictConfig(conf)

logger = logging.getLogger(__name__)


def Events():
    """Events flask app."""
    app = Flask(__name__)

    @app.route('/')
    def index():
        return make_response("Hello World", 200)

    @app.errorhandler(404)
    def not_found(e):
        return make_response("404 Page", 404)

    return app


class Site(wsgi.LazyWsgi):

    def setup(self, environ=None):
        app = Events()
        return wsgi.WsgiHandler((wsgi.wait_for_body_middleware,
                                 wsgi.middleware_in_executor(app)))


def server(**kwargs):
    return wsgi.WSGIServer(Site(), **kwargs)


if __name__ == '__main__':  # pragma    nocover
    server().start()
