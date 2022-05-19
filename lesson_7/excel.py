'''
Author: Jadedever
Date: 2022-05-03 15:04:00
LastEditors: Jadedever
LastEditTime: 2022-05-03 15:12:21
FilePath: /Python_Homework/lesson_7/excel.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

from openpyxl import Workbook

wb=Workbook()
sheet=wb.active

sheet.title ='8 月考勤统计表'
sheet['A1']='小贝'

row=['姓名','出勤天数','迟到次数']
sheet.append(row)

data=[
  ['姓名','出勤天数','迟到次数'],
  ['小贝',20,5],
  ['闻闻',22,0]
]

# 写入多行数据
for row in data:
  sheet.append(row)

# 保存 Excel 文件
wb.save('考勤统计.xlsx')