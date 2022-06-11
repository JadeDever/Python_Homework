'''
Author: Jadedever
Date: 2022-05-18 23:51:14
LastEditors: Jadedever
LastEditTime: 2022-05-19 22:18:27
FilePath: /Python_Homework/lesson_11/appinn/appinn/pipelines.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AppinnPipeline:
    def process_item(self, item, spider):
        if item.get('score'):
            # 把 item 的 score 变成整数
            item['score'] = int(item['score'])
        if item['score'] < 3:
            raise DropItem('去掉 3 分以下的文章')
        return item
