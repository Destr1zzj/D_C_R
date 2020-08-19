import os

def count_file():
    all_files = os.listdir(os.curdir)
    type_dict = dict()

    for each_file in all_files:
        if os.path.isdir(each_file):
            type_dict.setdefault('文件夹',0)
            type_dict['文件夹'] += 1
        else:
            ext = os.path.splitext(each_file)[1]
            type_dict.setdefault(ext , 0)
            type_dict[ext] += 1

    for each_type in type_dict.keys():
        print('该文件下[%s]的文件共有 %d 个' %(each_type , type_dict[each_type]))

def calc_file():
    all_files = os.listdir(os.curdir)
    file_dict = dict()

    for each_file in  all_files:
        if os.path.isfile(each_file):
            file_size = os.path.getsize(each_file)
            file_dict[each_file] = file_size

    for each in file_dict.items():
        print('%s[%dbytes]' % (each[0],each[1]))


def search_file(target):
    os.chdir(os.curdir)

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(target)
            os.chdir(os.pardir)

# start_dir = input('目录：')
target = input('文件：')
search_file(target)