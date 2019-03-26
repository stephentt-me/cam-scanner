import uuid
import logging
from pathlib import Path

import src.image_processing.processing as processing
from src.proto.ImageProcessRequest_pb2 import Image

this_dir = Path(__file__).resolve().parent


def reproduce_buffer_message():
    with open(str(this_dir / "4.jpg"), "rb") as f:
        data = f.read()
    return Image(image=data)


def test_document_scanner_process_buffer():
    request = reproduce_buffer_message()
    resp_buf = processing.document_scanner_process_buffer(request.image)  # pylint: disable=no-member


if __name__ == "__main__":
    test_document_scanner_process_buffer()
