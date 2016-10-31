#!/usr/bin/python 
#coding: utf-8
import re
import urllib2
import sys

ip= sys.argv[1]
ipcnurl = "http://ip.cn/index.php?ip=" + ip
response = urllib2.urlopen(ipcnurl)
res = response.read()

pattern = "(您查询的 IP：<code>((([2]?[0-5]?[0-5]\.)|([1]?[0-9]?[0-9]\.)){3}(([2]?[0-5]?[0-5]\.)|([1]?[0-9]?[0-9]))))"
r = re.findall(pattern,res)
for i in r:
    print i[1],

pattern = "(所在地理位置：<code>(.*?)</code>)"
r = re.findall(pattern,res)
for i in r:
    print i[1]
