#!/bin/env python
#coding:utf8

import MySQLdb
import sys
import csv

try:
    f = file(sys.argv[1])
    try:
        conn = MySQLdb.connect(
               host='192.168.0.148',
               user='root',
               passwd='123qwe',
               db='django',
               charset='utf8'
               )
    except Exception,e:
        print e
    csv_obj = csv.reader(f)
    for line in csv_obj:
        insert_sql = "INSERT INTO test VALUES({id},{value},{type},{start_date},{end_date})".format(
                   id=int(line[0]),value=int(line[1]),type=int(line[2]),
                   start_date="'"+line[3].replace('/','-')+"'",
                   end_date="'"+line[4].replace('/','-')+"'"
                   )
        cur = conn.cursor()
        cur.execute(insert_sql)
        conn.commit()
        cur.close()
    conn.close()
except Exception,e:
    print e

