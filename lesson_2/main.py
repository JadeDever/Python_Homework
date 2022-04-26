'''
Author: Jadedever
Date: 2022-04-25 23:32:15
LastEditors: Jadedever
LastEditTime: 2022-04-26 00:06:14
FilePath: /Python_Homework/lesson_2/main.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup
import time

# 将获取一页图书数据代码封装成函数 get_one_page_data()
def get_one_page_data(page):
  # 豆瓣读书 Top 250 首页 URL
  base_url='https://book.douban.com/top250'
  # 定制消息头
  headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
  }
  count=page*25
  # 根据传入参数定制查询参数
  params={
    'start':count
  }
  # 发送带消息头和查询参数的请求
  res=requests.get(base_url,params=params,headers=headers)
  # 解析成 BeautifulSoup 对象
  soup=BeautifulSoup(res.text,'html.parser')
  # 提取出书名、作者、出版社信息并按行打印
  book_name_tags = soup.select('div.pl2 a')
  book_info_tags = soup.select('p.pl')

  for i in range(len(book_name_tags)):
    # 通过元素 title 属性提取书名
    name = book_name_tags[i]['title']
    # 获取书籍信息
    info=book_info_tags[i].text
    # 按“ / ”分割字符串
    info_list =info.split('/')
    # 结果列表中第一项为作者信息
    author=info_list[0]
    # 倒数第三项为出版社信息
    publisher=info_list[-3]
    # 打印书名、作者、出版社信息
    print(count+i+1,"《"+name+"》",author,publisher)

# 循环 10 次，分别获取第 1～10 页数据
for i in range(10) :
  get_one_page_data(i)
  time.sleep(2)