import asyncio

async def wget(host):
    print(f"wget{host}...")
    # 异步并发-获取80端口号
    reader,writer=await asyncio.open_connection(host,80)
    # 发送HTTP请求：
    header=f"GET / HTTP/1.0\r\nHost:{host}\r\n\r\n"
    writer.write(header.encode("utf-8"))
    # 异步并发-内存缓冲区控制（相当于内存区的水坝，不断的直接write()操作会大量占用内存缓冲区，drain()会视情况暂停并发操作）
    await writer.drain()

    # 读取响应
    while True:
        # 异步并发-读取请求头每一行
        line=await reader.readline()
        if line==b"\r\n":
            break
        print("%s header > %s"%(host,line.decode("utf-8").rstrip()))
        # Ignore the body,close the socket
        writer.close()
        # 异步并发-等待写入响应
        await writer.wait_closed()
        print(f"Done {host}")

async def main():
    await asyncio.gather(wget("www.sina.com.cn"),wget("www.sohu.com"),wget("www.163.com"))

asyncio.run(main())