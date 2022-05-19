'''
Author: Jadedever
Date: 2022-05-18 23:51:14
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:04:46
FilePath: /Python_Homework/lesson_11/appinn/appinn/items.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class AppinnItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class Article(scrapy.Item):
  title = scrapy.Field()  # 标题
  time = scrapy.Field()   # 时间
  author = scrapy.Field()   # 作者
  score = scrapy.Field()  # 分数
  content = scrapy.Field()  # 内容