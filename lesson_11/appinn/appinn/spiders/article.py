'''
Author: Jadedever
Date: 2022-05-19 22:06:09
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:10:38
FilePath: /Python_Homework/lesson_11/appinn/appinn/spiders/article.py
Description: 
找到当前页面中所有文章的链接，生成解析请求，Scrapy 会用 parse_article() 方法解析文章链接；
找到下一个页面的链接，生成解析请求，Scrapy 会用 parse() 方法解析它找到的文章列表链接。

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import scrapy
from appinn.items import Article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['www.appinn.com']
    start_urls = ['https://www.appinn.com/category/windows/']

    def parse(self, response):
        # 找到所有文章的链接，通知 Scrapy 用 parse_article 方法解析
        for article_url in response.css('article h2.title a::attr(href)').getall():
            if not article_url:
                continue
            # 后续请求和解析
            yield response.follow(article_url, self.parse_article)

        # 找到下一页的链接，通知 Scrapy 用 parse 方法解析
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            # 后续请求和解析
            yield response.follow(next_page, self.parse)
        

    def parse_article(self, response):
        article = Article()
        # 从 response 里提取出标题、时间、作者、分数和内容
        # 并将它们都存到 article 这个 item 里
        article['title'] = response.css('h1.title::text').get()
        article['time'] = response.css('span.thetime span::text').get()
        article['author'] = response.css('span.theauthor span a::text').get()
        article['score'] = response.css('em strong::text').get()
        contents = response.css('div.post-single-content *::text').getall()
        article['content'] = '\n'.join(contents)
        # 给出结果
        yield article

