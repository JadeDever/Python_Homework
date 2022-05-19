'''
Author: Jadedever
Date: 2022-04-26 23:58:24
LastEditors: Jadedever
LastEditTime: 2022-04-27 00:23:14
FilePath: /Python_Homework/lesson_3/fetchMultiPage.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''


import requests
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'referer': 'http://movie.mtime.com/'
}

for num in range(1, 6):
    params = {
        "tt": "{}".format(int(time.time()*1000)),
        "movieId": "251525",
        "pageIndex": "{}".format(num),
        "pageSize": "20",
        "orderType": "2"
    }
    res = requests.get('http://front-gateway.mtime.com/library/movie/comment.api',
                       params=params,
                       headers=headers)
                      
    comments_list = res.json()['data']['list']

    for i in comments_list:
        print("用户：", i['nickname'])
        print("评论：", i['content'])

    time.sleep(1)
