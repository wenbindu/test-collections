from gevent import monkey
monkey.patch_all()

import grpc
import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()


import operator_pb2
import operator_pb2_grpc
import api

import grpc
import time
from concurrent import futures


class GameService(operator_pb2_grpc.GameServicer):
    def GetResult(self, request, context):
        response = operator_pb2.Resp()
        data = api.get_result(request.u_id)
        response.data = data['data']
        response.code = data['code']
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
operator_pb2_grpc.add_GameServicer_to_server(
    GameService(), server)
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)