'''
Author: Jadedever
Date: 2022-05-19 22:34:29
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:34:37
FilePath: /Python_Homework/lesson_11/huanqiu/check_article.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# # 导入 json 库以使用 JSON 函数
# import json

# # 打开 huanqiu_per.jsonl 文件
# with open('huanqiu_per.jsonl') as f:

#   # JSON Lines 格式支持用 for 循环按行遍历
#   for line in f:
#   # JSON 中保存的是 object 数据
#   # 使用 json.loads() 解析，得到的数据为字典类型
#     data = json.loads(line)

#     # 打印字典 data 中 'title' 键的值（也即文章标题）
#     if data.get('title'):
#       print(data['title'])


# 导入 json 库以使用 JSON 函数
import json

# 打开 huanqiu_per.jsonl 文件
with open('huanqiu_per.jsonl') as f:

  word = '腾讯'
  article_count = 0
  word_count = 0

  # JSON Lines 格式支持用 for 循环按行遍历
  for line in f:
  # JSON 中保存的是 object 数据
  # 使用 json.loads() 解析，得到的数据为字典类型
    data = json.loads(line)

  # 统计共有多少篇文章，文章标题中腾讯共被提及多少次
    if data.get('title'):
      article_count += 1
      word_count += data['title'].count(word)

print('环球网科技人物的前{}篇文章中，有{}篇与{}相关'.format(article_count, word_count, word))