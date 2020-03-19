from flask_caching import Cache
from flask import Flask
import redis
import time

app = Flask(__name__)
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)

pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )


@cache.cached(timeout=50, key_prefix='all_comments')
def get_cache():
    return r.get('test')

def get_cache_redis():
    return r.get('test')

r.set('test', '2')
s = time.time()
for _ in range(100000):
    print(get_cache_redis())

print(time.time() - s)