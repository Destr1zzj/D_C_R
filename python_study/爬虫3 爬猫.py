#!/usr/bin/python
# -*- coding: utf-8 -*-
import easygui as g
import urllib.request

def main():
    msg = "cat size"
    title = "downloda a cat!"
    fieldNames = ['width:','height:']
    fieldValues = []
    size = width,height = 400,600
    fieldValues = g.multenterbox(msg,title,fieldNames,size)

    while True:
        if fieldValues == None:
            break
        errmsg = ""
        try:
            width = int(fieldValues[0].strip())
        except:
            errmsg += "宽度必须为整数"


        try:
            height = int(fieldValues[1].strip())
        except:
            errmsg += "高度必须为整数"

        if errmsg == "":
            break

        fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)

    url = "http://placekitten.com/g/%d/%d" % (width,height)
    response = urllib.request.urlopen(url)
    cat_img = response.read()
    filepath = g.diropenbox("download in:")
    if filepath:
        filename = '%s/cat_%d_%d.jpg'%(filepath,width,height)
    else:
        filename =  'cat_%d_%d.jpg'%(width,height)
    with open (filename , 'wb') as f:
        f.write(cat_img)


if __name__ == "__main__":
    main()




