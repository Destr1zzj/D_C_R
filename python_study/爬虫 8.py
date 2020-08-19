#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import os
import base64
import time

def change_b64(page_num):
    today = time.strftime('%Y%m%d',time.localtime(time.time())) + '-' + str(page_num)
    print(today)
    today_b64 = base64.urlsafe_b64encode(str.encode(today)).decode('ascii')
    print(today_b64)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]
    pass

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img_url = 'http:' + each
            img = url_open(img_url)
            f.write(img)
    pass

def download_mm(folder = 'OOXX',pages =10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + str(change_b64(page_num)) +'#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


    pass

if __name__ == '__main__':
    download_mm()