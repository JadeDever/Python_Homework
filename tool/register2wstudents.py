'''
Author: Jadedever
Date: 2022-05-12 23:28:38
LastEditors: Jadedever
LastEditTime: 2022-06-01 15:45:27
FilePath: /Python_Homework/tool/register2wstudents.py
Description: 注册两万学员

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

import urllib.parse
import json
import httplib2
import time
from concurrent import futures


h = httplib2.Http(".cache")
# host = "http://localhost:81"
host = 'http://47.114.159.152:81'

register_url = host+'/api/v1/users'
login_url = host+'/api/v1/authorizations'

headers = {
    "X-DIATUH-USER": "1234567890",
    "Accept": 'application/json',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    "Content-type": "application/json"}  # 头


def register(username, phone):
    body = {
        'username': username,
        'password': '11223344',
        'phone': phone,
        'verification_key': '11111',
        'verification_code': '11111'
    }
    resp, content = h.request(
        register_url, "POST", headers=headers, body=json.dumps(body))

    content = json.loads(content)

    print(content)

    time.sleep(0.001)


def login(username):
    body = {
        'username': username,
        'password': '11223344'
    }
    resp, content = h.request(
        login_url, "POST", headers=headers, body=json.dumps(body))

    content = json.loads(content)

    print(content)

    # time.sleep(0.001)


def build_row_data(index):
    sIndex = str(index)

    username = 'stu'+sIndex
    phone = str(19000000000+index)
    return [username, phone]


def create_student(start, count):
    print('开始生成 %d 个用户' % (count))
    for i in range(count+1):
        user = build_row_data(start+i)
        register(user[0], user[1])
        print('成功注册第 %d 个用户，还剩 %d 个' % ((i+1), (count-i)))

# 注册用户
create_student(22551, 2000)


def login_student(start, count):
    print('开始登录 %d 个用户，从第 %d 个开始' % (count, start))
    for i in range(count+1):
        user = build_row_data(start+i)
        login(user[0])
        print('成功登录第 %d 个用户，还剩 %d 个' % ((i), (count-i)))

# 登录用户
# login_student(1, 10000)


# 多线程登录
# executor = futures.ThreadPoolExecutor(max_workers=10)

# groups=10    #分几个线程组同时登录
# count=1000 # 每组登录数量
# begin=1002   # 开始登录的基数
# for group in range(groups):
#     f=executor.submit(login_student,begin+group*count,count)
#     fs.append(f)

# futures.wait(fs)
# result = [f.result().text for f in fs]
# print(result)

# fs=[]
# start = 1001
# count = 3
# for i in range(count):
#     index = start+i
#     f=executor.submit(login,('stu'+str(index)))
#     fs.append(f)

# futures.wait(fs)

