import time
import functools
import redis
from flask import Flask, request, jsonify


app = Flask(__name__)

pool = redis.ConnectionPool(host='127.0.0.1', 
                    port='6379', 
                    db=6,
                    encoding='utf-8',
                    decode_responses=True)
r = redis.StrictRedis(
        connection_pool=pool
    )

def timer(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        s = time.time()
        data = request.json or request.form.to_dict()
        r = func(data, *args, **kwargs)
        end = time.time()
        print('spend: {}'.format(int(end * 1000 - s * 1000)))
        return r

    return decorator


@app.route('/test', methods=['POST', 'GET'])
@timer
def test(data):
    # r.smembers('test1')
    r.get('test')
    return jsonify(dict(code=200))
    

# gunicorn -w 4 -t 1800 -b :8081 -k gevent --log-level=info server:app
""" 20
spend: 35.444091796875
spend: 34.06298828125
spend: 34.8818359375
spend: 42.34521484375
"""

"""200
spend: 358.463134765625
spend: 372.356689453125
spend: 299.43408203125
spend: 347.26171875
"""
# gunicorn -w 4 -t 1800 -b :8081 --log-level=info server:app 
""" 20
pend: 2.4541015625
spend: 0.539794921875
spend: 3.024658203125
spend: 1.0751953125
spend: 4.28100585937
"""

"""200
spend: 2.976806640625
spend: 0.615966796875
spend: 2.06396484375
spend: 3.73974609375
spend: 0.419677734375
"""

