import logging
from proto.ImageProcessRequest_pb2 import Image

from proto.ImageProcessRequest_pb2_grpc import ImageProcessingServicer
import src.processing as processing


class Servicer(ImageProcessingServicer):
    def ScanningDocument(self, request, context):
        logging.debug("Got a request")
        res_buf = processing.document_scanner_process_buffer(request.image)
        return Image(image=res_buf)
