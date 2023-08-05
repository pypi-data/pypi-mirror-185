# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class AtomicType(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'AtomicType': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['AtomicType']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'AtomicType']]: ...
    UNSPECIFIED = typing___cast('AtomicType', 0)
    BYTE = typing___cast('AtomicType', 1)
    INT16 = typing___cast('AtomicType', 2)
    INT32 = typing___cast('AtomicType', 3)
    INT64 = typing___cast('AtomicType', 4)
    FLOAT = typing___cast('AtomicType', 5)
    DOUBLE = typing___cast('AtomicType', 6)
    STRING = typing___cast('AtomicType', 7)
    BOOLEAN = typing___cast('AtomicType', 8)
    BYTES = typing___cast('AtomicType', 9)
UNSPECIFIED = typing___cast('AtomicType', 0)
BYTE = typing___cast('AtomicType', 1)
INT16 = typing___cast('AtomicType', 2)
INT32 = typing___cast('AtomicType', 3)
INT64 = typing___cast('AtomicType', 4)
FLOAT = typing___cast('AtomicType', 5)
DOUBLE = typing___cast('AtomicType', 6)
STRING = typing___cast('AtomicType', 7)
BOOLEAN = typing___cast('AtomicType', 8)
BYTES = typing___cast('AtomicType', 9)

class Schema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    encoding_positions_set = ... # type: builtin___bool

    @property
    def fields(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Field]: ...

    @property
    def options(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
        *,
        fields : typing___Optional[typing___Iterable[Field]] = None,
        id : typing___Optional[typing___Text] = None,
        options : typing___Optional[typing___Iterable[Option]] = None,
        encoding_positions_set : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Schema: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Schema: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"encoding_positions_set",u"fields",u"id",u"options"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"encoding_positions_set",b"encoding_positions_set",u"fields",b"fields",u"id",b"id",u"options",b"options"]) -> None: ...

