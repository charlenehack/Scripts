#!/bin/env python
#coding:UTF8

import requests
import time
import re
import random


headers = {
    'user-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accpet-Encoding':'gzip, deflate, br',
}

def get_userdata(resp_string):
    reg = re.compile('<.*hidden.*>')
    user_id = reg.findall(resp_string)[0].split()[-2].split('"')[-2]
    value = reg.findall(resp_string)[0].split()[-1].split('"')[-2]
    user_data = {'accessSource':'100',user_id:value}
    return user_data

def login_frb(user,passwd):
    user_data = {'urltype':'login_url','j_username':user,'j_password':passwd}
    s = requests.Session()
    s.get('https://www.frbao.com/')
    time.sleep(1)
    s.get('https://www.frbao.com/login.html')
    time.sleep(3)
    s.post('https://www.frbao.com/hy/login',headers=headers,data=user_data)
    time.sleep(0.5)
    s.get('https://www.frbao.com/hy/authorization!loginSuccess.action',headers=headers)
    time.sleep(1)
    s.get('https://www.frbao.com/hy/myintegral.html',headers=headers)
    time.sleep(1)
    resp = s.get('http://jf.frbao.com/',headers=headers)
    qindao_data = get_userdata(resp.content)
    s.post('http://jf.frbao.com/sign/dailySignV2.do',headers=headers,data=qindao_data)
    time.sleep(2)
    s.get('http://www.frbao.com/hy/logout')


if __name__ == '__main__':
    run_day = ''
    run_hour = random.randint(10,12)
    run_min = random.randint(0,59)
    curr_day = time.localtime().tm_mday
    while not run_day:
        curr_hour = time.localtime().tm_hour
        curr_min = time.localtime().tm_min
        if curr_hour == run_hour and curr_min == run_min:
            run_day = curr_day
            login_frb(username,password)
            print 'runing at %s:%s' %(curr_hour,curr_min)
            break
        time.sleep(50)
