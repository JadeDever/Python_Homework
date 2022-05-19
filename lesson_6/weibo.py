'''
Author: Jadedever
Date: 2022-05-01 20:15:28
LastEditors: Jadedever
LastEditTime: 2022-05-01 20:59:20
FilePath: /Python_Homework/lesson_6/weibo.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import requests

class WeiboSpider:
  def __init__(self):
    self.session = requests.Session()
    self.headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
      'mweibo-pwa': '1',
      'x-requested-with': 'XMLHttpRequest',
      'cookie': 'loginScene=102003; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https%3A%2F%2Fm.weibo.cn%2Fcompose%2F; WEIBOCN_FROM=1110006030; SUB=_2A25PavBFDeRhGeFK71AQ-S3PyTiIHXVslJANrDV6PUJbkdANLUrukW1NQ0kewTuc-aKUWJJyuA80iKWSGn3jICBM; _T_WM=93583125798; XSRF-TOKEN=c786f0; MLOGIN=1; mweibo_short_token=625f55a140; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174'

    }
    self.session.headers.update(self.headers)

  def get_st(self):
    config_headers = {
      'origin': 'https://m.weibo.cn/',
      'referer': 'https://m.weibo.cn/'
    }
    self.session.headers.update(config_headers)

    config_req = self.session.get('https://m.weibo.cn/api/config')
    config = config_req.json()
    st = config['data']['st']
    return st

  def compose(self, content, st):
    compose_headers = {
      'origin': 'https://m.weibo.cn/',
      'referer': 'https://m.weibo.cn/compose/',
      'x-xsrf-token': st
    }
    self.session.headers.update(compose_headers)

    compose_data = {
      'content': content,
      'st': st
    }
    compose_req = self.session.post('https://m.weibo.cn/api/statuses/update', data=compose_data)
    print(compose_req.json())

  def send(self, content):
    st = self.get_st()
    self.compose(content, st)

  # 获取微博列表
  def get_weibo_list(self):
    params = {
      'sudaref':'security.weibo.com',
      'type':'uid',
      'value':'2139359753',
      'containerid':'1076032139359753',
    }
    weibo_list_req=self.session.get('https://m.weibo.cn/api/container/getIndex',params=params)
    weibo_list_data=weibo_list_req.json()
    weibo_list = weibo_list_data['data']['cards']
    return weibo_list

  # 点赞微博
  def vote_up(self,id):
    vodte_up_data={
      'id':id,
      'attitude':'heart',
      'st':self.get_st()
    }
    vodte_up_req = self.session.post('https://m.weibo.cn/api/attitudes/create',data=vodte_up_data)
    json = vodte_up_req.json()
    print(json['msg'])

  # 批量点赞微博
  def vote_up_all(self):
    st = self.get_st()
    vote_headers ={
      'x-xsrf-token':st
    }
    self.session.headers.update(vote_headers)
    weibo_list = self.get_weibo_list()
    for i in weibo_list:
      if i['card_type']==9:
        self.vote_up(i['mblog']['id'])


weibo = WeiboSpider()
# weibo.send('本条微博由 Python 发送')

weibo.vote_up_all()
