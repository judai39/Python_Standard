# 同4.2所示，需要一个进程通信的方式--队列Queue
from multiprocessing import Queue

# 1.队列的入队，出队
def queue_put_and_get():
    q=Queue(3)
    # 入队消息
    q.put('pyton')
    q.put('is')
    q.put('fun')
    print("队列中的消息数量：",q.qsize())
    print("队列是否已满：",q.full())

    # 出队消息
    print(q.get())
    print(q.get())
    print(q.get(True))#如果能get再get，没有数据了就不get
    print("队列是否为空",q.empty())

# 2.向满队列添加超时等待
def queue_full_timeout():
    q=Queue(2)
    q.put('python')
    q.put('python')
    # put()添加超时等待，如果到了规定时间队列还是满的会报错
    q.put('python',timeout=3)

if __name__ == '__main__':
    # queue_put_and_get()
    queue_full_timeout()