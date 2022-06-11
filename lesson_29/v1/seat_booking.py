'''
Author: Jadedever
Date: 2022-06-11 23:10:02
LastEditors: Jadedever
LastEditTime: 2022-06-11 23:10:03
FilePath: /Python_Homework/lesson_29/v1/seats_book.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# 导入 time 模块才能调用 sleep() 函数
import time

class SeatBooking:
  
  # 展示所有座位的预订信息
  def check_bookings(self, seats):
    print("正在为您查询该场次电影的预订状态...")
    time.sleep(0.7)
    print('从上到下为 1～6 排，从左至右为 1～8 座')
    print("======================")
    for row in seats:
      time.sleep(0.1)
      print('  '.join(row))
    print("======================")
    time.sleep(0.7)

  # 指定座位号预订座位
  def book_seat(self, seats):
    # 获取用户输入，转换为座位列表的行索引和列索引
    row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字")) - 1
    column = int(input("预订这一排的第几座呢？请输入 1～8 之间的数字")) - 1

    # 如果列表中对应值为 '○' 则预订成功，否则预订失败
    if seats[row][column] == '○':
      print("正在为您预订指定座位...")
      time.sleep(0.7)
      seats[row][column] = '●'  # 预订成功，该座位将被标记为“已预约”
      print("预订成功！座位号：{}排{}座".format(str(row + 1), str(column + 1)))
    else:
      print("这个座位已经被预订了哦")