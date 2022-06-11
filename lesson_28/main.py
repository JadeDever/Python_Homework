'''
Author: Jadedever
Date: 2022-06-11 22:18:36
LastEditors: Jadedever
LastEditTime: 2022-06-11 22:36:21
FilePath: /Python_Homework/lesson_28/main.py
Description: 

Copyright (c) 2022 by Jadedever, All Rights Reserved. 
'''
from article_until import get_word_count,get_difficulty

article = '''This is a photograph of our village.
Our village is in a valley.
It is between two hills.
The village is on a river.
Here is another photograph of the village.
My wife and I are walking along the banks of the river.
We are on the left.
There is a boy in the water.
He is swimming across the river.
Here is another photograph.
This is the school building.
It is beside a park.
The park is on the right.
Some children are coming out of the building.
Some of them are going into the park.
'''

new_words = [
  'photograph',
  'village',
  'valley',
  'between',
  'hills',
  'another',
  'prep',
  'wife',
  'along',
  'banks',
  'water',
  'swimming',
  'building',
  'park',
  'into'
]

word_list = get_word_count(article)
print( get_difficulty(word_list,new_words))
