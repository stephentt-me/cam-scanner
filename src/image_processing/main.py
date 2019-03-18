import logging
import time
import concurrent.futures

import grpc

import cv2

from src.proto.ImageProcessRequest_pb2_grpc import (
    ImageProcessingServicer,
    add_ImageProcessingServicer_to_server,
)
from src.proto.ImageProcessRequest_pb2 import Image
import src.image_processing.processing as processing
from src.image_processing.hearbeat import make_heartbeat

SERVER_PORT = "[::]:50051"


class Servicer(ImageProcessingServicer):
    def ScanningDocument(self, request, context):
        logging.debug("Got a request")
        res_buf = processing.document_scanner_process_buffer(request.image)
        return Image(image=res_buf)


def serve():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Server started")

    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    add_ImageProcessingServicer_to_server(Servicer(), server)
    server.add_insecure_port(SERVER_PORT)
    server.start()
    try:
        while True:
            make_heartbeat(SERVER_PORT)
            time.sleep(3)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
