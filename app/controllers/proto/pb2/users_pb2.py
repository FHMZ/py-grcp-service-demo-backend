# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: users.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'users.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x04user\"\x19\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"8\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06trx_id\x18\x03 \x01(\t2?\n\x0bUserService\x12\x30\n\x07GetUser\x12\x11.user.UserRequest\x1a\x12.user.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=21
  _globals['_USERREQUEST']._serialized_end=46
  _globals['_USERRESPONSE']._serialized_start=48
  _globals['_USERRESPONSE']._serialized_end=104
  _globals['_USERSERVICE']._serialized_start=106
  _globals['_USERSERVICE']._serialized_end=169
# @@protoc_insertion_point(module_scope)
