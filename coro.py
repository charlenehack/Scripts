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
