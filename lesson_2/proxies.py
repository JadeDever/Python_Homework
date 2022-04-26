'''
Author: Jadedever
Date: 2022-04-25 23:54:30
LastEditors: Jadedever
LastEditTime: 2022-04-26 00:05:02
FilePath: /Python_Homework/lesson_2/proxies.py
Description: 代理

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup
from random import choice
import time

# 将获取一页图书数据代码封装成函数 get_one_page_data
def get_one_page_data(page, proxy):
  # 豆瓣读书 Top 250 首页 URL
  base_url = 'https://book.douban.com/top250/'
  # 定制消息头，内容省略
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
  # 发送带消息头、查询参数、代理的请求
  res = requests.get(
    base_url, headers=headers, params=params, proxies=proxy
  )
  # 解析成 BeautifulSoup 对象
  soup = BeautifulSoup(res.text, 'html.parser')
  # 提取出书名、作者、出版社信息并按行打印
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
    
# IP 代理池（瞎写的并没有用）
proxies_list = [
  {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
  },
  {
    "http": "http://10.10.1.11:3128",
    "https": "http://10.10.1.11:1080",
  },
  {
    "http": "http://10.10.1.12:3128",
    "https": "http://10.10.1.12:1080",
  }
]
# 循环 10 次，分别获取第 1～10 页数据
for i in range(1, 11):
  # 从 IP 代理池中随机选择一个
  get_one_page_data(i, choice(proxies_list))
  time.sleep(1)