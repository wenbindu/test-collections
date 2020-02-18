import time
import requests
import random

def get_result():
    data = {'u_id': str(random.randint(0,1000))}
    r = requests.post('http://127.0.0.1:8081/spin', json=data).json()
    print(r)

if __name__ == '__main__':
    start = time.time()
    for _ in range(0,10000):
        get_result()
    print('-' * 10)
    print(time.time() - start)

# http: 1000 4.2s   10000 38-44s