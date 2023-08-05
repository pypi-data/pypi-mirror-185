from typing import Dict
from typing import List
from typing import Optional

from typeguard import typechecked

from tecton_core import specs
from tecton_core.id_helper import IdHelper
from tecton_proto.common import id_pb2
from tecton_proto.data import fco_pb2
from tecton_proto.data.feature_view_pb2 import FeatureView as FeatureViewProto
from tecton_proto.data.transformation_pb2 import Transformation as Transformation
from tecton_proto.data.virtual_data_source_pb2 import VirtualDataSource as DataSourceProto


class FcoContainer:
    """A wrapper class for FcoContainer proto, contains convenience accessors."""

    @typechecked
    def __init__(self, proto: fco_pb2.FcoContainer):
        self._proto = proto
        self._id_to_spec: Dict[str, specs.TectonObjectSpec] = {}
        for fco_proto in self._proto.fcos:
            spec = _spec_from_fco_data_proto(fco_proto)
            self._id_to_spec[spec.id] = spec

    @typechecked
    def get_by_id(self, id: str) -> specs.TectonObjectSpec:
        """
        :return: The TectonObjectSpec with the provided `id`.
        """
        return self._id_to_spec[id]

    @typechecked
    def get_by_id_proto(self, id_proto: id_pb2.Id) -> specs.TectonObjectSpec:
        """
        :return: The TectonObjectSpec with the provided `id` proto.
        """
        id_string = IdHelper.to_string(id_proto)
        return self._id_to_spec[id_string]

    @typechecked
    def get_by_ids(self, ids: List[str]) -> List[specs.TectonObjectSpec]:
        """
        :return: The TectonObjectSpec with the provided `ids`.
        """

        return [self.get_by_id(id) for id in ids]

    @typechecked
    def get_single_root(self) -> Optional[specs.TectonObjectSpec]:
        """
        :return: The root TectonObjectSpec for the container or None. Errors if len(root_ids) > 1
        """

        num_root_ids = len(self._proto.root_ids)
        if num_root_ids == 0:
            return None
        elif num_root_ids > 1:
            raise ValueError(f"Expected a single result but got $num_root_ids")
        else:
            return self.get_by_id_proto(self._proto.root_ids[0])

    @typechecked
    def get_root_fcos(self) -> List[specs.TectonObjectSpec]:
        """
        :return: All root TectonObjectSpec for the container.
        """

        return [self.get_by_id_proto(id) for id in self._proto.root_ids]


FCO_CONTAINER_EMTPY = FcoContainer(fco_pb2.FcoContainer())


def _spec_from_fco_data_proto(fco: fco_pb2.Fco) -> specs.TectonObjectSpec:
    if fco.HasField("virtual_data_source"):
        return specs.DataSourceSpec.from_data_proto(fco.virtual_data_source)
    elif fco.HasField("entity"):
        return specs.EntitySpec.from_data_proto(fco.entity)
    elif fco.HasField("transformation"):
        return specs.TransformationSpec.from_data_proto(fco.transformation)
    elif fco.HasField("feature_view"):
        return specs.create_feature_view_spec_from_data_proto(fco.feature_view)
    elif fco.HasField("feature_service"):
        return specs.FeatureServiceSpec.from_data_proto(fco.feature_service)
    else:
        raise ValueError(f"Unexpected fco type: {fco}")


def _wrap_data_fco(inner_proto) -> fco_pb2.Fco:
    fco = fco_pb2.Fco()
    if isinstance(inner_proto, DataSourceProto):
        fco.virtual_data_source.CopyFrom(inner_proto)
    elif isinstance(inner_proto, Transformation):
        fco.transformation.CopyFrom(inner_proto)
    elif isinstance(inner_proto, FeatureViewProto):
        fco.feature_view.CopyFrom(inner_proto)
    else:
        raise Exception("Unsupported type " + str(type(inner_proto)))
    return fco


def create_fco_container(fco_protos: List) -> fco_pb2.FcoContainer:
    proto = fco_pb2.FcoContainer()
    for inner_fco_proto in fco_protos:
        wrapped_fco_proto = _wrap_data_fco(inner_fco_proto)
        proto.fcos.append(wrapped_fco_proto)
    return FcoContainer(proto)
