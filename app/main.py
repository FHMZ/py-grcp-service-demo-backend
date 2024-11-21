import logging
from concurrent import futures

import grpc

from controllers.controller import UserController
from controllers.proto.pb2 import users_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserController(), server)
    server.add_insecure_port('[::]:50051')
    print("Started gRPC Server on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
