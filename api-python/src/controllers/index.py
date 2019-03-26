import io

import grpc
from flask import Blueprint, request, send_file, render_template, jsonify
from voluptuous import Schema as HTTPSchema, Invalid as SchemaInvalid, ALLOW_EXTRA, Required

from proto.ImageProcessRequest_pb2_grpc import ImageProcessingStub
from proto.ImageProcessRequest_pb2 import Image

bp = Blueprint(__name__, "index")


@bp.route("/")
def index():
    return render_template("index.html")


def call_external_image_processing(image_buf):
    channel = grpc.insecure_channel("localhost:50051")
    stub = ImageProcessingStub(channel)
    res_image = stub.ScanningDocument(Image(image=image_buf))
    return res_image.image


processing_form_schema = HTTPSchema({"filename": Required(str)})


@bp.route("/images", methods=["POST"])
def processing():
    try:
        form = processing_form_schema(request.form.to_dict())
        image = request.files["image"]
    except (SchemaInvalid, KeyError) as e:
        return (
            jsonify({"success": False, "status": "Form Invalid", "detail": str(e)}),
            400,
        )

    image_buf = image.read()
    res_image = call_external_image_processing(image_buf)
    return send_file(
        io.BytesIO(res_image),
        attachment_filename=form["filename"],
        mimetype="image/jpg",
    )
