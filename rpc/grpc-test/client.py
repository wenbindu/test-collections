import random
import time
import grpc

import operator_pb2
import operator_pb2_grpc
from gevent import monkey
monkey.patch_all()

import grpc._cython.cygrpc
grpc._cython.cygrpc.init_grpc_gevent()

# import gevent
# import gevent.monkey
# gevent.monkey.patch_socket()
# from gevent.pool import Pool

def get_result():
    print('begin')
    # time.sleep(1)
    data = operator_pb2.Req(u_id=str(random.randint(0,1000)))
    response = stub.GetResult.future(data)
    # print(response)
    return response

channel = grpc.insecure_channel('localhost:50051')
stub = operator_pb2_grpc.GameStub(channel)

# start = time.time()
# pool = Pool(10)

# for _ in range(0, 10):
#     # data = {'u_id': str(random.randint(0,1000))}
#     pool.spawn(get_result)
# print('*' * 10)
# pool.join()
# print('-' * 10)
# print(time.time() - start)
# grpc: 1000  0.7s   10000。 6-10s
num_requests=3000
start=time.time()
futures = []

# Make async requests
for i in range (num_requests):
  futures.append(get_result)

# Wait for the requests to complete
for i in range (num_requests):
  try:
    result = futures[i].result()
    # Do something with the result
    print(result)
  except Exception as e:
    print(e)
end = time.time()
print(end - start)