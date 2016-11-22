#!/bin/env python
#coding:utf8

from multiprocessing import Process
from time import ctime,sleep

def echo(name):
    print 'start the echo-%s at %s' %(name,ctime())
    sleep(3)
    print 'end the echo-%s at %s' %(name,ctime())
    
    
if __name__ == '__main__':
    print "Start the Main process at %s"  %(ctime())
    process = []
    #五个进程同时执行
    for i in range(5):
        p = Process(target=echo,args=(i,)) #if echo(**name),then Process(target=echo,kwargs={'name':i})
        process.append(p)
    for proces in process:
        proces.start()
    for proces in process:
        proces.join()
    print "All echo function is over at %s" %(ctime(),)
    
 
