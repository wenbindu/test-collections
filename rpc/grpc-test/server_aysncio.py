
import operator_pb2
import operator_pb2_grpc
import api

import grpc
import time
from concurrent import futures
from grpc_asyncio import AsyncioExecutor


class GameService(operator_pb2_grpc.GameServicer):
    async def GetResult(self, request, context):
        response = operator_pb2.Resp()
        data = await api.get_result_short(request.u_id)
        response.data = data['data']
        response.code = data['code']
        return response


def main():
    server = grpc.server(AsyncioExecutor())
    operator_pb2_grpc.add_GameServicer_to_server(
        GameService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    return server


if __name__ == '__main__':
    server = main()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
    
