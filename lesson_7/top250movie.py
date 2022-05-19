'''
Author: Jadedever
Date: 2022-05-03 18:13:49
LastEditors: Jadedever
LastEditTime: 2022-05-03 18:22:20
FilePath: /Python_Homework/lesson_7/top250movie.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests
from openpyxl import Workbook
import time

def get_data():
  data=[]
  headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'referer': 'http://movie.mtime.com/'
  }

  # 以 50 为一页，共 4 页
  for num in range(1,5):
    params={
      "tt": "{}".format(int(time.time() * 1000)),
      # 电影id：209164
      "movieId": "209164",
      "pageIndex": "{}".format(num),
      "pageSize": "50",
      # 按最新评论排序
      "orderType": "2"
    }

    res = requests.get(
      'http://front-gateway.mtime.com/library/movie/comment.api',
      params=params,
      headers=headers
    )

    comment_list = res.json()['data']['list']
    for comment in comment_list:
      row = [comment['nickname'], comment['content'], comment['rating']]
      data.append(row)
    # 暂停一下，防止爬取太快被封
    time.sleep(1)
  return data


def save_data():
  rows = get_data()
  wb=Workbook()
  sheet=wb.active
  sheet.title='电影列表'
  for row in rows:
    sheet.append(row)
  wb.save('电影列表.xlsx')

save_data()