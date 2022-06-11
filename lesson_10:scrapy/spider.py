'''
Author: Jadedever
Date: 2022-05-18 23:53:26
LastEditors: Jadedever
LastEditTime: 2022-05-18 23:53:28
FilePath: /Python_Homework/lesson_10:scrapy/spider.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import scrapy

# 定义一个类叫做 TitleSpider 继承自 scrapy.Spider
class TitleSpider(scrapy.Spider):
  name = 'title-spider'
  # 设定开始爬取的页面
  start_urls = ['https://www.appinn.com/category/windows/']

  def parse(self, response):
    # 找到所有 article 元素
    for article in response.css('article'):
      # 解析 article 下面 a 元素里的链接和标题
      a = article.css('h2.title a')
      if a:
        result = {
          'title': a.attrib['title'],
          'url': a.attrib['href'],
        }
        # 得到结果
        yield result

    # 解析下一页的链接
    next_page = response.css('a.next::attr(href)').get()
    if next_page is not None:
      # 开始爬下一页，使用 parse 方法解析
      yield response.follow(next_page, self.parse)