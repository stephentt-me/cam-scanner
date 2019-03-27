import uuid
import logging
from pathlib import Path

import src.processing as processing
from proto.ImageProcessRequest_pb2 import Image

this_dir = Path(__file__).resolve().parent


def reproduce_buffer_message():
    with open(str(this_dir / "4.jpg"), "rb") as f:
        data = f.read()
    return Image(image=data)

