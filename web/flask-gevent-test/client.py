import time
import requests
import random
import threading 
from multiprocessing import Pool

s = requests.session()

def post_result(mid):
    start = time.time()
    data = {
        "total_pay": 0,
        "level": 2,
        "mid": mid,
        "machine": "FuFuRiches",
        "avatar_url": "",
        "vip_level": 0,
        "balance": 101660,
        "bet": 500
    }
    r = s.post('http://127.0.0.1:8081/test', json=data, timeout=10).json()
    
    timer = time.time() - start
    print('resp_time:{}'.format(timer))

def multi_process():
    p = Pool(200)
    i = 149500
    for _ in range(1):
        p.map(post_result, [i for i in range(i, i+200)])

def multi_thread():
    ths = []
    for i in range(200):
        t = threading.Thread(target=post_result, args=(i,))
        ths.append(t)
    
    print('begin start')
    for t in ths:
        t.start()
    
    print('begin join...')
    for t in ths:
        t.join()

if __name__ == '__main__':
    start = time.time()
    multi_process()
    # multi_thread()
    print(time.time() - start)
    

# 200 + gevent + gunicorn + flask
"""
resp_time:1.4399609565734863
resp_time:1.3442130088806152
resp_time:1.2940950393676758
resp_time:1.534102201461792
resp_time:1.3304438591003418
"""
# 20 gunicorn + gevent + flask
"""
resp_time:0.10559415817260742
resp_time:0.11883115768432617
resp_time:0.10376501083374023
resp_time:0.11776995658874512
"""

# 20 gunicorn + flask
"""
resp_time:0.08155584335327148
resp_time:0.08160281181335449
resp_time:0.0867300033569336
"""

# 200 gunicorn + flask
"""
resp_time:0.850884199142456
resp_time:0.8485920429229736
resp_time:0.8648147583007812
resp_time:0.8581891059875488
resp_time:0.9136908054351807
"""
