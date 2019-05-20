# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class PingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/api.Ping/SayHello',
        request_serializer=api__pb2.PingMessage.SerializeToString,
        response_deserializer=api__pb2.PingMessage.FromString,
        )


class PingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=api__pb2.PingMessage.FromString,
          response_serializer=api__pb2.PingMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Ping', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class HealthStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HealthCheck = channel.unary_unary(
        '/api.Health/HealthCheck',
        request_serializer=api__pb2.HealthMessage.SerializeToString,
        response_deserializer=api__pb2.HealthMessage.FromString,
        )


class HealthServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HealthCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HealthServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HealthCheck': grpc.unary_unary_rpc_method_handler(
          servicer.HealthCheck,
          request_deserializer=api__pb2.HealthMessage.FromString,
          response_serializer=api__pb2.HealthMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Health', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
