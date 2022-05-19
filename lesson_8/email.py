'''
Author: Jadedever
Date: 2022-05-03 19:09:44
LastEditors: Jadedever
LastEditTime: 2022-05-03 19:09:46
FilePath: /Python_Homework/lesson_8/email.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
import yagmail

yag = yagmail.SMTP(user='xxxxxx@qq.com', password='xxxxxx', host='smtp.qq.com')
yag.send(to=['xxxxxx@qq.com'], subject='Python 发送邮件', contents='人生苦短，我用 Python')