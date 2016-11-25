#!/bin/env python
#coding:utf8

#Use for Elasticsearch version 1.7.X

import time
from Queue import Queue
from threading import Thread,Event
from elasticsearch import Elasticsearch as ES
#import re



#定义搜索函数，根据关键字从Elasticsear中取出匹配内容
def  search(env,message,size,start,q):
    ent = Event()
    host = '10.168.169.51'
    client = ES([{'host':host,'port':9200}])
    resp = client.search(
        size=size,
        from_=start,
        sort="timestamp",
        fields=['timestamp','full_message','source'],
        body={
            'query':{
                'filtered':{
                    'query':[
                        {'query_string':{'query':'"'+message+'"'}},
                     ]
                 }
            },
            'filter':{
                'and':[
                    {'term':{'environment':env}}, #指定环境
                    {'range':{'timestamp':{'from':'2016-11-18 16:00:00.000','to':'2016-11-23 16:00:00.000'}}},
                    #{'regexp':{'full_message':message}},#regexp不支持中文，中文会匹配不到
                ]
            }              
        }
    )
    q.put((resp,ent))

#定义时间加八小时函数，因为默认ELK中的时间为标准UTC时间。
def time_plus(time_string):
    time_str,sec = time_string.encode('utf8').split('.')
    time_tup = time.strptime(time_str,'%Y-%m-%d %H:%M:%S')
    time_sec = time.mktime(time_tup) + 8*60*60
    add_time_tup = time.localtime(time_sec)
    return time.strftime('%Y-%m-%d %H:%M:%S',add_time_tup)+'.'+sec


#定义处理返回结果函数，写入文件
def write_f(msg,q):
    resp,ent = q.get()
    total = resp['hits']['total']
    print u'%s 关键词匹配 到   %s行'  %(msg,total)
    for hit in resp['hits']['hits']:
        log_msg = hit['fields']['full_message'][0]
        time_msg = hit['fields']['timestamp'][0]
        host = hit['fields']['source'][0]
        with open(msg+'.log','a+') as f:
            f.write(time_plus(time_msg)+':'+host.encode('utf8')+'- '+log_msg.encode('utf8')+'\n')
    ent.set()
        
        
#主程序开始
if __name__ == '__main__':
    time.clock()
    q = Queue()
    msgs = [
        '1182856',
        u'发送数据', #中文切记要加u字符串，英文不需要
    ]
    env = 'PRODUCTION'A
    size = 20000
    start = 0
    search_ts = []
    write_ts = []
    for msg in msgs:
        elk_t = Thread(target=search,args=(env,msg,size,start,q))
        w_t = Thread(target=write_f,args=(msg,q))
        search_ts.append(elk_t)
        write_ts.append(w_t)
        
    for t1,t2 in zip(search_ts,write_ts):
        t1.start()
        t2.start()
        t1.join()
        t2.join()    
print "Use the time is %2.5f" %(time.clock(),)
