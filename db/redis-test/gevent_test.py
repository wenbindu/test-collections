from gevent import monkey

monkey.patch_all()
import time
import timeit
import redis
from redis.connection import UnixDomainSocketConnection


pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )

def redis_test():
    print('begin')
    r.set("testsocket", 1)
    for _ in range(100):
        r.incr('testsocket', 10)
    r.get('testsocket')
    r.delete('testsocket')
    print('end')

def redis_pipe():
    p = r.pipeline(transaction=False)
    p.set("testsocket", 1)
    for i in range(100):
        p.incr('testsocket', 10)
    p.get('testsocket')
    p.delete('testsocket')
    p.execute()

# def main():
#     st = time.time()
#     for _ in range(1000):
#         redis_pipe()
#     print(time.time() - st)

# main()

print(timeit.Timer(stmt='redis_test()', 
setup='from __main__ import redis_test').timeit(number=1000))



# python -m cProfile -o test.pstats  gevent_test.py
# snakeviz test.pstats

# gevent: 11s
# no gevent: 8s
# gevent: pipeline: 1.45s
# no gevent: pipelint: 1.37s