#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:30:12 2018

@author: ed
"""

spam = ['list1', 'list2', 'list3']

print(spam.index('list2'))

import copy

spam = ['A', 'B', 'C', 'D']
spam1 = spam

cheese = copy.deepcopy(spam)

cheese[1] = 50

print(cheese)
print(spam)
print(spam1)