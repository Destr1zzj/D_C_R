import os
# 列出当前目录下所有的文件
files = os.listdir('E:\\fuli\\10.27\\5041 new4')  # 如果path为None，则使用path = '.' 

for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名与扩展名
    # 如果后缀是jpg
    if portion[1] == '.7z 删除汉字再解压一次':
        # 重新组合文件名和后缀名
        newname = portion[0] + '.7z'
        os.rename(filename, newname)