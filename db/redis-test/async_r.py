import asyncio
import aioredis
import time

async def direct(r):
    p = r.pipeline()
    p.sadd('test_info', '123')
    p.expire('test_info', 2)
    p.get('redis_test')
    p.set('redis_test', 5)
    p.expire('redis_test', 10)
    await p.execute()

async def go():
    redis = await aioredis.create_redis_pool(
        'redis://localhost')
    s = time.time()
    l = []
    for _ in range(5000):
        l.append(direct(redis))
    # print(l)
    await asyncio.gather(*l)
    print(time.time() - s)
    redis.close()
    await redis.wait_closed()
    
    

asyncio.run(go())