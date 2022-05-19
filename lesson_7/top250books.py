'''
Author: Jadedever
Date: 2022-05-03 15:29:33
LastEditors: Jadedever
LastEditTime: 2022-05-03 15:41:26
FilePath: /Python_Homework/lesson_7/top250books.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
res = requests.get('https://book.douban.com/top250/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

items = soup.select('.item')

wb=Workbook()
sheet = wb.active
sheet.title = '豆瓣图书 Top250'
# 写入表头
header=['书名','评分','链接']
sheet.append(header)

for i in items:
  tag=i.select('div.pl2 a')[0]
  rating =i .select('.rating_nums')[0].text
  name=tag['title']
  link=tag['href']
  # 写一行数据
  row= [name,rating,link]
  sheet.append(row)
  print(name,rating,link)

wb.save('豆瓣图书.xlsx')