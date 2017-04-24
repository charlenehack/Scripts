#!/usr/bin/env python
#coding:utf8

import xml.dom.minidom
import sys


#使用xml.dom.minidom解析XML时，要获取各节点的属性值。
#所有的XML解析，其实就是关注节点与属性两个东西就可以了
#因为XML是树结构，所要一层一层往下解析

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


##Type two
from xml.dom.minidom import parse
from xml.dom.minidom import Element


#定义过滤子节点带有'\n'函数
def filter_dom(doms):
    doms = [ node for node in doms if not hasattr(node,'data')]
    return doms

xml = parse('log4j.xml')
#获取根节点
root_ele = xml.documentElement
#获取当前节点下的所有子节点。这里是第二层节点
sec_ele = filter_dom(root_ele.childNodes)
#获取当前节点的指定属性值
root_ele.getAttribute('xmlns:log4j')
#获取当前节点所有的属性值与Value,返回列表数据
root_ele.arributes.items()


#写入示例
#写入使用DOM对象的appendChild()方法，它传入xml.dom.minidom.Element的实例对象
cheng_ele = Element('cheng') 
cheng_ele.setAttribute('name','cheng')
root_ele.appendChild(cheng_ele)
with open('new.xml','w') as f:
    f.write(root_ele.toprettyxml(encoding='utf8'))
