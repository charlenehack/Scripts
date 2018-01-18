import time
import asyncio

class Cheng(object):
    def __init__(self):
        self.curr = 'a'

    def __repr__(self):
        return 'Class Cheng({0},{1})'.format(self.x, self.y)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr == 'z':
            raise StopIteration
        return self.curr
      

def grep(pattern):
    print('Pattern {0}'.format(pattern))
    while True:
        line = yield
        if pattern in line:
            print('True')

async def func():
    print(time.ctime())
    time.sleep(5)
    print(time.ctime())
    return 'func'

async def coro():
    print('function coro start Runging')
    x = await func()
    print('x',x) # x is 'func'.is fuc return value


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  
    loop.run_until_complete(coro())  
    loop.close()  
    #await实际上是挂起当前程序流，等待其后表达式的返回。如果后面没有表达式，
    #因为协程是在asyncio这个模块中运行。所以，控制权交给了loop。如果loop中
    #还注册了其他协程，那么它就会将其他协程拿来运行。

