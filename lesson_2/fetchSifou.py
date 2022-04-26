'''
Author: Jadedever
Date: 2022-04-25 23:50:37
LastEditors: Jadedever
LastEditTime: 2022-04-25 23:50:38
FilePath: /Python_Homework/lesson_2/fetchSifou.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup
import time

def get_one_page_data(page):
  # 思否搜索页 URL
  sf_search_url = 'https://segmentfault.com/search'
  # 定制消息头
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
  }
  # 定制查询参数
  params = {
    'q': 'python', # 搜索关键字
    'type': 'article', # 搜索范围：文章
    'page': page
  }
  # 发送请求
  res = requests.get(sf_search_url, headers=headers, params=params)
  res.encoding = 'utf-8'
  # 解析请求
  soup = BeautifulSoup(res.text, 'html.parser')
  # 获取文章标题所在元素
  title_tags = soup.select('h5')
  # 提取文章标题内容
  titles = [tag.text for tag in title_tags]
  # 打印摘要
  if title_tags:
    print('在第 {} 页获取了 {} 篇文章信息，有 {} 等'.format(
      page, len(titles), titles[0]
    ))
  else:
    print('获取第 {} 页内容失败'.format(page))

# 循环 5 次，获取 5 页数据
for i in range(1, 6):
  get_one_page_data(i)
  time.sleep(1)