# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/basic_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.args import version_constraints_pb2 as tecton__proto_dot_args_dot_version__constraints__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"tecton_proto/args/basic_info.proto\x12\x11tecton_proto.args\x1a$tecton_proto/args/diff_options.proto\x1a+tecton_proto/args/version_constraints.proto\"\x8b\x02\n\tBasicInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x05\x92M\x02\x08\x01R\x0b\x64\x65scription\x12\x1b\n\x05owner\x18\x06 \x01(\tB\x05\x92M\x02\x08\x01R\x05owner\x12\"\n\x06\x66\x61mily\x18\x04 \x01(\tB\n\x92M\x02\x08\x01\x82}\x02\x10\x04R\x06\x66\x61mily\x12\x41\n\x04tags\x18\x05 \x03(\x0b\x32&.tecton_proto.args.BasicInfo.TagsEntryB\x05\x92M\x02\x08\x01R\x04tags\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01J\x04\x08\x03\x10\x04\x42\x13\n\x0f\x63om.tecton.argsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.args.basic_info_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.argsP\001'
  _BASICINFO_TAGSENTRY._options = None
  _BASICINFO_TAGSENTRY._serialized_options = b'8\001'
  _BASICINFO.fields_by_name['description']._options = None
  _BASICINFO.fields_by_name['description']._serialized_options = b'\222M\002\010\001'
  _BASICINFO.fields_by_name['owner']._options = None
  _BASICINFO.fields_by_name['owner']._serialized_options = b'\222M\002\010\001'
  _BASICINFO.fields_by_name['family']._options = None
  _BASICINFO.fields_by_name['family']._serialized_options = b'\222M\002\010\001\202}\002\020\004'
  _BASICINFO.fields_by_name['tags']._options = None
  _BASICINFO.fields_by_name['tags']._serialized_options = b'\222M\002\010\001'
  _BASICINFO._serialized_start=141
  _BASICINFO._serialized_end=408
  _BASICINFO_TAGSENTRY._serialized_start=347
  _BASICINFO_TAGSENTRY._serialized_end=402
# @@protoc_insertion_point(module_scope)
