import os
import logging

import grpc
from flask import Flask, jsonify

from src.web.controllers.index import bp as bp_index
from src.web.system.exception import ServiceUnavailable


def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

    app.register_blueprint(bp_index)

    @app.errorhandler(ServiceUnavailable)
    def service_unavailable_handle(e):
        return jsonify({"success": False, "message": "Service unavailable."}) , 400
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)
