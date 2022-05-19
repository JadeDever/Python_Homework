'''
Author: Jadedever
Date: 2022-05-03 17:47:11
LastEditors: Jadedever
LastEditTime: 2022-05-03 17:56:04
FilePath: /Python_Homework/lesson_7/top250csv.py
Description: r

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup
import csv

with open('豆瓣.csv','w',newline='') as file:
  csv_writer = csv.writer(file)
  # 写入表头
  header=['书名','评分','链接']
  csv_writer.writerow(header)

  headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

  res=requests.get('https://book.douban.com/top250/',headers=headers)
  soup=BeautifulSoup(res.text,'html.parser')
  items=soup.select('.item')

  for i in items:
    tag = i.select('div.pl2 a')[0]
    rating=i.select('.rating_nums')[0].text
    name=tag['title']
    link=tag['href']
    row=[name,rating,link]
    csv_writer.writerow(row)
    print(name,rating,link)