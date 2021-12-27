# -*- coding: utf-8 -*-
#这里写打包的逻辑
#1.读取文本
#2.读取图片
from bs4 import BeautifulSoup
import requests
import pdfkit
import re
import os
from PIL import Image



class Get_page():
    def __init__(self,url):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                         "/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
                  }
        self.path = "D:\Git_res\D_C_R\pack_wechat_article\\test\\" + "deszzj.pdf"
        self.response = requests.get(url,headers = self.headers)
        self.soup = BeautifulSoup(self.response.text)
        #print(self.soup.prettify())
        #print(self.response.text)
        #pdfkit.from_url(url,output_path= path)

        #----other----#
        self.title = self.get_title()


    def get_title(self):
        title = re.findall('<meta property="twitter:title" content="(.*?)"',self.response.text)
        return title[0]

    def pack_img(self):
        ## -----这里正则获取图片------#
        img_list = re.findall('data-src="(.*?)"',self.response.text)
        path = "test/图片{}.jpeg"
        x = 1
        for url in img_list:
            if url[-1] == 'f' or url[0] != 'h':
                continue
            img = requests.get(url, self.headers)
            with open(path.format(x), 'wb') as fd:  #todo 修改path
                fd.write(img.content)

        ##------这里是压缩图片------##todo 解决透明图片无法用jpeg存的问题

            img = Image.open(path.format(x))
            size = os.path.getsize(path.format(x)) / 1024
            if size > 200:
                try:
                    img.save(path.format(x))
                except:
                    img = img.convert("RGB")
                temp_path = "test/temp.jpeg"
                while size > 200:
                    width,height = round(img.size[0]*0.95),round(img.size[1]*0.95)
                    img= img.resize((width,height),Image.ANTIALIAS)
                    img.save(temp_path)
                    size = os.path.getsize(temp_path)/1024
                img.save(path.format(x))
            x += 1
        def del_temp():
            pass



if __name__ == '__main__':
    """
    测试网址
    https://mp.weixin.qq.com/s/hfZIzMuLkoriR9MIJ9oHKg
    https://mp.weixin.qq.com/s/vptYVJZXAcst2oPvdLkamQ
    """
    html=Get_page("https://mp.weixin.qq.com/s/vptYVJZXAcst2oPvdLkamQ")
    html.pack_img()