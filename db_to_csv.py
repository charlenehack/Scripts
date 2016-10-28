#!/bin/env python
#coding:UTF8

import csv
import pymssql
import time


time.clock()
user = 'sa'
passwd = 'xsd123!@#'
host = '192.168.0.71'
conn = pymssql.connect(host,user,passwd,'xueshandai_dev')
cursor = conn.cursor()
cursor.execute('SELECT top 10 id,username,password,reg_time from member')
with open('cf.csv','wb') as f:
    fileds = ['id','username','password']
    csv_writer = csv.DictWriter(f,fileds)
    csv_writer.writeheader()
    for fetch in cursor:
        csv_writer.writerow({'id':fetch[0],'username':fetch[1].encode('utf8'),'password':fetch[2].encode('utf8')})
  
