from typing import Callable
from typing import Optional

import attrs
from typeguard import typechecked

from tecton_core import function_deserialization
from tecton_core import id_helper
from tecton_core.specs import tecton_object_spec
from tecton_core.specs import utils
from tecton_proto.args import transformation_pb2 as transformation__args_pb2
from tecton_proto.common import framework_version_pb2
from tecton_proto.data import transformation_pb2 as transformation__data_pb2

__all__ = ["TransformationSpec"]


@utils.frozen_strict
class TransformationSpec(tecton_object_spec.TectonObjectSpec):
    transformation_mode: transformation__args_pb2.TransformationMode
    user_function: Callable = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})

    # Temporarily expose the underlying data proto during migration.
    # TODO(TEC-12443): Remove this attribute.
    data_proto: Optional[transformation__data_pb2.Transformation] = attrs.field(
        metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True}
    )

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: transformation__data_pb2.Transformation) -> "TransformationSpec":
        user_function = None
        if proto.HasField("user_function"):
            user_function = function_deserialization.from_proto(proto.user_function)
        return cls(
            name=proto.fco_metadata.name,
            id=id_helper.IdHelper.to_string(proto.transformation_id),
            framework_version=utils.get_field_or_none(proto.fco_metadata, "framework_version"),
            workspace=utils.get_field_or_none(proto.fco_metadata, "workspace"),
            is_local_object=False,
            transformation_mode=proto.transformation_mode,
            user_function=user_function,
            data_proto=proto,
        )

    @classmethod
    @typechecked
    def from_args_proto(
        cls, proto: transformation__args_pb2.TransformationArgs, user_function: Callable
    ) -> "TransformationSpec":
        return cls(
            name=proto.info.name,
            id=id_helper.IdHelper.to_string(proto.transformation_id),
            framework_version=framework_version_pb2.FrameworkVersion.FWV5,
            workspace=None,
            is_local_object=True,
            transformation_mode=proto.transformation_mode,
            user_function=user_function,
            data_proto=None,
        )
