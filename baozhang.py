#!/bin/env python
#coding:utf8

def baozhang(func):
    def wrapper(*args,**kwargs):
        print "Starting the func"
        result = func(*args,**kwargs)
        print "End the func"
        return result
    return wrapper
    
@baozhang    
def test_func(*args,**kwargs):
    print args[0]
    
 
 test_func('this func')
