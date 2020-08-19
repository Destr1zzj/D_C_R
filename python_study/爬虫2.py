#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import json
import time

# res = urllib.request.urlopen("http://placekitten.com/g/1920/1080")
# cat_img = res.read()
#
# with open("cat.jpg","wb") as f:
#     f.write(cat_img)

while True:
    content = input('翻译内容（q！退出）==')
    if content == 'q!':
        break
    #translate
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}
    data['i'] = content
    data['from'] ='AUTO'
    data['to']='AUTO'
    data['smartresult']= 'dict'
    data['client'] ='fanyideskweb'
    data['salt']='15830435723965'
    data['sign']='cb92863af34221e4d55abf92aa38cbaa'
    data['ts']='1583043572396'
    data['bv']='6b71bda0785160f59caa738e5cbcdf96'
    data['doctype'] ='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action:']= 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62')
    response = urllib.request.urlopen(req)
    # code = response.getcode()
    # print(code)
    html = response.read().decode('utf-8')
    html_2 = json.loads(html)
    print ("translate == %s"% (html_2["translateResult"][0][0]['tgt']))
    print('3s 后可重新使用。。。/')
    time.sleep(3)
