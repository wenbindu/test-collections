import random
import time
import grpc

import operator_pb2
import operator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = operator_pb2_grpc.GameStub(channel)

start = time.time()
for _ in range(0, 10000):
    # data = {'u_id': str(random.randint(0,1000))}
    data = operator_pb2.Req(u_id=str(random.randint(0,1000)))
    response = stub.GetResult(data)
    print(response)

print('-' * 10)
print(time.time() - start)
# grpc: 1000  0.7s   10000。 6-10s