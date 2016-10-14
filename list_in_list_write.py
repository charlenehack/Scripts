#!/bin/env python
#coding:utf8


import xlwt
import pymssql

conn = pymssql.connect(host+':3433',user,passwd,'xueshandai')
cursor = conn.cursor()
cursor.execute(sql)
row = 0
excel = xlwt.Workbook(encoding='utf8')
sheet = excel.add_sheet('sheet1')
for fetch in cursor:
    for col,data in enumerate(fetch):
        sheet.write(row,col,data)
    row += 1
excel.save(u'2_'+date+'.xlsx')
        
