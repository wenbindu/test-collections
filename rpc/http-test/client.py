import time
import requests
import random
import gevent
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool

s = requests.session()

def get_result():
    print('begin')
    data = {'u_id': str(random.randint(0,1000))}
    r = s.post('http://127.0.0.1:8081/spin', json=data).json()
    print(r)

if __name__ == '__main__':
    start = time.time()
    # for _ in range(0,1000):
    #     get_result()
    # print('-' * 10)
    pool = Pool(10)
    for i in range(0, 10):
        pool.spawn(get_result)
    print(time.time() - start)
    pool.join()
    print(time.time() - start)

# http: 1000 4.2s   10000 38-44s