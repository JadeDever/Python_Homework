'''
Author: Jadedever
Date: 2022-04-26 23:37:12
LastEditors: Jadedever
LastEditTime: 2022-04-26 23:56:11
FilePath: /Python_Homework/lesson_3/fetchComments.py
Description: 获取评论--动态数据

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'referer': 'http://movie.mtime.com/'
}
params = {
   # 将当前时间戳转为毫秒后取整，作为 tt 的值
  "tt": "{}".format(int(time.time() * 1000)),
  "movieId": "251525",
  "pageIndex": "2",
  "pageSize": "20",
  "orderType": "1"
}

res = requests.get(
  'http://front-gateway.mtime.com/library/movie/comment.api',
  params=params,
  headers=headers
)  
comment_list = res.json()['data']['list']
for i in comment_list:
  print("用户：", i['nickname'])
  print("评论：", i['content'])
 