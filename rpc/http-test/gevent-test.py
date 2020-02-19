import gevent
import requests
import random

def req():
    data = {'u_id': str(random.randint(0,1000))}
    r = requests.post('http://127.0.0.1:8081/spin', json=data).json()
    print(r)

reqs = []

for _ in range(10000):
    g = gevent.spawn(req)
    reqs.append(g)

print('*' * 10)

list(map(lambda g: g.get(), reqs))