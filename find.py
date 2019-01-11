#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: find.py
@time: 2019/1/11 23:37
"""
import os
import fnmatch

path = os.path.abspath('.')

for root, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if fnmatch.fnmatch(filename, '*.py'):
            print(os.path.join(root, filename))
