'''
Author: Jadedever
Date: 2022-05-12 09:30:30
LastEditors: Jadedever
LastEditTime: 2022-06-09 15:00:52
FilePath: /Python_Homework/tool/create2wstudent.py
Description: 生成 2 万学生列表

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''

from openpyxl import Workbook
from random import choice
import csv

## type=xlsx or csv
def create_student(start, count, type='xlsx'):
    filename = '/Users/afujade/Desktop/data/模拟学生数据表'+str(start)+"-"+str(count+start-1)+"."+type

    if type == 'xlsx':
        sheet_title = str(start)+"-"+str(count+start)

        wb = Workbook()
        sheet = wb.active
        sheet.title = sheet_title
        header = [['提示占位'], ['用户名', '邮箱', '密码', '手机号',
                             '姓名', '性别', '公司', '职业', '行业', '身份证号']]

        for row in header:
            sheet.append(row)

        for i in range(count): 
            sheet.append(build_row_data(start+i))

        wb.save(filename)
        print('文件创建成功：'+filename)

    # 创建简易登录文件
    elif type == 'csv':
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            header = ['用户名', '密码']
            csv_writer.writerow(header)

            for i in range(count):
                csv_writer.writerow(build_row_data(start+i, True))

        print("文件创建成功："+filename)

    else:
        print("类型错误")


industries = ['医疗器械', '食品', '药品', '化妆品']
pwd = '11223344'


def build_row_data(index, is_short=False):
    sIndex = str(index)

    username = 'stu'+sIndex

    if is_short:
        return [username, pwd]
    else:
        email = ''
        phone = str(19000000000+index)
        truename = '学生'+sIndex
        gender = ''
        company = '上海名育职业技能培训有限公司'+sIndex
        job = '职业'+sIndex
        industry = choice(industries)
        id_card = '530328199110'+str(100000+index)

        return [username, email, pwd, phone, truename, gender, company, job, industry, id_card]


per_count=900
for i in range(27):
    start = i*per_count if i>0 else 1
    create_student(start, per_count,'xlsx')
    # create_student(500, 500,'xlsx')
