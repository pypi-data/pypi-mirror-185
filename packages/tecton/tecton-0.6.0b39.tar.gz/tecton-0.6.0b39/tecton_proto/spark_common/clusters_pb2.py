# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/spark_common/clusters.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(tecton_proto/spark_common/clusters.proto\x12\x19tecton_proto.spark_common\"0\n\x0f\x45xistingCluster\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\"\xd6\x07\n\nNewCluster\x12!\n\x0bnum_workers\x18\x01 \x01(\x05H\x00R\nnumWorkers\x12\x44\n\tautoscale\x18\x02 \x01(\x0b\x32$.tecton_proto.spark_common.AutoScaleH\x00R\tautoscale\x12!\n\x0c\x63luster_name\x18\x03 \x01(\tR\x0b\x63lusterName\x12#\n\rspark_version\x18\x04 \x01(\tR\x0csparkVersion\x12S\n\nspark_conf\x18\x0f \x03(\x0b\x32\x34.tecton_proto.spark_common.NewCluster.SparkConfEntryR\tsparkConf\x12O\n\x0e\x61ws_attributes\x18\x07 \x01(\x0b\x32(.tecton_proto.spark_common.AwsAttributesR\rawsAttributes\x12 \n\x0cnode_type_id\x18\x06 \x01(\tR\nnodeTypeId\x12.\n\x13\x65nable_elastic_disk\x18\x0c \x01(\x08R\x11\x65nableElasticDisk\x12N\n\x0cinit_scripts\x18\t \x03(\x0b\x32+.tecton_proto.spark_common.ResourceLocationR\x0binitScripts\x12U\n\x10\x63luster_log_conf\x18\n \x01(\x0b\x32+.tecton_proto.spark_common.ResourceLocationR\x0e\x63lusterLogConf\x12\x46\n\x0b\x63ustom_tags\x18\x0b \x03(\x0b\x32%.tecton_proto.spark_common.ClusterTagR\ncustomTags\x12\x30\n\x13terminateOnComplete\x18\r \x01(\x08R\x13terminateOnComplete\x12]\n\x0espark_env_vars\x18\x10 \x03(\x0b\x32\x37.tecton_proto.spark_common.NewCluster.SparkEnvVarsEntryR\x0csparkEnvVars\x1a<\n\x0eSparkConfEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a?\n\x11SparkEnvVarsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0e\n\x0cworkers_typeJ\x04\x08\x05\x10\x06J\x04\x08\x08\x10\tJ\x04\x08\x0e\x10\x0f\"M\n\tAutoScale\x12\x1f\n\x0bmin_workers\x18\x01 \x01(\x05R\nminWorkers\x12\x1f\n\x0bmax_workers\x18\x02 \x01(\x05R\nmaxWorkers\"\xab\x03\n\rAwsAttributes\x12&\n\x0f\x66irst_on_demand\x18\x05 \x01(\x05R\rfirstOnDemand\x12N\n\x0c\x61vailability\x18\x06 \x01(\x0e\x32*.tecton_proto.spark_common.AwsAvailabilityR\x0c\x61vailability\x12\x17\n\x07zone_id\x18\x07 \x01(\tR\x06zoneId\x12\x33\n\x16spot_bid_price_percent\x18\x08 \x01(\x05R\x13spotBidPricePercent\x12\x30\n\x14instance_profile_arn\x18\x04 \x01(\tR\x12instanceProfileArn\x12P\n\x0f\x65\x62s_volume_type\x18\x01 \x01(\x0e\x32(.tecton_proto.spark_common.EbsVolumeTypeR\rebsVolumeType\x12(\n\x10\x65\x62s_volume_count\x18\x02 \x01(\x05R\x0e\x65\x62sVolumeCount\x12&\n\x0f\x65\x62s_volume_size\x18\x03 \x01(\x05R\rebsVolumeSize\"\xe1\x01\n\x10ResourceLocation\x12:\n\x02s3\x18\x01 \x01(\x0b\x32(.tecton_proto.spark_common.S3StorageInfoH\x00R\x02s3\x12@\n\x04\x64\x62\x66s\x18\x03 \x01(\x0b\x32*.tecton_proto.spark_common.DbfsStorageInfoH\x00R\x04\x64\x62\x66s\x12\x43\n\x05local\x18\x02 \x01(\x0b\x32+.tecton_proto.spark_common.LocalStorageInfoH\x00R\x05localB\n\n\x08location\"I\n\rS3StorageInfo\x12 \n\x0b\x64\x65stination\x18\x01 \x01(\tR\x0b\x64\x65stination\x12\x16\n\x06region\x18\x02 \x01(\tR\x06region\"3\n\x0f\x44\x62\x66sStorageInfo\x12 \n\x0b\x64\x65stination\x18\x01 \x01(\tR\x0b\x64\x65stination\"&\n\x10LocalStorageInfo\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\"J\n\x0e\x43lusterLogConf\x12\x38\n\x02s3\x18\x01 \x01(\x0b\x32(.tecton_proto.spark_common.S3StorageInfoR\x02s3\"4\n\nClusterTag\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value*\x8f\x01\n\x0f\x41wsAvailability\x12\x1c\n\x18UNKNOWN_AWS_AVAILABILITY\x10\x00\x12\x08\n\x04SPOT\x10\x01\x12\r\n\tON_DEMAND\x10\x02\x12\x16\n\x12SPOT_WITH_FALLBACK\x10\x03\x12-\n)INSTANCE_FLEET_FOR_INTEGRATION_TESTS_ONLY\x10\x04*c\n\rEbsVolumeType\x12\x1b\n\x17UNKNOWN_EBS_VOLUME_TYPE\x10\x00\x12\x17\n\x13GENERAL_PURPOSE_SSD\x10\x01\x12\x1c\n\x18THROUGHPUT_OPTIMIZED_HDD\x10\x02\x42\x1b\n\x17\x63om.tecton.spark_commonP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.spark_common.clusters_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.tecton.spark_commonP\001'
  _NEWCLUSTER_SPARKCONFENTRY._options = None
  _NEWCLUSTER_SPARKCONFENTRY._serialized_options = b'8\001'
  _NEWCLUSTER_SPARKENVVARSENTRY._options = None
  _NEWCLUSTER_SPARKENVVARSENTRY._serialized_options = b'8\001'
  _AWSAVAILABILITY._serialized_start=2142
  _AWSAVAILABILITY._serialized_end=2285
  _EBSVOLUMETYPE._serialized_start=2287
  _EBSVOLUMETYPE._serialized_end=2386
  _EXISTINGCLUSTER._serialized_start=71
  _EXISTINGCLUSTER._serialized_end=119
  _NEWCLUSTER._serialized_start=122
  _NEWCLUSTER._serialized_end=1104
  _NEWCLUSTER_SPARKCONFENTRY._serialized_start=945
  _NEWCLUSTER_SPARKCONFENTRY._serialized_end=1005
  _NEWCLUSTER_SPARKENVVARSENTRY._serialized_start=1007
  _NEWCLUSTER_SPARKENVVARSENTRY._serialized_end=1070
  _AUTOSCALE._serialized_start=1106
  _AUTOSCALE._serialized_end=1183
  _AWSATTRIBUTES._serialized_start=1186
  _AWSATTRIBUTES._serialized_end=1613
  _RESOURCELOCATION._serialized_start=1616
  _RESOURCELOCATION._serialized_end=1841
  _S3STORAGEINFO._serialized_start=1843
  _S3STORAGEINFO._serialized_end=1916
  _DBFSSTORAGEINFO._serialized_start=1918
  _DBFSSTORAGEINFO._serialized_end=1969
  _LOCALSTORAGEINFO._serialized_start=1971
  _LOCALSTORAGEINFO._serialized_end=2009
  _CLUSTERLOGCONF._serialized_start=2011
  _CLUSTERLOGCONF._serialized_end=2085
  _CLUSTERTAG._serialized_start=2087
  _CLUSTERTAG._serialized_end=2139
# @@protoc_insertion_point(module_scope)
