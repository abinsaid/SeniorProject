# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/endpoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/endpoint.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\rEndpointProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19google/api/endpoint.proto\x12\ngoogle.api"Q\n\x08\x45ndpoint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x07\x61liases\x18\x02 \x03(\tB\x02\x18\x01\x12\x0e\n\x06target\x18\x65 \x01(\t\x12\x12\n\nallow_cors\x18\x05 \x01(\x08\x42o\n\x0e\x63om.google.apiB\rEndpointProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3',
)


_ENDPOINT = _descriptor.Descriptor(
    name="Endpoint",
    full_name="google.api.Endpoint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.api.Endpoint.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="aliases",
            full_name="google.api.Endpoint.aliases",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="google.api.Endpoint.target",
            index=2,
            number=101,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="allow_cors",
            full_name="google.api.Endpoint.allow_cors",
            index=3,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=41,
    serialized_end=122,
)

DESCRIPTOR.message_types_by_name["Endpoint"] = _ENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType(
    "Endpoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENDPOINT,
        "__module__": "google.api.endpoint_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Endpoint)
    },
)
_sym_db.RegisterMessage(Endpoint)


DESCRIPTOR._options = None
_ENDPOINT.fields_by_name["aliases"]._options = None
# @@protoc_insertion_point(module_scope)
