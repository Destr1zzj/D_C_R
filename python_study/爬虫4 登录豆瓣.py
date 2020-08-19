#!/usr/bin/python
# -*- coding: utf-8 -*-
#opener 学习文件
import urllib.request

url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http':'115.221.244.196'})
opener = urllib.request.build_opener(proxy_support)
print(opener.addheaders)
urllib.request.install_opener(opener)

res = urllib.request .urlopen(url)
html = res.read().decode('utf-8')
print(html)