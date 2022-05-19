'''
Author: Jadedever
Date: 2022-05-15 14:23:06
LastEditors: Jadedever
LastEditTime: 2022-05-15 14:48:55
FilePath: /Python_Homework/lesson_10/护坡.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests
from concurrent import futures
from bs4 import BeautifulSoup

headers={
  'cookie':'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22180c678bb574f9-059550d6a1f52f4-654e264f-1930176-180c678bb58ac4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22180c678bb574f9-059550d6a1f52f4-654e264f-1930176-180c678bb58ac4%22%7D; _HUPUSSOID=2f141c45-d6f3-44b4-855d-9d53ce356ba7; ua=16692901; u=96715898|6JmO5omRSlIwNTc2MDI4MjE1|268f|87d45e1630a9e50fc5b940012702a56b|aed1ccc8b823a894|aHVwdV9hMGUwYWMxZTBmN2JlMmRh; us=888d24c704c1ec3616bf98ade82743252a3be6a2f56b9726db9a7d3df840f606987d46a3a10b58b5c8b33480b019ba2289d548284201f03c9503978fb522343d; _CLT=00376064be821b71351c003dda774e37; Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1652597286; Hm_lpvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1652597286; Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615=1652597286; Hm_lpvt_4fac77ceccb0cd4ad5ef1be46d740615=1652597286',
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
}
session =requests.Session()

session.headers.update(headers)
executor = futures.ThreadPoolExecutor(max_workers=5)

# 解析列表页，得到内容链接
def parse_list_page(text):
  soup =BeautifulSoup(text,'html.parser')
  ul = soup.select('div.bbs-sl-web-post')[0].select('ul')[0]
  urls =[]
  prefix ='https://bbs.hupu.com'
  for li in ul.select('li'):
    url=li.div.select('a.p-title')[0].attrs['href']
    url=prefix+url
    urls.append(url)
  return urls

# 解析内容页，得到标题和回复
def parse_content_page(text):
  soup= BeautifulSoup(text,'html.parser')
  title =soup.select('h1.name')[0].text
  contents=[]
  for floor in soup.select('div.post-reply-list-container'):
    floor_box=floor.select('div.thread-content-detail')
    if not floor_box:
      return None,None 
    contents.append(floor_box[0].text)
  return title,contents

# 爬取列表页，解析出这一页的内容链接
def get_content_urls(list_url):
  res=session.get(list_url)
  content_urls=parse_list_page(res.text)
  return content_urls

# 爬取内容页，解析标题和回复
def get_content(content_url):
  res=session.get(content_url)
  title,contents=parse_content_page(res.text)

  return title,contents
# 获取内容页链接
fs=[]
url ='https://bbs.hupu.com/acg'
fs.append(executor.submit(get_content_urls,url))
futures.wait(fs)
content_urls=set()
for f in fs:
  for url in f.result():
    content_urls.add(url)

# 爬取内容页

fs=[]
for url in content_urls:
  fs.append(executor.submit(get_content,url))
  
futures.wait(fs)
result={}
for f in fs:
  title,contents=f.result()
  if title:
    result[title]=contents

print(result.keys())