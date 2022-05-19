'''
Author: Jadedever
Date: 2022-05-03 18:35:59
LastEditors: Jadedever
LastEditTime: 2022-05-03 18:37:21
FilePath: /Python_Homework/lesson_8/office.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

import csv

filenames = ['2019-12-%02d-销售数据.csv' % (i + 1) for i in range(31)]

with open('12月销售数据汇总.csv', 'w', newline='') as file:
  csv_writer = csv.writer(file)

  for filename in filenames:
    with open(filename, newline='') as file:
      csv_reader = csv.reader(file)
      if filename == filenames[0]:  # 第一个文件保留表头
        rows = csv_reader
      else:
        rows = list(csv_reader)[1:]
      csv_writer.writerows(rows)