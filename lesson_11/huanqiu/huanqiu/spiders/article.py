'''
Author: Jadedever
Date: 2022-05-19 22:29:44
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:30:13
FilePath: /Python_Homework/lesson_11/huanqiu/huanqiu/spiders/article.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import json
import scrapy
from huanqiu.items import Article

# 限制最多爬取 200 篇文章
ARTICLE_LIMIT = 200
# 用来标记当前文章列表中第一篇文章的位置
OFFSET = 0
# 科技人物列表链接
LIST_URL = 'https://tech.huanqiu.com/api/list2?node=/e3pmh164r/e3pmtmdvg&offset={}&limit=20'
# 文章链接
ARTICLE_URL = 'https://tech.huanqiu.com/article/{}'


class ArticleSpider(scrapy.Spider):
  name = 'article'
  allowed_domains = ['tech.huanqiu.com']
  start_urls = [LIST_URL.format(OFFSET)] # 从文章列表 OFFSET 位置开始爬取数据

  # 解析数码新闻列表页
  def parse(self, response):
    global OFFSET
    # 如果爬到限制文章数，结束本次爬取任务
    if OFFSET >= ARTICLE_LIMIT:
      return

    # 获取当前页面所有文章
    article_text = json.loads(response.text)
    article_list = article_text['list']
    # 遍历每篇文章
    for article in article_list:
      # 若文章加载不成功，aid 为空
      # 所以这里先判断 article 有没有 aid 键
      if article.get('aid'):
        # 获取文章 aid
        aid = article['aid']
        # 使用 parse_article() 方法根据 aid 爬取文章
        yield response.follow(ARTICLE_URL.format(aid), self.parse_article)

    OFFSET += 20
    # 使用 parse() 方法，从文章列表 OFFSET 位置开始爬取数据
    yield response.follow(LIST_URL.format(OFFSET), self.parse)

  # 解析文章页
  def parse_article(self, response: scrapy.Selector.response):
    article = Article()
    # 从 response 中提取出标题、时间、出处、作者、内容
    # 并将它们都存到 article 这个 item 里
    article['title'] = response.css('div.t-container-title > h3::text').get()
    article['time'] = response.css('div.metadata-info > p.time::text').get()
    article['source'] = response.css('span.source > span::text').get()
    article['author'] = response.css('span.author > span::text').get()
    article['content'] = response.css('article section p::text').getall()
    yield article