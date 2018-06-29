#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:55:34 2018

@author: ed
"""
import pprint 

message = 'It was a bright cold day in April, and the clocks were striking thirteen'

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)