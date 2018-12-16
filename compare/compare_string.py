#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: compare_string.py
@time: 2018/12/15 0:04
"""
import difflib

text1 = """Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug ，
        '模板引擎则使用 Jinja2 。Flask使用 BSD 授权。"""
text2 = """Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug ，
        '模板引擎则使用 Jinja2 。Flask1111使用 BSD 授权。"""

# d = difflib.Differ()
# diff = d.compare(text1.splitlines(), text2.splitlines())
#
# print('\n'.join(list(diff)))

# use HtmlDiff() class's make_file() to generate html doc
hd = difflib.HtmlDiff()
print(hd.make_file(text1.splitlines(), text2.splitlines()))

