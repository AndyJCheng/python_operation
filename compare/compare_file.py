#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: compare_file.py
@time: 2019/1/9 22:43
"""
import difflib
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]


def readfile(filename):
    try:
        with open(filename) as f:
            text = f.read().splitlines()
            return text
    except IOError as error:
        print(error)
        sys.exit()


text1 = readfile(file1)
text2 = readfile(file2)

d = difflib.HtmlDiff()
print(d.make_file(text1, text2))




