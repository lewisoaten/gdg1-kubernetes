"""This is an example webserver to demonstrate K8s deployment."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import configparser
import logging
import sys
import socket

import memcache

mc = None


class GDGDemoRequestHandler(BaseHTTPRequestHandler):
    """Demo webserver that simply serves text."""

    def do_GET(self):
        """Handle a GET request with some simple text."""
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if not mc.get("count"):
            mc.set("count", 0)

        mc.incr("count")

        message = "Hello world"
        # message += " #{}".format(mc.get("count"))
        # message += " from {}!".format(socket.gethostname())
        message += "\n"

        self.wfile.write(bytes(message, "utf8"))


def run():
    """Run the webserver."""
    global mc
    mc = memcache.Client(
        ["{host}:{port}".format(**config['memcached'])],
        debug=0,
        )

    logging.info("Starting server...")
    server_address = (config['web']['address'], int(config['web']['port']))
    httpd = HTTPServer(server_address, GDGDemoRequestHandler)

    logging.info("Running server with address {}".format(server_address))
    httpd.serve_forever()


if __name__ == "__main__":
    # Iniitialise config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Initialise logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # Run our application
    run()
