# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/dataobs/metric.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tecton_proto/dataobs/metric.proto\x12\x14tecton_proto.dataobs\x1a\x1fgoogle/protobuf/timestamp.proto\"F\n\x0bMetricValue\x12!\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\tR\x0b\x66\x65\x61tureName\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\xa4\x02\n\x0fMetricDataPoint\x12J\n\x13interval_start_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11intervalStartTime\x12\x46\n\rmetric_values\x18\x02 \x03(\x0b\x32!.tecton_proto.dataobs.MetricValueR\x0cmetricValues\x12\x34\n\x16materialization_run_id\x18\x03 \x01(\tR\x14materializationRunId\x12G\n materialization_task_attempt_url\x18\x04 \x01(\tR\x1dmaterializationTaskAttemptUrl*\xcb\x01\n\nMetricType\x12\x17\n\x13METRIC_TYPE_UNKNOWN\x10\x00\x12\x12\n\x0e\x43OUNT_DISTINCT\x10\x01\x12\x0e\n\nCOUNT_ROWS\x10\x02\x12\x0f\n\x0b\x43OUNT_NULLS\x10\x03\x12\x0f\n\x0b\x43OUNT_ZEROS\x10\n\x12\r\n\tAVG_VALUE\x10\x04\x12\r\n\tMAX_VALUE\x10\x05\x12\r\n\tMIN_VALUE\x10\x06\x12\x0e\n\nVAR_SAMPLE\x10\x07\x12\x11\n\rSTDDEV_SAMPLE\x10\x08\x12\x0e\n\nAVG_LENGTH\x10\t*4\n\x11QueryMetricStatus\x12\x1f\n\x1bQUERY_METRIC_STATUS_UNKNOWN\x10\x00\x42\x16\n\x12\x63om.tecton.dataobsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.dataobs.metric_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.tecton.dataobsP\001'
  _METRICTYPE._serialized_start=460
  _METRICTYPE._serialized_end=663
  _QUERYMETRICSTATUS._serialized_start=665
  _QUERYMETRICSTATUS._serialized_end=717
  _METRICVALUE._serialized_start=92
  _METRICVALUE._serialized_end=162
  _METRICDATAPOINT._serialized_start=165
  _METRICDATAPOINT._serialized_end=457
# @@protoc_insertion_point(module_scope)
