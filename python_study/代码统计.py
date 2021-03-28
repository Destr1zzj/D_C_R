import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "[%s]源文件【%d】个，源代码 【%d】行\n" %(i,file_list[i],lines)
    title = "结果"
    msg = '目前共编写 %d 行代码，完成进度 %.2f%%\n离10万行代码还差%d行。'%(total,total/1000,100000-total)
    g.textbox(msg,title,text)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print("正在计算文件：%s...\\" % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass
    return lines

def search_file(start_dir):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file)
            #统计文件
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            #统计源代码
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines


        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)

target = ['.c','.cpp','.py','.cc','.java','.pas','.asm']
file_list = {}
source_list = {}

g.msgbox("请打开代码文件夹......\\","统计代码量")
path = g.diropenbox("请选择：")

search_file(path)
show_result(path)
show_result(file_list)
show_result(source_list)





