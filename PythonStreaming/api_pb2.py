# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tapi.proto\x12\x03\x61pi\"\x1f\n\x0bPingMessage\x12\x10\n\x08greeting\x18\x01 \x01(\t\"/\n\rHealthMessage\x12\x0e\n\x06health\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x32<\n\x04Ping\x12\x34\n\x08SayHello\x12\x10.api.PingMessage\x1a\x10.api.PingMessage\"\x00(\x01\x30\x01\x32\x41\n\x06Health\x12\x37\n\x0bHealthCheck\x12\x12.api.HealthMessage\x1a\x12.api.HealthMessage\"\x00\x62\x06proto3')
)




_PINGMESSAGE = _descriptor.Descriptor(
  name='PingMessage',
  full_name='api.PingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='api.PingMessage.greeting', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=49,
)


_HEALTHMESSAGE = _descriptor.Descriptor(
  name='HealthMessage',
  full_name='api.HealthMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health', full_name='api.HealthMessage.health', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.HealthMessage.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=51,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['PingMessage'] = _PINGMESSAGE
DESCRIPTOR.message_types_by_name['HealthMessage'] = _HEALTHMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingMessage = _reflection.GeneratedProtocolMessageType('PingMessage', (_message.Message,), dict(
  DESCRIPTOR = _PINGMESSAGE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.PingMessage)
  ))
_sym_db.RegisterMessage(PingMessage)

HealthMessage = _reflection.GeneratedProtocolMessageType('HealthMessage', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHMESSAGE,
  __module__ = 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.HealthMessage)
  ))
_sym_db.RegisterMessage(HealthMessage)



_PING = _descriptor.ServiceDescriptor(
  name='Ping',
  full_name='api.Ping',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=100,
  serialized_end=160,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='api.Ping.SayHello',
    index=0,
    containing_service=None,
    input_type=_PINGMESSAGE,
    output_type=_PINGMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PING)

DESCRIPTOR.services_by_name['Ping'] = _PING


_HEALTH = _descriptor.ServiceDescriptor(
  name='Health',
  full_name='api.Health',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=162,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='HealthCheck',
    full_name='api.Health.HealthCheck',
    index=0,
    containing_service=None,
    input_type=_HEALTHMESSAGE,
    output_type=_HEALTHMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEALTH)

DESCRIPTOR.services_by_name['Health'] = _HEALTH

# @@protoc_insertion_point(module_scope)
