# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/data/transformation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import user_defined_function_pb2 as tecton__proto_dot_args_dot_user__defined__function__pb2
from tecton_proto.data import fco_metadata_pb2 as tecton__proto_dot_data_dot_fco__metadata__pb2
from tecton_proto.args import transformation_pb2 as tecton__proto_dot_args_dot_transformation__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tecton_proto/data/transformation.proto\x12\x11tecton_proto.data\x1a-tecton_proto/args/user_defined_function.proto\x1a$tecton_proto/data/fco_metadata.proto\x1a&tecton_proto/args/transformation.proto\x1a\x1ctecton_proto/common/id.proto\"\xbe\x02\n\x0eTransformation\x12\x44\n\x11transformation_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10transformationId\x12\x41\n\x0c\x66\x63o_metadata\x18\x02 \x01(\x0b\x32\x1e.tecton_proto.data.FcoMetadataR\x0b\x66\x63oMetadata\x12V\n\x13transformation_mode\x18\x03 \x01(\x0e\x32%.tecton_proto.args.TransformationModeR\x12transformationMode\x12K\n\ruser_function\x18\x04 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x0cuserFunctionB\x13\n\x0f\x63om.tecton.dataP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.data.transformation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.dataP\001'
  _TRANSFORMATION._serialized_start=217
  _TRANSFORMATION._serialized_end=535
# @@protoc_insertion_point(module_scope)
