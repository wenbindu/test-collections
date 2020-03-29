import time
import json
# import orjson
import rapidjson
import ujson
import simplejson


num = 10**6

m = {
    "timestamp": 1556283673.1523004,
    "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
    "task_level": [1, 2, 1],
    "action_status": "started",
    "action_type": "main",
    "key": "value",
    "another_key": 123,
    "and_another": ["a", "b"],
}

m1 = {
    "mid": 12345
}

s = '{"timestamp": 1556283673.1523004, "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7", "task_level": [1, 2, 1], "action_status": "started", "action_type": "main", "key": "value", "another_key": 123, "and_another": ["a", "b"]}'
s1 = '{"mid": 12345}'


def benchmark(name, dumps):
    start = time.time()
    for i in range(num):
        dumps(m)
    print(name, time.time() - start)

def benchmark_load(name, loads):
    start = time.time()
    for i in range(num):
        loads(s)
    print(name, time.time() - start)


# orjson only outputs bytes, but often we need unicode:
# benchmark("orjson", lambda s: orjson.dumps(s).decode('utf-8'))
benchmark("Python", json.dumps)
# benchmark("rapidjson", rapidjson.dumps)
benchmark("ujson", ujson.dumps)
benchmark("simplejson", simplejson.dumps)

# benchmark_load("orjson", lambda x: orjson.loads(x.encode('utf-8')))
benchmark_load("Python", json.loads)
# benchmark_load("rapidjson", rapidjson.loads)
benchmark_load("ujson", ujson.loads)
benchmark_load("simplejson", simplejson.loads)

# dumps
# orjson 1.227565050125122
# Python 5.861892938613892
# rapidjson 2.87353777885437
# ujson 1.669421911239624

# loads
# orjson 2.642509937286377
# Python 4.873814105987549
# rapidjson 3.068044900894165
# ujson 1.7971441745758057


# orjson==2.6.1
# python-rapidjson==0.9.1
# simplejson==3.17.0
# ujson==1.35