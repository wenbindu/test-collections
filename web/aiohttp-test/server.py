from aiohttp import web
import asyncio

async def handle(request):
    u_id = 10
    return web.json_response(dict(data=u_id, code=200))

app = web.Application()
app.add_routes([web.get('/test', handle)])

if __name__ == '__main__':
    web.run_app(app, port=8081)

# gunicorn server:app -b localhost:8081 -k aiohttp.GunicornWebWorker -w 9