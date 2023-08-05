# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/auction/v1beta1/tx.proto',
  package='injective.auction.v1beta1',
  syntax='proto3',
  serialized_options=b'ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"injective/auction/v1beta1/tx.proto\x12\x19injective.auction.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"f\n\x06MsgBid\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x33\n\nbid_amount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\r\n\x05round\x18\x03 \x01(\x04:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x10\n\x0eMsgBidResponse2Z\n\x03Msg\x12S\n\x03\x42id\x12!.injective.auction.v1beta1.MsgBid\x1a).injective.auction.v1beta1.MsgBidResponseBOZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_MSGBID = _descriptor.Descriptor(
  name='MsgBid',
  full_name='injective.auction.v1beta1.MsgBid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='injective.auction.v1beta1.MsgBid.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_amount', full_name='injective.auction.v1beta1.MsgBid.bid_amount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='injective.auction.v1beta1.MsgBid.round', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=221,
)


_MSGBIDRESPONSE = _descriptor.Descriptor(
  name='MsgBidResponse',
  full_name='injective.auction.v1beta1.MsgBidResponse',
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
  serialized_start=223,
  serialized_end=239,
)

_MSGBID.fields_by_name['bid_amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['MsgBid'] = _MSGBID
DESCRIPTOR.message_types_by_name['MsgBidResponse'] = _MSGBIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgBid = _reflection.GeneratedProtocolMessageType('MsgBid', (_message.Message,), {
  'DESCRIPTOR' : _MSGBID,
  '__module__' : 'injective.auction.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.MsgBid)
  })
_sym_db.RegisterMessage(MsgBid)

MsgBidResponse = _reflection.GeneratedProtocolMessageType('MsgBidResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBIDRESPONSE,
  '__module__' : 'injective.auction.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.MsgBidResponse)
  })
_sym_db.RegisterMessage(MsgBidResponse)


DESCRIPTOR._options = None
_MSGBID.fields_by_name['bid_amount']._options = None
_MSGBID._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='injective.auction.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=241,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='Bid',
    full_name='injective.auction.v1beta1.Msg.Bid',
    index=0,
    containing_service=None,
    input_type=_MSGBID,
    output_type=_MSGBIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
