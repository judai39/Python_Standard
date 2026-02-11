# 协程的引入：
# 有人可能会说，这两个任务毫无关联，并发操作有什么意义呢？对，但是如果两个任务分别是“播放视频的画
# 面”和“播放视频的声音”呢？我们都知道看视频要声画同步，有了协程就可以通过单一线程实现这个功能。

# 协程的作用，是在执行函数A时，可以随时中断，去执行函数B，然后再次中断继续执行函数A(可以自由切换)。
# 但这一过程并不是函数调用(没有调用语句)，这一整个过程看似像多线程，然而协程只有一个线程执行。
# Python对协程的支持是通过generator实现的。

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    # generator.send()方法用于向generator传入一个值，并恢复generator的执行。
    # 第一次调用send()方法时，必须传入None，因为此时generator还没有开始执行。
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

print(type(consumer()))#<class 'generator'>返回一个generator对象

c = consumer()
produce(c)
