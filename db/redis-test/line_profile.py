import line_profiler
import atexit
import time
import functools
import redis

from multiprocessing import Process

profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)


pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )


@profile
def direct(r):
    r.sadd('test_info', '123')
    r.expire('test_info', 2)
    r.get('redis_test')
    r.set('redis_test', 5)
    r.expire('redis_test', 10)

@profile
def pipeline(r):
    p = r.pipeline()
    p.sadd('test_info', '123')
    p.expire('test_info', 2)
    p.get('redis_test')
    p.set('redis_test', 5)
    p.expire('redis_test', 10)
    p.execute()


def main():
    s = time.time()
    for _ in range(0,5000):
        pipeline(r)

    print(time.time() - s)


@profile
def multi_main():
    s = time.time()

    for _ in range(1000):
        jobs = []
        for _ in range(3):
            p = Process(target=pipeline, args=(r,))
            jobs.append(p)
            p.start()

        for j in jobs:
            j.join()
    print(time.time() - s)

multi_main()