import logging
import time
import concurrent.futures

import grpc
from grpc_reflection.v1alpha import reflection

from proto.ImageProcessRequest_pb2_grpc import add_ImageProcessingServicer_to_server
from proto.ImageProcessRequest_pb2 import DESCRIPTOR
from src.servicer import Servicer

SERVER_PORT = "[::]:50051"


def serve():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Server started")

    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    add_ImageProcessingServicer_to_server(Servicer(), server)

    # Enable server reflection
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['ImageProcessing'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(SERVER_PORT)
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
