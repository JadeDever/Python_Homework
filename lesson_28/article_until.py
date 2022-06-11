'''
Author: Jadedever
Date: 2022-06-11 22:22:26
LastEditors: Jadedever
LastEditTime: 2022-06-11 22:51:57
FilePath: /Python_Homework/lesson_28/article_until.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''


def get_word_count(article):
  word_list = article.lower().replace('.', '').split()
  word_count = {}
  for word in word_list:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  return word_count

def get_difficulty(word_count,new_words):
  difficulty=0
  for word in new_words:
    if word in word_count:
      difficulty=difficulty+word_count[word]*5
  return difficulty

