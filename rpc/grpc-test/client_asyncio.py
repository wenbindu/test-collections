import random
import time
import grpc

import operator_pb2
import operator_pb2_grpc

def get_result():
    # print('begin')
    # time.sleep(1)
    data = operator_pb2.Req(u_id=str(random.randint(0,1000)))
    response = stub.GetResult.future(data)
    # print(response)
    return response

channel = grpc.insecure_channel('localhost:50051')
stub = operator_pb2_grpc.GameStub(channel)

num_requests=10000
start=time.time()
futures = []

# Make async requests
for i in range (num_requests):
  futures.append(get_result())

# Wait for the requests to complete
for i in range (num_requests):
  try:
    result = futures[i].result()
    # Do something with the result
    # print(result)
  except Exception as e:
    print(e)
end = time.time()
print(end - start)