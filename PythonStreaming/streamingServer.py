from concurrent import futures
import time
import logging

import grpc

import api_pb2
import api_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Pinger(api_pb2_grpc.PingServicer):

    def SayHello(self, request_iterator, context):
        print("In SayHello here")
        while True:
            yield api_pb2.PingMessage(greeting='Hello from the python server')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_PingServicer_to_server(Pinger(), server)
    server.add_insecure_port('[::]:7777')
    print("Server Listening")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()

    serve()