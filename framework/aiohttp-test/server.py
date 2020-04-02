from aiohttp import web
import asyncio

async def handle(request):
    await asyncio.sleep(1)
    data = await request.json()
    if not data:
        return web.json_response(dict(data='', code=400))
    u_id = data.get('u_id')
    return web.json_response(dict(data=u_id, code=200))

app = web.Application()
app.add_routes([web.post('/spin', handle)])

if __name__ == '__main__':
    web.run_app(app, port=8081)

# gunicorn server:app -b localhost:8081 -k aiohttp.GunicornWebWorker -w 9