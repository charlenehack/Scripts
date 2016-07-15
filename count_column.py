#!/usr/bin/env python
#coding:utf8



def count_col(count_file):
    count = 0
    with open(count_file,'rb') as f:
        while True:
            buff = f.read(1024*200)
            if not buff:
                break
            count += buff.count('\n')
            print count


count_col('image.json')
