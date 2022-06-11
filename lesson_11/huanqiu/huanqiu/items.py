'''
Author: Jadedever
Date: 2022-05-18 23:51:14
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:25:57
FilePath: /Python_Homework/lesson_11/huanqiu/huanqiu/items.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class HuanqiuItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class Article(scrapy.Item):
  title = scrapy.Field()    # 标题
  time = scrapy.Field()     # 时间
  source = scrapy.Field()   # 出处
  author = scrapy.Field()   # 作者
  content = scrapy.Field()  # 内容