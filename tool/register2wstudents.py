'''
Author: Jadedever
Date: 2022-05-12 23:28:38
LastEditors: Jadedever
LastEditTime: 2022-05-13 23:34:08
FilePath: /Python_Homework/tool/register2wstudents.py
Description: 注册两万学员

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

import urllib.parse
import json
import httplib2
import time


h = httplib2.Http(".cache")
url = "http://localhost:81/api/v1/users"
headers = {
    "X-DIATUH-USER": "1234567890",
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
        url, "POST", headers=headers, body=json.dumps(body))

    content = json.loads(content)
    
    print(content)
    print('成功注册一个用户')

    time.sleep(0.01)


def build_row_data(index):
    sIndex = str(index)

    username = 'stu'+sIndex
    phone = str(19000000000+index)
    return [username, phone]


def create_student(start, count):
    for i in range(count):
        user = build_row_data(start+i)
        register(user[0], user[1])

create_student(510, 9)
