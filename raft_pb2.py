# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\x12\x04raft\"\\\n\x0cRequest_Vote\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\t\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"8\n\x13RequestVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0bvoteGranted\x18\x02 \x01(\x08\"#\n\x05\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x8f\x01\n\x0e\x41ppend_Entries\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\t\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x1c\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x0b.raft.Entry\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\"6\n\x15\x41ppendEntriesResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1f\n\x0cServe_Client\x12\x0f\n\x07Request\x18\x01 \x01(\t\"F\n\x13ServeClientResponse\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\x12\x10\n\x08LeaderID\x18\x02 \x01(\t\x12\x0f\n\x07Success\x18\x03 \x01(\x08\x32\xc6\x01\n\x04Raft\x12<\n\x0bRequestVote\x12\x12.raft.Request_Vote\x1a\x19.raft.RequestVoteResponse\x12\x42\n\rAppendEntries\x12\x14.raft.Append_Entries\x1a\x1b.raft.AppendEntriesResponse\x12<\n\x0bServeClient\x12\x12.raft.Serve_Client\x1a\x19.raft.ServeClientResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST_VOTE']._serialized_start=20
  _globals['_REQUEST_VOTE']._serialized_end=112
  _globals['_REQUESTVOTERESPONSE']._serialized_start=114
  _globals['_REQUESTVOTERESPONSE']._serialized_end=170
  _globals['_ENTRY']._serialized_start=172
  _globals['_ENTRY']._serialized_end=207
  _globals['_APPEND_ENTRIES']._serialized_start=210
  _globals['_APPEND_ENTRIES']._serialized_end=353
  _globals['_APPENDENTRIESRESPONSE']._serialized_start=355
  _globals['_APPENDENTRIESRESPONSE']._serialized_end=409
  _globals['_SERVE_CLIENT']._serialized_start=411
  _globals['_SERVE_CLIENT']._serialized_end=442
  _globals['_SERVECLIENTRESPONSE']._serialized_start=444
  _globals['_SERVECLIENTRESPONSE']._serialized_end=514
  _globals['_RAFT']._serialized_start=517
  _globals['_RAFT']._serialized_end=715
# @@protoc_insertion_point(module_scope)
