import aioredis
import asyncio
from sanic import Sanic
from sanic.response import json
import time
import uvloop

app = Sanic(__name__)
app.config.ACCESS_LOG = False

loop = asyncio.get_event_loop()
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())



@app.listener('before_server_start')
async def before_server_start(app, loop):
	# app.redis_pool = await aioredis.create_connection( ('127.0.0.1', '6379'), loop=loop )
    app.redis_pool = await aioredis.create_redis_pool(
        'redis://127.0.0.1', encoding='utf-8')


@app.listener('after_server_stop')
async def after_server_stop(app, loop):
	app.redis_pool.close()
	await app.redis_pool.wait_closed()


@app.route("/test", methods=['GET', 'POST'])
async def test(request):
    s = loop.time() * 1000
    data = await app.redis_pool.get('test')
    e = loop.time() * 1000
    print('spend: {}'.format(int(e-s)))
    return json(dict(code=data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)



# gunicorn server:app --bind 0.0.0.0:8081 --worker-class sanic.worker.GunicornWorker
