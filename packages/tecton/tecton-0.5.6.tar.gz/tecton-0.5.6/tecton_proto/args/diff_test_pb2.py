# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/diff_test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tecton_proto/args/diff_test.proto\x12\x11tecton_proto.args\x1a\x1ctecton_proto/common/id.proto\x1a\"tecton_proto/args/basic_info.proto\x1a$tecton_proto/args/diff_options.proto\"?\n\x0b\x44iffTestFoo\x12\x17\n\x07\x66ield_a\x18\x01 \x01(\tR\x06\x66ieldA\x12\x17\n\x07\x66ield_b\x18\x02 \x01(\tR\x06\x66ieldB\"\xb3\x07\n\x0c\x44iffTestArgs\x12\x39\n\x0ctest_args_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\ntestArgsId\x12\x30\n\x04info\x18\x02 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoR\x04info\x12\x42\n\tnew_field\x18\x03 \x01(\x0b\x32\x1e.tecton_proto.args.DiffTestFooB\x05\x92M\x02\x08\x03R\x08newField\x12\x42\n\told_field\x18\x04 \x01(\x0b\x32\x1e.tecton_proto.args.DiffTestFooB\x05\x92M\x02\x08\x04R\x08oldField\x12*\n\rpassive_field\x18\x05 \x01(\tB\x05\x92M\x02\x08\x05R\x0cpassiveField\x12\x45\n\x1brecreate_suppressable_field\x18\x06 \x01(\tB\x05\x92M\x02\x08\x06R\x19recreateSuppressableField\x12z\n\"recreate_suppressable_nested_field\x18\x08 \x01(\x0b\x32&.tecton_proto.args.DiffTestNestedInnerB\x05\x92M\x02\x08\x06R\x1frecreateSuppressableNestedField\x12q\n2recreate_suppressable_invalidate_checkpoints_field\x18\t \x01(\tB\x05\x92M\x02\x08\x07R.recreateSuppressableInvalidateCheckpointsField\x12\xa6\x01\n9recreate_suppressable_invalidate_checkpoints_nested_field\x18\n \x01(\x0b\x32&.tecton_proto.args.DiffTestNestedInnerB\x05\x92M\x02\x08\x07R4recreateSuppressableInvalidateCheckpointsNestedField\x12\x61\n*recreate_suppressable_restart_stream_field\x18\x0b \x01(\tB\x05\x92M\x02\x08\x08R&recreateSuppressableRestartStreamField\x12@\n\x1cunannotated_needing_recreate\x18\x07 \x01(\tR\x1aunannotatedNeedingRecreate\"\x98\x02\n\x13\x44iffTestNestedInner\x12*\n\rinplace_field\x18\x01 \x01(\tB\x05\x92M\x02\x08\x01R\x0cinplaceField\x12\x45\n\x1brecreate_suppressable_field\x18\x02 \x01(\tB\x05\x92M\x02\x08\x06R\x19recreateSuppressableField\x12\x61\n*recreate_suppressable_restart_stream_field\x18\x04 \x01(\tB\x05\x92M\x02\x08\x08R&recreateSuppressableRestartStreamField\x12+\n\x11unannotated_field\x18\x03 \x01(\tR\x10unannotatedField\"Q\n\x13\x44iffTestNestedOuter\x12:\n\x04\x61rgs\x18\x01 \x01(\x0b\x32\x1f.tecton_proto.args.DiffTestArgsB\x05\x92M\x02\x08\x01R\x04\x61rgsB\x13\n\x0f\x63om.tecton.argsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.args.diff_test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.argsP\001'
  _DIFFTESTARGS.fields_by_name['new_field']._options = None
  _DIFFTESTARGS.fields_by_name['new_field']._serialized_options = b'\222M\002\010\003'
  _DIFFTESTARGS.fields_by_name['old_field']._options = None
  _DIFFTESTARGS.fields_by_name['old_field']._serialized_options = b'\222M\002\010\004'
  _DIFFTESTARGS.fields_by_name['passive_field']._options = None
  _DIFFTESTARGS.fields_by_name['passive_field']._serialized_options = b'\222M\002\010\005'
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_field']._options = None
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_field']._serialized_options = b'\222M\002\010\006'
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_nested_field']._options = None
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_nested_field']._serialized_options = b'\222M\002\010\006'
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_invalidate_checkpoints_field']._options = None
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_invalidate_checkpoints_field']._serialized_options = b'\222M\002\010\007'
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_invalidate_checkpoints_nested_field']._options = None
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_invalidate_checkpoints_nested_field']._serialized_options = b'\222M\002\010\007'
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_restart_stream_field']._options = None
  _DIFFTESTARGS.fields_by_name['recreate_suppressable_restart_stream_field']._serialized_options = b'\222M\002\010\010'
  _DIFFTESTNESTEDINNER.fields_by_name['inplace_field']._options = None
  _DIFFTESTNESTEDINNER.fields_by_name['inplace_field']._serialized_options = b'\222M\002\010\001'
  _DIFFTESTNESTEDINNER.fields_by_name['recreate_suppressable_field']._options = None
  _DIFFTESTNESTEDINNER.fields_by_name['recreate_suppressable_field']._serialized_options = b'\222M\002\010\006'
  _DIFFTESTNESTEDINNER.fields_by_name['recreate_suppressable_restart_stream_field']._options = None
  _DIFFTESTNESTEDINNER.fields_by_name['recreate_suppressable_restart_stream_field']._serialized_options = b'\222M\002\010\010'
  _DIFFTESTNESTEDOUTER.fields_by_name['args']._options = None
  _DIFFTESTNESTEDOUTER.fields_by_name['args']._serialized_options = b'\222M\002\010\001'
  _DIFFTESTFOO._serialized_start=160
  _DIFFTESTFOO._serialized_end=223
  _DIFFTESTARGS._serialized_start=226
  _DIFFTESTARGS._serialized_end=1173
  _DIFFTESTNESTEDINNER._serialized_start=1176
  _DIFFTESTNESTEDINNER._serialized_end=1456
  _DIFFTESTNESTEDOUTER._serialized_start=1458
  _DIFFTESTNESTEDOUTER._serialized_end=1539
# @@protoc_insertion_point(module_scope)
