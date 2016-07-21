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

#拿到根节点名称,就是XML文件最外层的节点名称，这里是log4j:configuration
root_ele = xml_dom.documentElement

#通过根节点，获取根节点下的子节点。返回一个节点列表对象。这里获取根下appender
appender_ele_lst = root_ele.getElementsByTagName('appender')


for appender_ele in appender_ele_lst:
    #获取当前节点的属性值
    print appender_ele.getAttribute('name')
    print appender_ele.getAttribute('class')

    #如果获取不到指定的元素，为空列表。
    print appender_ele.getElementsByTagName('layout')

    #获取appender节点中的param子节点属性值
    for param_ele in appender_ele.getElementsByTagName('param'):
        #print param_ele.attributes.items()
        print param_ele.getAttribute('name')
        pass

    break
