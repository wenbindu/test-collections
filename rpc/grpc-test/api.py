import time
import asyncio

async def get_result(u_id):
    await asyncio.sleep(0.5)
    if not u_id:
        return dict(data='', code=400)
    return dict(data=u_id, code=200)


async def get_result_short(u_id):
    await asyncio.sleep(1)
    if not u_id:
        return dict(data='', code=400)
    return dict(data=u_id, code=200)