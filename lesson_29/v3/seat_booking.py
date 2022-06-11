'''
Author: Jadedever
Date: 2022-06-11 23:10:02
LastEditors: Jadedever
LastEditTime: 2022-06-11 23:49:14
FilePath: /Python_Homework/lesson_29/v3/seat_booking.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
# 导入 time 模块才能调用 sleep() 函数
import time

class SeatBooking:
  def get_row(self):
    input_row = input("预订第几排的座位呢？请输入 1～6 之间的数字")
    valid_row = [str(i + 1) for i in range(6)]
    
    # 如果用户输入不符合要求，就提醒用户重新输入
    while input_row not in valid_row:
      input_row = input('没有按要求输入哦，请输入 1～6 之间的数字')

    # 将行号转换为二维列表的行索引
    row = int(input_row) - 1
    return row
  
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

  def get_col(self):
    input_column = input('预订这一排的第几座呢？请输入 1～8 之间的数字')
    valid_column = [str(i + 1) for i in range(8)]

    # 如果用户输入不符合要求，就提醒用户重新输入
    while input_column not in valid_column:
      input_column = input('没有按要求输入哦，请输入 1～8 之间的数字')
      
    # 将列号转换为二维列表的列索引
    column = int(input_column) - 1
    return column

  # 指定座位号预订座位
  def book_seat(self, seats):
    # 获取符合系统要求的行列索引
    while True:
      row = self.get_row()
      column = self.get_col()

      # 如果列表中对应值为 '○' 则预订成功，否则预订失败
      if seats[row][column] == '○':
        print("正在为您预订指定座位...")
        time.sleep(0.7)
        seats[row][column] = '●'  # 预订成功，该座位将被标记为“已预约”
        print("预订成功！座位号：{}排{}座".format(str(row + 1), str(column + 1)))
        break
      else:
        print("这个座位已经被预订了哦")
        time.sleep(0.7)

  # 预订最靠前的座位
  def book_seat_at_front(self, seats):
    print("正在为您预订最靠前的座位...")
    time.sleep(0.7)
    # 外循环：遍历 seats 的行
    for row in range(6):
      # 内循环：遍历 seats 的列
      for column in range(8):
        # 若碰到没有被预订的座位
        if seats[row][column] == '○':
          seats[row][column] = '●' # 预订该座位
          print("预订成功！座位号：{}排{}座".format(row + 1, column + 1))
          return # 结束函数的执行，返回到它被调用的地方
    # 没有在循环内部结束程序，说明不存在没有被预订的座位
    print("非常抱歉🥺，所有座位都被订满了，无法为您保留座位")