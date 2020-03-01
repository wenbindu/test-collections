## rpc
> http vs zerorpc vs grpc


| service | 1000(s) | 10000(s)|
| --- | --- | --- |
| rest | 4.2s | 38-44s |
| zerorpc| 1.6s | 15-17s |
| grpc  | 0.7s | 6-8s |

#### 基于此给出以下建议：

1. http搭建简单，性能一般，适合小并发情景。
2. rpc总是比http要高效，对于内部服务沟通，同时性能有要求，建议采用rpc。
3. **grpc是推荐方案，虽然搭建过程最为复杂，但是性能较高，安全可观，同时支持各种语言。对于将来做服务发现以及自动注册，扩展迁移性好。**


## web-server
> gunicorn+flask vs gunicorn+gevent+flask

| service | 并发数量 | 响应耗时(ms) | redis耗时(ms)|
| --- | --- | --- | ---| 
| gunicorn+flask| 20 | -80+ | -5+ |
| - | 200 | -800+ | -5+ |
|gunicorn+gevent+flask| 20 | -100+ | -10+ |
| - | 200| -1300+ | -700+ |


> wrk test

| service | 并发数量 | redis耗时(ms)|requests/second |
| --- | --- | --- | --- |
| **sanic**| 400 | -20+ | *7600* |
| flask|400 | -10+ | 500 |
|gevent+flask| 400 | -300+ | 1300 |


#### 建议：
1. `gevent`的加入虽然使并发支持更高，但是响应时间增加了，需要权衡利弊。
2. `redis`在后台作为服务，在gevent的情况下导致`redis.get(key)`等操作耗时大大增加，随着并发越高，耗时越长。
3. `sanic` 作为asyncio的加入，并发数量提高，响应时间缩短，同时cpu占用率保持在60%[本地观察], `flask(gevent)`均使cpu达到100%。

