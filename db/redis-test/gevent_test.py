import gevent
# from gevent import monkey

# monkey.patch_all()
import time
import timeit
import redis

pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )

def redis_test():
    r.set("testsocket", 1)
    for _ in range(100):
        r.incr('testsocket', 10)
    r.get('testsocket')
    r.delete('testsocket')

def redis_pipe():
    p = r.pipeline(transaction=False)
    p.set("testsocket", 1)
    for i in range(100):
        p.incr('testsocket', 10)
    p.get('testsocket')
    p.delete('testsocket')
    p.execute()

def main():
    st = time.time()
    gs = []
    for _ in range(1000):
        # gs.append(gevent.spawn(redis_pipe))
        gs.append(gevent.spawn(redis_test))

    gevent.joinall(gs)
    print(time.time() - st)

main()


# python -m cProfile -o test.pstats  gevent_test.py
# snakeviz test.pstats

# gevent: 10.5s   connection: 1
# no gevent: 7.7s  connection: 200+
# gevent: pipeline: 1.53s
# no gevent: pipelint: 1.31s