from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import logging

import grpc
from flask import Flask, jsonify

from src.controllers.index import bp as bp_index
from src.system.exception import ServiceUnavailable


def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

    app.register_blueprint(bp_index)

    @app.after_request
    def nocache_header(r):
        """Support add no cache header to response data
        """
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        return r

    @app.errorhandler(ServiceUnavailable)
    def service_unavailable_handle(e):
        """Exception hanlder when an external service not available
        """
        return jsonify({"success": False, "message": "Service unavailable."}) , 400
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
