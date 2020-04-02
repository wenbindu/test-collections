import zerorpc
import time
import random
import gevent
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool


c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

def get_result():
    print('begin')
    data = {'u_id': str(random.randint(0,1000))}
    resp = c.get_result(data)
    print(resp)

if __name__ == '__main__':
    start = time.time()
    pool = Pool(10000)

    for _ in range(0,10000):
        pool.spawn(get_result)
    pool.join()

    print('-' * 10)
    print(time.time() - start)

# zerorpc: 1000  1.6s   10000 15-17s