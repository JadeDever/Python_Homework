'''
Author: Jadedever
Date: 2022-04-24 23:19:40
LastEditors: Jadedever
LastEditTime: 2022-04-25 00:15:24
FilePath: /spiderLearn/lesson_1/fetchMovie.py
Description: 爬取豆瓣电影

Copyright (c) 2022 by Jadedever, All Rights Reserved.
'''
import requests

from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

res = requests.get('https://movie.douban.com/top250', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

link_tags = soup.select('div.hd a')
i=0
for link in link_tags:
  name_tag = link.select('span')[0]
  i=i+1
  print(i,"《"+name_tag.text+"》",link['href'])
  
