#!/bin/env python
#coding:utf8

from elasticsearch import Elasticsearch as ES
from pprint import pprint


host = '192.168.0.65'
es = ES([{'host':host,'port':9200}])

msg = '当前用户'

res = es.search(
  index='graylog_0',   #索引名称，不指定时为ALL
  size=20,             #每次取20条,不指定默认取10条
  sort=['timestamp'],  #用以排序字段
  from_=0,             #从第五条开始取
  fields=['full_message','timestamp'],#只取该两列

  body={
      #DSL查询数据，定义想要的数据
      'query':{
          'bool':{
              'must':[
                  {'term':{'source':'development-web'}},
                  {'match_phrase':{'message':msg}},

              ],
      
              'filter':[
                  #{'term':{'message':''}},
                  {'range':{'timestamp':{'gte':'now-1d/d','lte':'now/d'}}},
              ]
           }
    }
 }

)

#打印总共匹配到多少条记录
pprint(res['hits']['total'])

#只取hists中的hits.另外还有_shards,timed_out,took键
if res['hits']['hits']:
    for hit in res['hits']['hits']:
        #如果不指定fields，需要将fields修改为_source,而且不需要加索引了
        print hit['fields']['timestamp'][0],  hit['fields']['full_message'][0]
        #break
        pass
else:
    print "Not Found"
