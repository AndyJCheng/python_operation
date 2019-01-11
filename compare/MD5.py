#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: MD5.py
@time: 2019/1/11 23:58
"""
import hashlib

d = hashlib.md5()

with open('diff.html') as f:
    for line in f:
        d.update(line.encode('utf8'))

print(d.hexdigest())
