'''
Author: Jadedever
Date: 2022-05-15 14:03:46
LastEditors: Jadedever
LastEditTime: 2022-05-15 14:03:48
FilePath: /Python_Homework/lesson_10/多线程代码解析.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import time
import requests
# 导入 concurrent.futures 这个包
from concurrent import futures

urls = ["https://wpblog.x0y1.com/?p=34"] * 30
# 初始化一个线程池，最大的同时任务数是 5
executor = futures.ThreadPoolExecutor(max_workers=5)
session = requests.Session()

fs = []
for url in urls:
  # 提交任务到线程池
  f = executor.submit(session.get, url)
  fs.append(f)

# 等待这些任务全部完成
futures.wait(fs)
# 获取任务的结果
result = [f.result().text for f in fs]