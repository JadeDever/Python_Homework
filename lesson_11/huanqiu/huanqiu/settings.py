'''
Author: Jadedever
Date: 2022-05-18 23:51:14
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:32:18
FilePath: /Python_Homework/lesson_11/huanqiu/huanqiu/settings.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
BOT_NAME = 'huanqiu'

SPIDER_MODULES = ['huanqiu.spiders']
NEWSPIDER_MODULE = 'huanqiu.spiders'

# 遵循环球网的机器人协议
ROBOTSTXT_OBEY = True

# 输出成 JSON Lines 格式，也就是最后文件里每一行是一个完整的 JSON
FEED_URI = 'huanqiu_per.jsonl'
FEED_FORMAT = 'jsonlines'
FEED_EXPORT_ENCODING = 'utf-8'

# 加上默认 headers 防止反爬
DEFAULT_REQUEST_HEADERS = {
  "authority": "tech.huanqiu.com",
  "referer": "https://tech.huanqiu.com/",
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# 为了避免对被爬网站造成太大的压力，我们启动自动限速，设置最大并发数为 10
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 10