class Field(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    description = ... # type: typing___Text
    id = ... # type: builtin___int
    encoding_position = ... # type: builtin___int

    @property
    def type(self) -> FieldType: ...

    @property
    def options(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        type : typing___Optional[FieldType] = None,
        id : typing___Optional[builtin___int] = None,
        encoding_position : typing___Optional[builtin___int] = None,
        options : typing___Optional[typing___Iterable[Option]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Field: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Field: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",u"encoding_position",u"id",u"name",u"options",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"type",b"type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"encoding_position",b"encoding_position",u"id",b"id",u"name",b"name",u"options",b"options",u"type",b"type"]) -> None: ...

class FieldType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    nullable = ... # type: builtin___bool
    atomic_type = ... # type: AtomicType

    @property
    def array_type(self) -> ArrayType: ...

    @property
    def iterable_type(self) -> IterableType: ...

    @property
    def map_type(self) -> MapType: ...

    @property
    def row_type(self) -> RowType: ...

    @property
    def logical_type(self) -> LogicalType: ...

    def __init__(self,
        *,
        nullable : typing___Optional[builtin___bool] = None,
        atomic_type : typing___Optional[AtomicType] = None,
        array_type : typing___Optional[ArrayType] = None,
        iterable_type : typing___Optional[IterableType] = None,
        map_type : typing___Optional[MapType] = None,
        row_type : typing___Optional[RowType] = None,
        logical_type : typing___Optional[LogicalType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FieldType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FieldType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"array_type",u"atomic_type",u"iterable_type",u"logical_type",u"map_type",u"row_type",u"type_info"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"array_type",u"atomic_type",u"iterable_type",u"logical_type",u"map_type",u"nullable",u"row_type",u"type_info"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"array_type",b"array_type",u"atomic_type",b"atomic_type",u"iterable_type",b"iterable_type",u"logical_type",b"logical_type",u"map_type",b"map_type",u"row_type",b"row_type",u"type_info",b"type_info"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"array_type",b"array_type",u"atomic_type",b"atomic_type",u"iterable_type",b"iterable_type",u"logical_type",b"logical_type",u"map_type",b"map_type",u"nullable",b"nullable",u"row_type",b"row_type",u"type_info",b"type_info"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"type_info",b"type_info"]) -> typing_extensions___Literal["atomic_type","array_type","iterable_type","map_type","row_type","logical_type"]: ...

class ArrayType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def element_type(self) -> FieldType: ...

    def __init__(self,
        *,
        element_type : typing___Optional[FieldType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ArrayType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArrayType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"element_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"element_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"element_type",b"element_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"element_type",b"element_type"]) -> None: ...

class IterableType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def element_type(self) -> FieldType: ...

    def __init__(self,
        *,
        element_type : typing___Optional[FieldType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IterableType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IterableType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"element_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"element_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"element_type",b"element_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"element_type",b"element_type"]) -> None: ...

class MapType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def key_type(self) -> FieldType: ...

    @property
    def value_type(self) -> FieldType: ...

    def __init__(self,
        *,
        key_type : typing___Optional[FieldType] = None,
        value_type : typing___Optional[FieldType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MapType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MapType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"key_type",u"value_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key_type",u"value_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"key_type",b"key_type",u"value_type",b"value_type"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key_type",b"key_type",u"value_type",b"value_type"]) -> None: ...

class RowType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def schema(self) -> Schema: ...

    def __init__(self,
        *,
        schema : typing___Optional[Schema] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RowType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RowType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"schema"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"schema"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"schema",b"schema"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"schema",b"schema"]) -> None: ...

class LogicalType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    urn = ... # type: typing___Text
    payload = ... # type: builtin___bytes

    @property
    def representation(self) -> FieldType: ...

    @property
    def argument_type(self) -> FieldType: ...

    @property
    def argument(self) -> FieldValue: ...

    def __init__(self,
        *,
        urn : typing___Optional[typing___Text] = None,
        payload : typing___Optional[builtin___bytes] = None,
        representation : typing___Optional[FieldType] = None,
        argument_type : typing___Optional[FieldType] = None,
        argument : typing___Optional[FieldValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogicalType: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogicalType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"argument",u"argument_type",u"representation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"argument",u"argument_type",u"payload",u"representation",u"urn"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"argument",b"argument",u"argument_type",b"argument_type",u"representation",b"representation"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"argument",b"argument",u"argument_type",b"argument_type",u"payload",b"payload",u"representation",b"representation",u"urn",b"urn"]) -> None: ...

class LogicalTypes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Enum(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'LogicalTypes.Enum': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['LogicalTypes.Enum']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'LogicalTypes.Enum']]: ...
        PYTHON_CALLABLE = typing___cast('LogicalTypes.Enum', 0)
        MICROS_INSTANT = typing___cast('LogicalTypes.Enum', 1)
        MILLIS_INSTANT = typing___cast('LogicalTypes.Enum', 2)
        DECIMAL = typing___cast('LogicalTypes.Enum', 3)
        FIXED_BYTES = typing___cast('LogicalTypes.Enum', 4)
        VAR_BYTES = typing___cast('LogicalTypes.Enum', 5)
        FIXED_CHAR = typing___cast('LogicalTypes.Enum', 6)
        VAR_CHAR = typing___cast('LogicalTypes.Enum', 7)
    PYTHON_CALLABLE = typing___cast('LogicalTypes.Enum', 0)
    MICROS_INSTANT = typing___cast('LogicalTypes.Enum', 1)
    MILLIS_INSTANT = typing___cast('LogicalTypes.Enum', 2)
    DECIMAL = typing___cast('LogicalTypes.Enum', 3)
    FIXED_BYTES = typing___cast('LogicalTypes.Enum', 4)
    VAR_BYTES = typing___cast('LogicalTypes.Enum', 5)
    FIXED_CHAR = typing___cast('LogicalTypes.Enum', 6)
    VAR_CHAR = typing___cast('LogicalTypes.Enum', 7)


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogicalTypes: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogicalTypes: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class Option(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    @property
    def type(self) -> FieldType: ...

    @property
    def value(self) -> FieldValue: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[FieldType] = None,
        value : typing___Optional[FieldValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Option: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Option: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"type",u"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"type",u"value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"type",b"type",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"type",b"type",u"value",b"value"]) -> None: ...

class Row(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FieldValue]: ...

    def __init__(self,
        *,
        values : typing___Optional[typing___Iterable[FieldValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Row: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Row: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"values"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"values",b"values"]) -> None: ...

class FieldValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def atomic_value(self) -> AtomicTypeValue: ...

    @property
    def array_value(self) -> ArrayTypeValue: ...

    @property
    def iterable_value(self) -> IterableTypeValue: ...

    @property
    def map_value(self) -> MapTypeValue: ...

    @property
    def row_value(self) -> Row: ...

    @property
    def logical_type_value(self) -> LogicalTypeValue: ...

    def __init__(self,
        *,
        atomic_value : typing___Optional[AtomicTypeValue] = None,
        array_value : typing___Optional[ArrayTypeValue] = None,
        iterable_value : typing___Optional[IterableTypeValue] = None,
        map_value : typing___Optional[MapTypeValue] = None,
        row_value : typing___Optional[Row] = None,
        logical_type_value : typing___Optional[LogicalTypeValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FieldValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FieldValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"array_value",u"atomic_value",u"field_value",u"iterable_value",u"logical_type_value",u"map_value",u"row_value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"array_value",u"atomic_value",u"field_value",u"iterable_value",u"logical_type_value",u"map_value",u"row_value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"array_value",b"array_value",u"atomic_value",b"atomic_value",u"field_value",b"field_value",u"iterable_value",b"iterable_value",u"logical_type_value",b"logical_type_value",u"map_value",b"map_value",u"row_value",b"row_value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"array_value",b"array_value",u"atomic_value",b"atomic_value",u"field_value",b"field_value",u"iterable_value",b"iterable_value",u"logical_type_value",b"logical_type_value",u"map_value",b"map_value",u"row_value",b"row_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"field_value",b"field_value"]) -> typing_extensions___Literal["atomic_value","array_value","iterable_value","map_value","row_value","logical_type_value"]: ...

class AtomicTypeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    byte = ... # type: builtin___int
    int16 = ... # type: builtin___int
    int32 = ... # type: builtin___int
    int64 = ... # type: builtin___int
    float = ... # type: builtin___float
    double = ... # type: builtin___float
    string = ... # type: typing___Text
    boolean = ... # type: builtin___bool
    bytes = ... # type: builtin___bytes

    def __init__(self,
        *,
        byte : typing___Optional[builtin___int] = None,
        int16 : typing___Optional[builtin___int] = None,
        int32 : typing___Optional[builtin___int] = None,
        int64 : typing___Optional[builtin___int] = None,
        float : typing___Optional[builtin___float] = None,
        double : typing___Optional[builtin___float] = None,
        string : typing___Optional[typing___Text] = None,
        boolean : typing___Optional[builtin___bool] = None,
        bytes : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AtomicTypeValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AtomicTypeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"boolean",u"byte",u"bytes",u"double",u"float",u"int16",u"int32",u"int64",u"string",u"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"boolean",u"byte",u"bytes",u"double",u"float",u"int16",u"int32",u"int64",u"string",u"value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"boolean",b"boolean",u"byte",b"byte",u"bytes",b"bytes",u"double",b"double",u"float",b"float",u"int16",b"int16",u"int32",b"int32",u"int64",b"int64",u"string",b"string",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"boolean",b"boolean",u"byte",b"byte",u"bytes",b"bytes",u"double",b"double",u"float",b"float",u"int16",b"int16",u"int32",b"int32",u"int64",b"int64",u"string",b"string",u"value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["byte","int16","int32","int64","float","double","string","boolean","bytes"]: ...

class ArrayTypeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def element(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FieldValue]: ...

    def __init__(self,
        *,
        element : typing___Optional[typing___Iterable[FieldValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ArrayTypeValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArrayTypeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"element"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"element",b"element"]) -> None: ...

class IterableTypeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def element(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FieldValue]: ...

    def __init__(self,
        *,
        element : typing___Optional[typing___Iterable[FieldValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IterableTypeValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IterableTypeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"element"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"element",b"element"]) -> None: ...

class MapTypeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def entries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MapTypeEntry]: ...

    def __init__(self,
        *,
        entries : typing___Optional[typing___Iterable[MapTypeEntry]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MapTypeValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MapTypeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entries"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entries",b"entries"]) -> None: ...

class MapTypeEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def key(self) -> FieldValue: ...

    @property
    def value(self) -> FieldValue: ...

    def __init__(self,
        *,
        key : typing___Optional[FieldValue] = None,
        value : typing___Optional[FieldValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MapTypeEntry: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MapTypeEntry: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

class LogicalTypeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def value(self) -> FieldValue: ...

    def __init__(self,
        *,
        value : typing___Optional[FieldValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogicalTypeValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogicalTypeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...
