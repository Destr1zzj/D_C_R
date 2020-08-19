#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import chardet
res = urllib.request.urlopen("http://www.fishc.com")
print(res.read(300))
# html = html.decode("utf-8")#网站信息转换为utf-8格式
def main():
    url = input("url = ")
    res2 = urllib.request.urlopen(url)
    html = res2.read()

    #decode
    encode = chardet.detect(html)['encoding']
    if encode =="GB2312":
        encode ="GBK"

    print("该网页使用的编码是： %s" % encode)

def main2():
    i = 0
    with open("urls.txt","r") as f:
        urls = f.read().splitlines()
        print (urls)
    for each in urls:
        res3 = urllib.request.urlopen(each)
        html = res3.read()
        encode = chardet.detect(html)['encoding']
        if encode == "GB2312":
            encode = "GBK"
        i += 1
        filename = "url_%d.txt" % i
        with open(filename, "w", encoding=encode) as each_file:
            each_file.write(html.decode(encode, "ignore"))


if __name__ =="__main__":

    main()