from typing import Any
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar

import attrs
import pendulum
import typeguard
from attrs import validators
from google import protobuf

from tecton_core import time_utils

# An attrs metadata key use to indicate that a spec field is allowed and expected to diverge for the same object
# definition between local and remote objects. This metadata used in testing and to codify fields where divergence is
# permitted.
LOCAL_REMOTE_DIVERGENCE_ALLOWED = "local_remote_divergence_allowed"


@typeguard.typechecked
def get_field_or_none(proto: protobuf.message.Message, field: str) -> Any:
    """Get the proto message's field. Return None if the field is not set (instead of the default value).

    When filling specs, `None` should be typically filled when the underlying proto field is unset - except in cases
    where the proto default (e.g. 0) is the desired for the Python value.
    """
    if proto.HasField(field):
        return getattr(proto, field)
    else:
        return None


@typeguard.typechecked
def get_duration_field_or_none(proto: protobuf.message.Message, field: str) -> Optional[pendulum.Duration]:
    """Get the proto message's duration-type field. Return None if the field is not set (instead of the default value)."""
    if proto.HasField(field):
        proto_duration = getattr(proto, field)
        return time_utils.proto_to_duration(proto_duration)
    else:
        return None


T = TypeVar("T")


@typeguard.typechecked
def get_tuple_from_repeated_field(repeated_field: Iterable[T]) -> Tuple[T, ...]:
    return tuple(value for value in repeated_field)


def type_validator(instance: Any, attribute: attrs.Attribute, value: Any):
    """An attrs validator that asserts that an attribute matches its declared type."""
    assert attribute.type is not None, "Type annotations are required."

    # It would be better to assert on the affirmative (e.g. `assert inspect.is_class(attribute.type)`), but generic
    # types (e.g. `Optional[str]`) are not classes and do not have a documented way to identify them.
    assert not isinstance(
        attribute.type, str
    ), f"Found unresolved type annotation `{attribute.type}` for attribute `{attribute.name}`. Do not use forward-declared types with the frozen_strict decorator."
    try:
        typeguard.check_type(attribute.name, value, attribute.type)
    except TypeError as e:
        raise TypeError(
            f"{instance.__class__.__name__} initialized with invalid type for attribute `{attribute.name}`. Expected type: `{attribute.type.__name__}`. Provided type: `{type(value).__name__}`."
        ) from e


def add_strict_type_validation(cls: type, fields: List[attrs.Attribute]) -> List[attrs.Attribute]:
    """An attrs field transformer that add type assertions to all fields."""
    new_fields = []
    for field in fields:
        if field.validator:
            new_validator = validators.and_(type_validator, field.validator)
        else:
            new_validator = type_validator
        new_fields.append(field.evolve(validator=new_validator))
    return new_fields


def frozen_strict(cls):
    """A decorator used to define a frozen attrs class where all attribute type annotations are enforced at runtime."""

    # Use slots=False because the slots optimization causes issues with serialization (needed for pyspark UDFs run on
    # worker nodes) when combined with attrs inheritance, i.e. attrs classes inheriting from other attrs classes.
    return attrs.frozen(cls, field_transformer=add_strict_type_validation, slots=False)
