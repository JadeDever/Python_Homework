'''
Author: Jadedever
Date: 2022-05-03 15:47:48
LastEditors: Jadedever
LastEditTime: 2022-05-03 17:42:31
FilePath: /Python_Homework/lesson_7/csvTest.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import csv

# csv 读取文件
# with open('考勤统计表.csv',newline='') as file:
#   csv_reader = csv.reader(file)
#   for row in csv_reader:
#     print(row)

# csv 写文件
with open('考勤统计表2.csv','w',newline='') as file:
  csv_writer = csv.writer(file)
  rows=[
    ['姓名','考勤天数','迟到次数'],
    ['小贝',20,5],
    ['闻闻',22,0],
  ]
  csv_writer.writerows(rows)
  # for row in rows:
  #   csv_writer.writerow(row)