import gevent
import time
import redis


def return_keys(db):
    pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=db,
                    encoding='utf-8',
                    decode_responses=True)
    r = redis.StrictRedis(
            connection_pool=pool
        )
    keys = r.keys()
    return keys, r

keys , r = return_keys(6)

def del_key():
    for key in keys:
        if r.ttl(key) < 0:
            print(key)
            if key.startswith('room:len:'):
                r.delete(key)

def print_keys():
    for key in keys:
        if r.ttl(key) < 0:
            print(key)
