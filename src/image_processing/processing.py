import uuid
import logging

import cv2
import numpy as np


def load_image_from_bytes(buf):
    """load from buffer (bytes) decode into and cv2's image
    """
    if not isinstance(buf, bytes):
        raise ValueError("Input must be bytes")
    arr = np.frombuffer(buf, dtype="uint8")
    return cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)


def image_to_buf(image):
    return cv2.imencode('.jpg', image)[1].tobytes()


def show_image(image):
    logging.warning("Using this function will block the program.")
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def document_scanner_process(image):
    """convert image to grayscale, blur it and find edge
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blured, 75, 200)
    return edged


def document_scanner_process_buffer(req_buf):
    image = load_image_from_bytes(req_buf)
    processed_image = document_scanner_process(image)
    resp_buf = image_to_buf(processed_image)
    return resp_buf
