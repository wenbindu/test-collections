import zerorpc
import time
import random

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

if __name__ == '__main__':
    start = time.time()
    for _ in range(0,10000):
        data = {'u_id': str(random.randint(0,1000))}
        data = c.get_result(data)
        print(data)
    print('-' * 10)
    print(time.time() - start)

# zerorpc: 1000  1.6s   10000 15-17s