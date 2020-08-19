# 异常处理学习文件
# try 语句

file_name = input('name:')
f = open(file_name)
print('all txt:')
for each_line in f:
    print(each_line)
# try:
#     检测范围
# except Exception[as reason]:
#     异常后代码
# finally:
#     无论如何都会执行的代码