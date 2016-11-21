!#/bin/env python
#coding:utf8

import threading
from time import sleep,ctime

#1.通过定义一个类，来启动多线程。类继承自threading.Thread.并定义run方法

class Cheng(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func  #这个多线程要执行的函数
        self.args = args  #这个是多线程要执行函数的参数。
    def run(self):        #因为run方法不能带参数，所以在构造函数中带入，这此直接通过绑定信息执行函数
        self.func(*self.args)
    

def func(*args):
    print "Start the func at",ctime()
    print args
    print "End the func at",ctime()
    
  
if __name__ == "__main__":
    threads = []
    for i in range(2):
        t = Cheng(func,('arg1','arg2'))
        threads.append(t)
        
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "All is over"
