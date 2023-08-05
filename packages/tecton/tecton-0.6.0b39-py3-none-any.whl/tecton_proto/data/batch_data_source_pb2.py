# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/data/batch_data_source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.args import data_source_pb2 as tecton__proto_dot_args_dot_data__source__pb2
from tecton_proto.args import data_source_config_pb2 as tecton__proto_dot_args_dot_data__source__config__pb2
from tecton_proto.args import user_defined_function_pb2 as tecton__proto_dot_args_dot_user__defined__function__pb2
from tecton_proto.common import spark_schema_pb2 as tecton__proto_dot_common_dot_spark__schema__pb2
from tecton_proto.data import hive_metastore_pb2 as tecton__proto_dot_data_dot_hive__metastore__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)tecton_proto/data/batch_data_source.proto\x12\x11tecton_proto.data\x1a\x1egoogle/protobuf/duration.proto\x1a$tecton_proto/args/diff_options.proto\x1a#tecton_proto/args/data_source.proto\x1a*tecton_proto/args/data_source_config.proto\x1a-tecton_proto/args/user_defined_function.proto\x1a&tecton_proto/common/spark_schema.proto\x1a&tecton_proto/data/hive_metastore.proto\"T\n\x19TimestampColumnProperties\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x16\n\x06\x66ormat\x18\x02 \x01(\tR\x06\x66ormat\"\x9a\x01\n\x1cSparkBatchDataSourceFunction\x12\x42\n\x08\x66unction\x18\x01 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x08\x66unction\x12\x36\n\x17supports_time_filtering\x18\x02 \x01(\x08R\x15supportsTimeFiltering\"\xd3\x07\n\x0f\x42\x61tchDataSource\x12G\n\nhive_table\x18\x01 \x01(\x0b\x32&.tecton_proto.data.HiveTableDataSourceH\x00R\thiveTable\x12\x37\n\x04\x66ile\x18\x08 \x01(\x0b\x32!.tecton_proto.data.FileDataSourceH\x00R\x04\x66ile\x12H\n\x0bredshift_db\x18\x0b \x01(\x0b\x32%.tecton_proto.data.RedshiftDataSourceH\x00R\nredshiftDb\x12\x46\n\tsnowflake\x18\x0c \x01(\x0b\x32&.tecton_proto.data.SnowflakeDataSourceH\x00R\tsnowflake\x12n\n\x1aspark_data_source_function\x18\r \x01(\x0b\x32/.tecton_proto.data.SparkBatchDataSourceFunctionH\x00R\x17sparkDataSourceFunction\x12\x43\n\x0cspark_schema\x18\t \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0bsparkSchema\x12l\n\x1btimestamp_column_properties\x18\x04 \x01(\x0b\x32,.tecton_proto.data.TimestampColumnPropertiesR\x19timestampColumnProperties\x12\x41\n\x0c\x62\x61tch_config\x18\x05 \x01(\x0b\x32\x1e.tecton_proto.args.BatchConfigR\x0b\x62\x61tchConfig\x12\x32\n\x15\x64\x61te_partition_column\x18\x06 \x01(\tR\x13\x64\x61tePartitionColumn\x12h\n\x1a\x64\x61tetime_partition_columns\x18\x07 \x03(\x0b\x32*.tecton_proto.data.DatetimePartitionColumnR\x18\x64\x61tetimePartitionColumns\x12X\n\x14raw_batch_translator\x18\n \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x12rawBatchTranslator\x12\x38\n\ndata_delay\x18\x0e \x01(\x0b\x32\x19.google.protobuf.DurationR\tdataDelayB\x0e\n\x0c\x62\x61tch_sourceJ\x04\x08\x02\x10\x03\"\x88\x02\n\x0e\x46ileDataSource\x12\x10\n\x03uri\x18\x01 \x02(\tR\x03uri\x12?\n\x06\x66ormat\x18\x02 \x02(\x0e\x32\'.tecton_proto.data.FileDataSourceFormatR\x06\x66ormat\x12\x33\n\x16\x63onvert_to_glue_format\x18\x04 \x01(\x08R\x13\x63onvertToGlueFormat\x12\x1d\n\nschema_uri\x18\x05 \x01(\tR\tschemaUri\x12I\n\x0fschema_override\x18\x06 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0eschemaOverrideJ\x04\x08\x03\x10\x04\"\x88\x01\n\x17\x44\x61tetimePartitionColumn\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x02(\tR\ncolumnName\x12#\n\rformat_string\x18\x02 \x02(\tR\x0c\x66ormatString\x12\'\n\x0fminimum_seconds\x18\x03 \x02(\x03R\x0eminimumSeconds\"\xc5\x01\n\x12RedshiftDataSource\x12\x1a\n\x08\x65ndpoint\x18\x01 \x01(\tR\x08\x65ndpoint\x12\x1d\n\ncluster_id\x18\x02 \x01(\tR\tclusterId\x12\x1a\n\x08\x64\x61tabase\x18\x03 \x01(\tR\x08\x64\x61tabase\x12\x16\n\x05table\x18\x04 \x01(\tH\x00R\x05table\x12\x1d\n\x05query\x18\x06 \x01(\tB\x05\x92M\x02\x18\x03H\x00R\x05query\x12\x17\n\x07temp_s3\x18\x05 \x01(\tR\x06tempS3B\x08\n\x06source\"g\n\x13SnowflakeDataSource\x12P\n\rsnowflakeArgs\x18\x01 \x01(\x0b\x32*.tecton_proto.args.SnowflakeDataSourceArgsR\rsnowflakeArgs*~\n\x14\x46ileDataSourceFormat\x12 \n\x1c\x46ILE_DATA_SOURCE_FORMAT_JSON\x10\x00\x12#\n\x1f\x46ILE_DATA_SOURCE_FORMAT_PARQUET\x10\x01\x12\x1f\n\x1b\x46ILE_DATA_SOURCE_FORMAT_CSV\x10\x02\x42\x13\n\x0f\x63om.tecton.dataP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.data.batch_data_source_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.dataP\001'
  _REDSHIFTDATASOURCE.fields_by_name['query']._options = None
  _REDSHIFTDATASOURCE.fields_by_name['query']._serialized_options = b'\222M\002\030\003'
  _FILEDATASOURCEFORMAT._serialized_start=2278
  _FILEDATASOURCEFORMAT._serialized_end=2404
  _TIMESTAMPCOLUMNPROPERTIES._serialized_start=342
  _TIMESTAMPCOLUMNPROPERTIES._serialized_end=426
  _SPARKBATCHDATASOURCEFUNCTION._serialized_start=429
  _SPARKBATCHDATASOURCEFUNCTION._serialized_end=583
  _BATCHDATASOURCE._serialized_start=586
  _BATCHDATASOURCE._serialized_end=1565
  _FILEDATASOURCE._serialized_start=1568
  _FILEDATASOURCE._serialized_end=1832
  _DATETIMEPARTITIONCOLUMN._serialized_start=1835
  _DATETIMEPARTITIONCOLUMN._serialized_end=1971
  _REDSHIFTDATASOURCE._serialized_start=1974
  _REDSHIFTDATASOURCE._serialized_end=2171
  _SNOWFLAKEDATASOURCE._serialized_start=2173
  _SNOWFLAKEDATASOURCE._serialized_end=2276
# @@protoc_insertion_point(module_scope)
