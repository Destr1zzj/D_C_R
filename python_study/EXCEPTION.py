#-*- coding : utf-8 -*-
# coding: utf-8

#  os模块学习----寻找txt中某个关键字

import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print('行数【%s】,第【%s】位置' %(each_key,str(key_dict[each_key])))

def pos_in_line(line,key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)
        begin = line.find(key, begin+1)

    return pos

def search_in_file(file_name,key):
    f = open(file_name, encoding="unicode_escape")
    count = 0
    key_dict = dict()

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line,key)
            key_dict[count] = pos

    f.close()
    return key_dict

def search_files(key, detail):
    all_flies = os.walk(os.getcwd())
    txt_files = []
    n = 0

    for i in all_flies:
        for each_file in i[2]:
            n += 1
            # print(i, '第%d次' % n)
            # print(i[2],'第%d次' % n)
            print(each_file, '第%d次' % n)
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('==================================================')
            print('file:[%s] key:[%s]' % (each_txt_file, key))
            if detail == 'Y':
                print_pos(key_dict)

################################

key = input('please put this in files , key = ')
detail = input('''if need detail ,please enter y \n''' '>>>')
search_files(key, detail)