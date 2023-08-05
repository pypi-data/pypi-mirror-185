# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from injective.wasmx.v1 import genesis_pb2 as injective_dot_wasmx_dot_v1_dot_genesis__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/wasmx/v1/query.proto',
  package='injective.wasmx.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1einjective/wasmx/v1/query.proto\x12\x12injective.wasmx.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a injective/wasmx/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\"\x19\n\x17QueryWasmxParamsRequest\"L\n\x18QueryWasmxParamsResponse\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.injective.wasmx.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\x17QueryModuleStateRequest\"K\n\x18QueryModuleStateResponse\x12/\n\x05state\x18\x01 \x01(\x0b\x32 .injective.wasmx.v1.GenesisState2\xb0\x02\n\x05Query\x12\x8c\x01\n\x0bWasmxParams\x12+.injective.wasmx.v1.QueryWasmxParamsRequest\x1a,.injective.wasmx.v1.QueryWasmxParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/injective/wasmx/v1/params\x12\x97\x01\n\x10WasmxModuleState\x12+.injective.wasmx.v1.QueryModuleStateRequest\x1a,.injective.wasmx.v1.QueryModuleStateResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /injective/wasmx/v1/module_stateBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,injective_dot_wasmx_dot_v1_dot_wasmx__pb2.DESCRIPTOR,injective_dot_wasmx_dot_v1_dot_genesis__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_QUERYWASMXPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryWasmxParamsRequest',
  full_name='injective.wasmx.v1.QueryWasmxParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=197,
)


_QUERYWASMXPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryWasmxParamsResponse',
  full_name='injective.wasmx.v1.QueryWasmxParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.wasmx.v1.QueryWasmxParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=275,
)


_QUERYMODULESTATEREQUEST = _descriptor.Descriptor(
  name='QueryModuleStateRequest',
  full_name='injective.wasmx.v1.QueryModuleStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=302,
)


_QUERYMODULESTATERESPONSE = _descriptor.Descriptor(
  name='QueryModuleStateResponse',
  full_name='injective.wasmx.v1.QueryModuleStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='injective.wasmx.v1.QueryModuleStateResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=379,
)

_QUERYWASMXPARAMSRESPONSE.fields_by_name['params'].message_type = injective_dot_wasmx_dot_v1_dot_wasmx__pb2._PARAMS
_QUERYMODULESTATERESPONSE.fields_by_name['state'].message_type = injective_dot_wasmx_dot_v1_dot_genesis__pb2._GENESISSTATE
DESCRIPTOR.message_types_by_name['QueryWasmxParamsRequest'] = _QUERYWASMXPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryWasmxParamsResponse'] = _QUERYWASMXPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryModuleStateRequest'] = _QUERYMODULESTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryModuleStateResponse'] = _QUERYMODULESTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryWasmxParamsRequest = _reflection.GeneratedProtocolMessageType('QueryWasmxParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYWASMXPARAMSREQUEST,
  '__module__' : 'injective.wasmx.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.QueryWasmxParamsRequest)
  })
_sym_db.RegisterMessage(QueryWasmxParamsRequest)

QueryWasmxParamsResponse = _reflection.GeneratedProtocolMessageType('QueryWasmxParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYWASMXPARAMSRESPONSE,
  '__module__' : 'injective.wasmx.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.QueryWasmxParamsResponse)
  })
_sym_db.RegisterMessage(QueryWasmxParamsResponse)

QueryModuleStateRequest = _reflection.GeneratedProtocolMessageType('QueryModuleStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATEREQUEST,
  '__module__' : 'injective.wasmx.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.QueryModuleStateRequest)
  })
_sym_db.RegisterMessage(QueryModuleStateRequest)

QueryModuleStateResponse = _reflection.GeneratedProtocolMessageType('QueryModuleStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATERESPONSE,
  '__module__' : 'injective.wasmx.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.QueryModuleStateResponse)
  })
_sym_db.RegisterMessage(QueryModuleStateResponse)


DESCRIPTOR._options = None
_QUERYWASMXPARAMSRESPONSE.fields_by_name['params']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='injective.wasmx.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=382,
  serialized_end=686,
  methods=[
  _descriptor.MethodDescriptor(
    name='WasmxParams',
    full_name='injective.wasmx.v1.Query.WasmxParams',
    index=0,
    containing_service=None,
    input_type=_QUERYWASMXPARAMSREQUEST,
    output_type=_QUERYWASMXPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/injective/wasmx/v1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WasmxModuleState',
    full_name='injective.wasmx.v1.Query.WasmxModuleState',
    index=1,
    containing_service=None,
    input_type=_QUERYMODULESTATEREQUEST,
    output_type=_QUERYMODULESTATERESPONSE,
    serialized_options=b'\202\323\344\223\002\"\022 /injective/wasmx/v1/module_state',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
