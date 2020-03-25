import time
import functools
import redis
from flask import Flask, request, jsonify
from threading import Thread
from multiprocessing import Process
# from multiprocessing import Pool

pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )


def direct(r):
    r.sadd('test_info', '123')
    r.expire('test_info', 2)
    r.get('redis_test')
    r.set('redis_test', 5)
    r.expire('redis_test', 10)

def incry(r):
    m = r.incr('test_incry')
    print(m)


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
    for _ in range(0,50000):
        pipeline(r)

    print(time.time() - s)


def run_1(r):
    for _ in range(0, 1000):
        incry(r)


def multi_main():
    # jobs = [Process(target=run_1, args=(r,)) for x in range(0,5)]
    jobs = [Thread(target=run_1, args=(r,)) for x in range(0,5)]
    
    print(jobs)
    s = time.time()
    for j in jobs:
        j.start()    

    for j in jobs:
        j.join()
    print(time.time() - s)

if __name__ == "__main__":
    main()
    # multi_main()
# python -m cProfile -o test.pstats  scripts.py
# python -m cProfile -s cumulative scripts.py
# snakeviz test.pstats
# gprof2dot -f pstats test.pstats | dot -Tpng -o output.png && eog output.png


# kernprof -l -v scripts.py
# python -m line_profiler scripts.py.lprof

# 5000次， 5进程， 0.5s-pipeline
# 5000， 5进程， 0.9s-connection
# 