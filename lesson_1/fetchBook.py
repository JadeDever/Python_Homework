'''
Author: Jadedever
Date: 2022-04-24 23:48:06
LastEditors: Jadedever
LastEditTime: 2022-04-24 23:48:06
FilePath: /spiderLearn/lesson_1/fetchMovie copy.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
'''
Author: Jadedever
Date: 2022-04-24 23:19:40
LastEditors: Jadedever
LastEditTime: 2022-04-24 23:43:46
FilePath: /spiderLearn/lesson_1/fetchMovie.py
Description: 爬取豆瓣电影

Copyright (c) 2022 by Jadedever, All Rights Reserved.
'''
import requests

from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

res = requests.get('https://book.douban.com/top250', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

book_name_tags = soup.select('div.pl2 a')
# print(book_name_tags)
book_info_tags = soup.select('p.pl')
# print(book_info_tags)

# 遍历所有书籍信息元素
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
    print(i+1,"《"+name+"》",author,publisher)
