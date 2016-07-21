#!/usr/bin/env python
#coding:utf8

import xml.dom.minidom
import sys


#使用xml.dom.minidom解析XML时，要获取各节点的属性值。
#使用树的方式进行解析。一层一层往下解析

try:
    xml_dom = xml.dom.minidom.parse(sys.argv[1])
except Exception:
    print "Input the parse file"

#拿到根节点名称
root_ele = xml_dom.documentElement

#通过根节点，获取根节点下的子节点。返回一个节点列表对象。这里获取根下moive
moive_ele_lst = root_ele.getElementsByTagName('movie')

for moive in moive_ele_lst:
    #获取title属性值。因为直接在该节点上
    print moive.getAttribute('title')
    print '*' * 100
    #获取该节点的Type属性值，在子节点下，同时因为只有一个。所以直接取序列索引0
    moive_type_ele = moive.getElementsByTagName('type')[0]
    #获取type的属性值
    print moive_type_ele.childNodes[0].data
    break
