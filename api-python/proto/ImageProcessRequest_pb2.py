# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ImageProcessRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ImageProcessRequest.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19ImageProcessRequest.proto\"\x16\n\x05Image\x12\r\n\x05image\x18\x01 \x01(\x0c\x32\x37\n\x0fImageProcessing\x12$\n\x10ScanningDocument\x12\x06.Image\x1a\x06.Image\"\x00\x62\x06proto3')
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='Image.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'ImageProcessRequest_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  ))
_sym_db.RegisterMessage(Image)



_IMAGEPROCESSING = _descriptor.ServiceDescriptor(
  name='ImageProcessing',
  full_name='ImageProcessing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=53,
  serialized_end=108,
  methods=[
  _descriptor.MethodDescriptor(
    name='ScanningDocument',
    full_name='ImageProcessing.ScanningDocument',
    index=0,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_IMAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGEPROCESSING)

DESCRIPTOR.services_by_name['ImageProcessing'] = _IMAGEPROCESSING

# @@protoc_insertion_point(module_scope)