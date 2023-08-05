# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/data_source.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from tecton_proto.args import data_source_config_pb2 as tecton__proto_dot_args_dot_data__source__config__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.args import user_defined_function_pb2 as tecton__proto_dot_args_dot_user__defined__function__pb2
from tecton_proto.common import spark_schema_pb2 as tecton__proto_dot_common_dot_spark__schema__pb2
from tecton_proto.args import version_constraints_pb2 as tecton__proto_dot_args_dot_version__constraints__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#tecton_proto/args/data_source.proto\x12\x11tecton_proto.args\x1a\x1egoogle/protobuf/duration.proto\x1a*tecton_proto/args/data_source_config.proto\x1a$tecton_proto/args/diff_options.proto\x1a-tecton_proto/args/user_defined_function.proto\x1a&tecton_proto/common/spark_schema.proto\x1a+tecton_proto/args/version_constraints.proto\"\xa0\x01\n\x1b\x44\x61tetimePartitionColumnArgs\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x1a\n\x08\x64\x61tepart\x18\x02 \x01(\tR\x08\x64\x61tepart\x12\x1f\n\x0bzero_padded\x18\x03 \x01(\x08R\nzeroPadded\x12#\n\rformat_string\x18\x04 \x01(\tR\x0c\x66ormatString\"\xcd\x01\n\x19\x42\x61tchDataSourceCommonArgs\x12\'\n\x0ftimestamp_field\x18\x01 \x01(\tR\x0etimestampField\x12M\n\x0epost_processor\x18\x02 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\rpostProcessor\x12\x38\n\ndata_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\tdataDelay\"\xa0\x02\n\x1aStreamDataSourceCommonArgs\x12\'\n\x0ftimestamp_field\x18\x01 \x01(\tR\x0etimestampField\x12U\n\x19watermark_delay_threshold\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x17watermarkDelayThreshold\x12M\n\x0epost_processor\x18\x03 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\rpostProcessor\x12\x33\n\x15\x64\x65\x64uplication_columns\x18\x04 \x03(\tR\x14\x64\x65\x64uplicationColumns\"\x91\x04\n\x12HiveDataSourceArgs\x12\x14\n\x05table\x18\x01 \x01(\tR\x05table\x12\x1a\n\x08\x64\x61tabase\x18\x02 \x01(\tR\x08\x64\x61tabase\x12\x32\n\x15\x64\x61te_partition_column\x18\x03 \x01(\tR\x13\x64\x61tePartitionColumn\x12\x39\n\x15timestamp_column_name\x18\x04 \x01(\tB\x05\x82}\x02\x10\x03R\x13timestampColumnName\x12)\n\x10timestamp_format\x18\x05 \x01(\tR\x0ftimestampFormat\x12l\n\x1a\x64\x61tetime_partition_columns\x18\x07 \x03(\x0b\x32..tecton_proto.args.DatetimePartitionColumnArgsR\x18\x64\x61tetimePartitionColumns\x12_\n\x14raw_batch_translator\x18\t \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x12rawBatchTranslator\x12T\n\x0b\x63ommon_args\x18\n \x01(\x0b\x32,.tecton_proto.args.BatchDataSourceCommonArgsB\x05\x82}\x02\x08\x05R\ncommonArgsJ\x04\x08\x06\x10\x07J\x04\x08\x08\x10\t\"\x95\x04\n\x12\x46ileDataSourceArgs\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12\x1f\n\x0b\x66ile_format\x18\x02 \x01(\tR\nfileFormat\x12\x33\n\x16\x63onvert_to_glue_format\x18\x03 \x01(\x08R\x13\x63onvertToGlueFormat\x12_\n\x14raw_batch_translator\x18\x04 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x12rawBatchTranslator\x12$\n\nschema_uri\x18\x05 \x01(\tB\x05\x92M\x02\x08\x01R\tschemaUri\x12\x39\n\x15timestamp_column_name\x18\x06 \x01(\tB\x05\x82}\x02\x10\x03R\x13timestampColumnName\x12)\n\x10timestamp_format\x18\x07 \x01(\tR\x0ftimestampFormat\x12I\n\x0fschema_override\x18\t \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0eschemaOverride\x12Y\n\x0b\x63ommon_args\x18\n \x01(\x0b\x32,.tecton_proto.args.BatchDataSourceCommonArgsB\n\x82}\x02\x08\x05\x92M\x02\x10\x01R\ncommonArgsJ\x04\x08\x08\x10\t\"0\n\x06Option\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\x80\x06\n\x15KinesisDataSourceArgs\x12\x1f\n\x0bstream_name\x18\x01 \x01(\tR\nstreamName\x12\x16\n\x06region\x18\x02 \x01(\tR\x06region\x12\x61\n\x15raw_stream_translator\x18\x03 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x13rawStreamTranslator\x12*\n\rtimestamp_key\x18\x04 \x01(\tB\x05\x82}\x02\x10\x03R\x0ctimestampKey\x12v\n\x1f\x64\x65\x66\x61ult_initial_stream_position\x18\x05 \x01(\x0e\x32(.tecton_proto.args.InitialStreamPositionB\x05\x82}\x02\x10\x03R\x1c\x64\x65\x66\x61ultInitialStreamPosition\x12g\n\x17initial_stream_position\x18\x0b \x01(\x0e\x32(.tecton_proto.args.InitialStreamPositionB\x05\x82}\x02\x08\x05R\x15initialStreamPosition\x12k\n!default_watermark_delay_threshold\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x10\x03R\x1e\x64\x65\x66\x61ultWatermarkDelayThreshold\x12:\n\x15\x64\x65\x64uplication_columns\x18\x07 \x03(\tB\x05\x82}\x02\x10\x03R\x14\x64\x65\x64uplicationColumns\x12\x33\n\x07options\x18\x08 \x03(\x0b\x32\x19.tecton_proto.args.OptionR\x07options\x12Z\n\x0b\x63ommon_args\x18\n \x01(\x0b\x32-.tecton_proto.args.StreamDataSourceCommonArgsB\n\x82}\x02\x08\x05\x92M\x02\x10\x01R\ncommonArgsJ\x04\x08\t\x10\n\"\xbe\x06\n\x13KafkaDataSourceArgs\x12\x36\n\x17kafka_bootstrap_servers\x18\x01 \x01(\tR\x15kafkaBootstrapServers\x12\x16\n\x06topics\x18\x02 \x01(\tR\x06topics\x12\x61\n\x15raw_stream_translator\x18\x03 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x13rawStreamTranslator\x12*\n\rtimestamp_key\x18\x04 \x01(\tB\x05\x82}\x02\x10\x03R\x0ctimestampKey\x12k\n!default_watermark_delay_threshold\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x10\x03R\x1e\x64\x65\x66\x61ultWatermarkDelayThreshold\x12\x33\n\x07options\x18\x06 \x03(\x0b\x32\x19.tecton_proto.args.OptionR\x07options\x12\x39\n\x15ssl_keystore_location\x18\x07 \x01(\tB\x05\x92M\x02\x08\x01R\x13sslKeystoreLocation\x12K\n\x1fssl_keystore_password_secret_id\x18\x08 \x01(\tB\x05\x92M\x02\x08\x01R\x1bsslKeystorePasswordSecretId\x12=\n\x17ssl_truststore_location\x18\t \x01(\tB\x05\x92M\x02\x08\x01R\x15sslTruststoreLocation\x12O\n!ssl_truststore_password_secret_id\x18\n \x01(\tB\x05\x92M\x02\x08\x01R\x1dsslTruststorePasswordSecretId\x12\x32\n\x11security_protocol\x18\x0b \x01(\tB\x05\x92M\x02\x08\x01R\x10securityProtocol\x12Z\n\x0b\x63ommon_args\x18\x0c \x01(\x0b\x32-.tecton_proto.args.StreamDataSourceCommonArgsB\n\x82}\x02\x08\x05\x92M\x02\x10\x01R\ncommonArgs\"\xe3\x02\n\x16RedshiftDataSourceArgs\x12\x1a\n\x08\x65ndpoint\x18\x01 \x01(\tR\x08\x65ndpoint\x12\x16\n\x05table\x18\x02 \x01(\tH\x00R\x05table\x12\x1d\n\x05query\x18\x05 \x01(\tB\x05\x92M\x02\x18\x03H\x00R\x05query\x12_\n\x14raw_batch_translator\x18\x03 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x12rawBatchTranslator\x12*\n\rtimestamp_key\x18\x06 \x01(\tB\x05\x82}\x02\x10\x03R\x0ctimestampKey\x12Y\n\x0b\x63ommon_args\x18\x07 \x01(\x0b\x32,.tecton_proto.args.BatchDataSourceCommonArgsB\n\x82}\x02\x08\x05\x92M\x02\x10\x01R\ncommonArgsB\x08\n\x06sourceJ\x04\x08\x04\x10\x05\"\xc8\x03\n\x17SnowflakeDataSourceArgs\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x19\n\x04role\x18\x02 \x01(\tB\x05\x92M\x02\x08\x01R\x04role\x12\x1a\n\x08\x64\x61tabase\x18\x03 \x01(\tR\x08\x64\x61tabase\x12\x16\n\x06schema\x18\x04 \x01(\tR\x06schema\x12#\n\twarehouse\x18\x05 \x01(\tB\x05\x92M\x02\x08\x01R\twarehouse\x12\x16\n\x05table\x18\x06 \x01(\tH\x00R\x05table\x12\x1d\n\x05query\x18\x07 \x01(\tB\x05\x92M\x02\x18\x03H\x00R\x05query\x12_\n\x14raw_batch_translator\x18\x08 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionB\x05\x82}\x02\x10\x03R\x12rawBatchTranslator\x12*\n\rtimestamp_key\x18\t \x01(\tB\x05\x82}\x02\x10\x03R\x0ctimestampKey\x12Y\n\x0b\x63ommon_args\x18\x0c \x01(\x0b\x32,.tecton_proto.args.BatchDataSourceCommonArgsB\n\x82}\x02\x08\x05\x92M\x02\x10\x01R\ncommonArgsB\x08\n\x06source\"\xe2\x01\n\x14SparkBatchConfigArgs\x12X\n\x14\x64\x61ta_source_function\x18\x01 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x12\x64\x61taSourceFunction\x12\x38\n\ndata_delay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\tdataDelay\x12\x36\n\x17supports_time_filtering\x18\x03 \x01(\x08R\x15supportsTimeFiltering\"q\n\x15SparkStreamConfigArgs\x12X\n\x14\x64\x61ta_source_function\x18\x01 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x12\x64\x61taSourceFunctionB\x13\n\x0f\x63om.tecton.argsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.args.data_source_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.argsP\001'
  _HIVEDATASOURCEARGS.fields_by_name['timestamp_column_name']._options = None
  _HIVEDATASOURCEARGS.fields_by_name['timestamp_column_name']._serialized_options = b'\202}\002\020\003'
  _HIVEDATASOURCEARGS.fields_by_name['raw_batch_translator']._options = None
  _HIVEDATASOURCEARGS.fields_by_name['raw_batch_translator']._serialized_options = b'\202}\002\020\003'
  _HIVEDATASOURCEARGS.fields_by_name['common_args']._options = None
  _HIVEDATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005'
  _FILEDATASOURCEARGS.fields_by_name['raw_batch_translator']._options = None
  _FILEDATASOURCEARGS.fields_by_name['raw_batch_translator']._serialized_options = b'\202}\002\020\003'
  _FILEDATASOURCEARGS.fields_by_name['schema_uri']._options = None
  _FILEDATASOURCEARGS.fields_by_name['schema_uri']._serialized_options = b'\222M\002\010\001'
  _FILEDATASOURCEARGS.fields_by_name['timestamp_column_name']._options = None
  _FILEDATASOURCEARGS.fields_by_name['timestamp_column_name']._serialized_options = b'\202}\002\020\003'
  _FILEDATASOURCEARGS.fields_by_name['common_args']._options = None
  _FILEDATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005\222M\002\020\001'
  _KINESISDATASOURCEARGS.fields_by_name['raw_stream_translator']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['raw_stream_translator']._serialized_options = b'\202}\002\020\003'
  _KINESISDATASOURCEARGS.fields_by_name['timestamp_key']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['timestamp_key']._serialized_options = b'\202}\002\020\003'
  _KINESISDATASOURCEARGS.fields_by_name['default_initial_stream_position']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['default_initial_stream_position']._serialized_options = b'\202}\002\020\003'
  _KINESISDATASOURCEARGS.fields_by_name['initial_stream_position']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['initial_stream_position']._serialized_options = b'\202}\002\010\005'
  _KINESISDATASOURCEARGS.fields_by_name['default_watermark_delay_threshold']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['default_watermark_delay_threshold']._serialized_options = b'\202}\002\020\003'
  _KINESISDATASOURCEARGS.fields_by_name['deduplication_columns']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['deduplication_columns']._serialized_options = b'\202}\002\020\003'
  _KINESISDATASOURCEARGS.fields_by_name['common_args']._options = None
  _KINESISDATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005\222M\002\020\001'
  _KAFKADATASOURCEARGS.fields_by_name['raw_stream_translator']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['raw_stream_translator']._serialized_options = b'\202}\002\020\003'
  _KAFKADATASOURCEARGS.fields_by_name['timestamp_key']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['timestamp_key']._serialized_options = b'\202}\002\020\003'
  _KAFKADATASOURCEARGS.fields_by_name['default_watermark_delay_threshold']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['default_watermark_delay_threshold']._serialized_options = b'\202}\002\020\003'
  _KAFKADATASOURCEARGS.fields_by_name['ssl_keystore_location']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['ssl_keystore_location']._serialized_options = b'\222M\002\010\001'
  _KAFKADATASOURCEARGS.fields_by_name['ssl_keystore_password_secret_id']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['ssl_keystore_password_secret_id']._serialized_options = b'\222M\002\010\001'
  _KAFKADATASOURCEARGS.fields_by_name['ssl_truststore_location']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['ssl_truststore_location']._serialized_options = b'\222M\002\010\001'
  _KAFKADATASOURCEARGS.fields_by_name['ssl_truststore_password_secret_id']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['ssl_truststore_password_secret_id']._serialized_options = b'\222M\002\010\001'
  _KAFKADATASOURCEARGS.fields_by_name['security_protocol']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['security_protocol']._serialized_options = b'\222M\002\010\001'
  _KAFKADATASOURCEARGS.fields_by_name['common_args']._options = None
  _KAFKADATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005\222M\002\020\001'
  _REDSHIFTDATASOURCEARGS.fields_by_name['query']._options = None
  _REDSHIFTDATASOURCEARGS.fields_by_name['query']._serialized_options = b'\222M\002\030\003'
  _REDSHIFTDATASOURCEARGS.fields_by_name['raw_batch_translator']._options = None
  _REDSHIFTDATASOURCEARGS.fields_by_name['raw_batch_translator']._serialized_options = b'\202}\002\020\003'
  _REDSHIFTDATASOURCEARGS.fields_by_name['timestamp_key']._options = None
  _REDSHIFTDATASOURCEARGS.fields_by_name['timestamp_key']._serialized_options = b'\202}\002\020\003'
  _REDSHIFTDATASOURCEARGS.fields_by_name['common_args']._options = None
  _REDSHIFTDATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005\222M\002\020\001'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['role']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['role']._serialized_options = b'\222M\002\010\001'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['warehouse']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['warehouse']._serialized_options = b'\222M\002\010\001'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['query']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['query']._serialized_options = b'\222M\002\030\003'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['raw_batch_translator']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['raw_batch_translator']._serialized_options = b'\202}\002\020\003'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['timestamp_key']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['timestamp_key']._serialized_options = b'\202}\002\020\003'
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['common_args']._options = None
  _SNOWFLAKEDATASOURCEARGS.fields_by_name['common_args']._serialized_options = b'\202}\002\010\005\222M\002\020\001'
  _DATETIMEPARTITIONCOLUMNARGS._serialized_start=305
  _DATETIMEPARTITIONCOLUMNARGS._serialized_end=465
  _BATCHDATASOURCECOMMONARGS._serialized_start=468
  _BATCHDATASOURCECOMMONARGS._serialized_end=673
  _STREAMDATASOURCECOMMONARGS._serialized_start=676
  _STREAMDATASOURCECOMMONARGS._serialized_end=964
  _HIVEDATASOURCEARGS._serialized_start=967
  _HIVEDATASOURCEARGS._serialized_end=1496
  _FILEDATASOURCEARGS._serialized_start=1499
  _FILEDATASOURCEARGS._serialized_end=2032
  _OPTION._serialized_start=2034
  _OPTION._serialized_end=2082
  _KINESISDATASOURCEARGS._serialized_start=2085
  _KINESISDATASOURCEARGS._serialized_end=2853
  _KAFKADATASOURCEARGS._serialized_start=2856
  _KAFKADATASOURCEARGS._serialized_end=3686
  _REDSHIFTDATASOURCEARGS._serialized_start=3689
  _REDSHIFTDATASOURCEARGS._serialized_end=4044
  _SNOWFLAKEDATASOURCEARGS._serialized_start=4047
  _SNOWFLAKEDATASOURCEARGS._serialized_end=4503
  _SPARKBATCHCONFIGARGS._serialized_start=4506
  _SPARKBATCHCONFIGARGS._serialized_end=4732
  _SPARKSTREAMCONFIGARGS._serialized_start=4734
  _SPARKSTREAMCONFIGARGS._serialized_end=4847
# @@protoc_insertion_point(module_scope)
