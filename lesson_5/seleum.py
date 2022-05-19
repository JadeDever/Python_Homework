'''
Author: Jadedever
Date: 2022-04-30 22:08:11
LastEditors: Jadedever
LastEditTime: 2022-04-30 22:25:58
FilePath: /Python_Homework/lession_5/seleum.py
Description:  
pip install selenium -i https://pypi.doubanio.com/simple

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''  

# 从 selenium 中导入 webdriver（驱动）
from selenium import webdriver
import time

# 选择 Chrome 浏览器打开
browser = webdriver.Chrome()
# 打开网页
browser.get('https://wpblog.x0y1.com')
time.sleep(2)
h1 = browser.find_element_by_tag_name('h1')
link = browser.find_element_by_class_name('more-link')
print(h1.text)
print(link.get_attribute('href'))
browser.quit()

# 用 BeautifulSoup 解析网页源代码
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# a_tags = soup.select('a')
# for tag in a_tags:
#   print(tag.text)
# browser.quit()