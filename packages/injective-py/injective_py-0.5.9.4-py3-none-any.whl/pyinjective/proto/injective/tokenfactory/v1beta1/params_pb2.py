# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/tokenfactory/v1beta1/params.proto',
  package='injective.tokenfactory.v1beta1',
  syntax='proto3',
  serialized_options=b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+injective/tokenfactory/v1beta1/params.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x8f\x01\n\x06Params\x12\x84\x01\n\x12\x64\x65nom_creation_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBM\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x19yaml:\"denom_creation_fee\"\xc8\xde\x1f\x00\x42TZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='injective.tokenfactory.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom_creation_fee', full_name='injective.tokenfactory.v1beta1.Params.denom_creation_fee', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\031yaml:\"denom_creation_fee\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=217,
  serialized_end=360,
)

_PARAMS.fields_by_name['denom_creation_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'injective.tokenfactory.v1beta1.params_pb2'
  # @@protoc_insertion_point(class_scope:injective.tokenfactory.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['denom_creation_fee']._options = None
# @@protoc_insertion_point(module_scope)
