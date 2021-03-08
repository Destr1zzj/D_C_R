# -*- coding: UTF-8 -*-//解决出现Non-ASCII character '\xe5' in file的问题
import PIL.Image
import os, sys

def convert(dir):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        PIL.Image.open(path).save("D:\Git_res\D_C_R\python_study\\alien_invasion\images\\done\\"+filename[:-4]+".bmp")//这个地方根据实际情况而定（存储图片的路径+图片名称+需要转换成的图片格式）
        print "%s has been changed!"%filename

if __name__ == '__main__':
   dir = raw_input('please input the operate dir:')//运行后输入要进行转换的图片的路径
   convert(dir)
————————————————
版权声明：本文为CSDN博主「scoolplayers」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37163122/article/details/78229512