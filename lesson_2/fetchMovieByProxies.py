'''
Author: Jadedever
Date: 2022-04-26 00:02:33
LastEditors: Jadedever
LastEditTime: 2022-04-26 00:10:54
FilePath: /Python_Homework/lesson_2/fetchMovieByProxies.py
Description: 爬取电影信息，设置代理

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests 
from bs4 import BeautifulSoup
import time
from random import choice

def get_one_page_data(page,proxy):
  base_url='https://movie.douban.com/top250'
  headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'

  }
  count=page*25
  params={
    'start':count
  }
  res=requests.get(base_url,params=params,headers=headers,proxies=proxy)

  soup=BeautifulSoup(res.text,'html.parser')
  
  link_tags = soup.select('div.hd a')
  i=0
  for link in link_tags:
    name_tag = link.select('span')[0]
    i=i+1
    print(count+i,"《"+name_tag.text+"》",link['href'])


# IP 代理池（瞎写的并没有用）
proxies_list = [
  {
    "http": "101.228.6.159", 
  } 
]

# 循环 10 次，分别获取第 1～10 页数据
for i in range(10):
  # 从 IP 代理池中随机选择一个
  get_one_page_data(i, choice(proxies_list))
  time.sleep(1)