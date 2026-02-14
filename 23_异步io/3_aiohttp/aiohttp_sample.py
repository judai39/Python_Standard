# asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于
# HTTP连接就是IO操作，因此可以用单线程+async函数实现多用户的高并发支持。

# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
# pip install aiohttp
from aiohttp import web

async def index(request):
    text="<h1>Index Page</h1>"
    return web.Response(text=text,content_type="text/html")

async def hello(request):
    name=request.match_info.get("name","World")
    text=f"<h1>Hello,{name}</h1>"
    return web.Response(text=text,content_type="text/html")

app=web.Application()

# 添加路由
app.add_routes([web.get("/",index),web.get("/{name}",hello)])

if __name__=="__main__":
    web.run_app(app)