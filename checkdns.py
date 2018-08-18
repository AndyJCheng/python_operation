#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: checkdns.py
@time: 2018/ 8/14 22:43
@desc: check dns service
"""
import dns.resolver as dns
import requests

iplist = []
appdomain = "www.baidu.com"


def get_ip(domain):
    A = dns.query(domain, 'A')
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)


def check_ip(ip):
    response = requests.get('http://'+ip + ':80')
    if response.status_code == 200:
        print(ip + 'is correct')
    else:
        print(ip + 'is wrong')


get_ip(appdomain)
for ip in iplist:
    check_ip(ip)
