#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:51:45 2018

@author: ed
"""

import re

batRegex = re.compile(r'Bat(wo)?man')

var = batRegex.search('The adventure of Batman')

print(var.group())

var = batRegex.search('The adventures of Batwoman')

print(var.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
var = phoneRegex.search('My phone number is 415-555-1234. Call me')
print(var.group())

