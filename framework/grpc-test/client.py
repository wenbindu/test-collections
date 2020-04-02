import random
import time
import grpc

import operator_pb2
import operator_pb2_grpc

def get_result():
    print('begin')
    # time.sleep(1)
    data = operator_pb2.Req(u_id=str(random.randint(0,1000)))
    response = stub.GetResult(data)
    print(response)

channel = grpc.insecure_channel('localhost:50051')
stub = operator_pb2_grpc.GameStub(channel)

start=time.time()


# Wait for the requests to complete
for i in range (10000):
  try:
    get_result()
  except Exception as e:
    print(e)
end = time.time()
print(end - start)