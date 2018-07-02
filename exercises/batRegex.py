#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 20:16:35 2018

@author: ed
"""
import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()

mo = batRegex.search('Batmotorcycle lost a wheel')

mo == None

mo = batRegex.search('Batmotorcycle lost a wheel')

mo.group()

mo = batRegex.search('Batmotorcycle lost a wheel')
