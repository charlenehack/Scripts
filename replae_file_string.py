#!/usr/bin/env python
#coding:utf8

with open('age.txt') as input_file:
    with open('new.txt','w') as output_file:
        for line in input_file:
            output_file.write(line.replace('name','Name'))
        

