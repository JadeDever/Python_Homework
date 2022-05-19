'''
Author: Jadedever
Date: 2022-05-15 14:01:08
LastEditors: Jadedever
LastEditTime: 2022-05-15 14:01:29
FilePath: /Python_Homework/lesson_10/多线程.py
Description: 单线程与多线程对比

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import time
import requests
from concurrent import futures

# 假设我们要爬取 30 个网页
urls = ["https://wpblog.x0y1.com/?p=34"] * 30
session = requests.Session()

# 普通爬虫
start1 = time.time()
results = []
for url in urls:
  r = session.get(url)
  results.append(r.text)

end1 = time.time()
print("普通爬虫耗时", end1-start1, "秒")

# 多线程爬虫
executor = futures.ThreadPoolExecutor(max_workers=5)
start2 = time.time()
fs = []
for url in urls:
  f = executor.submit(session.get, url)
  fs.append(f)

futures.wait(fs)
result = [f.result().text for f in fs]
end2 = time.time()
print("多线程爬虫耗时", end2-start2, "秒")