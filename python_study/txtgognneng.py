#!/usr/bin/python
#-*- coding: UTF-8 -*-


def newtxt():
	name = input('新建文件名:')
	txt = name+'.txt'
	test = open (txt,'w')
	print('''现在写点啥呗，输入'.w'退出并保存 \n''')
	while True:
 		list_write_in = input()
 		if list_write_in != '.w':
 			test.write('%s\n' %list_write_in)
 		else:
 			break
	test.close()


def file_compare(file1,file2):
	f1 = open(file1,encoding= 'utf-8')
	f2 = open(file2,encoding= 'utf-8')
	count = 0 #统计行数
	diff = []# 统计不一样的数据量
	for line1 in f1:
		#print(line1)
		line2 = f2.readline()
		count += 1
		if line1 != line2:
			diff.append(count)
	f1.close()
	f2.close()
	return diff


def do_compare():
	file1 = input('对比文件【1】:')
	file2 = input('对比文件【2】:')
	diff = file_compare(file1,file2)
	if len(diff) == 0:
		print('same')
	else:
		print('有 [%d]处不同' % len(diff))
		for each in diff:
			print('第[%d]行存在差异' % each )
	pass		


def  file_view():
	file_name,line_num = input('你要看啥，要看几行？\n文件名和行数用;（En）分割\n').split(';')
	print('【%s 的前 %s 行】' % (file_name,line_num))
	print('【预览文件内容：】\n')
	the_file = open(file_name,encoding= 'utf-8')
	for  each_line in range(int(line_num)):
		print (the_file.readline(),end = '')
	the_file.close()
	pass


def file_view_ex():

	file_name,line_num = input('你要看啥，要看几行？\n文件名和行数用;（En）分割\n例如[test.txt;12:20]\n').split(';')
	
	if line_num.strip() == ':':
		begin = '1'
		end = '-1'
	
	(begin,end) = line_num.split(':')
	if begin == '':
		begin = '1'
	if end == '':
		end = '-1'
	if begin == '1' and end == '-1':
		prompt = '【全文】:'
	elif begin == '1':
		prompt = '【从开始到第 %s 行】：' % end
	elif end == '-1':
		prompt = '【从第 %s 行到结束】：' % begin
	else:
		prompt = '【从第 %s 行到第 %s 行】:' % (begin,end)
	print('文件[%s]你要看的[%s]在这里：' % (file_name,prompt))

	begin = int (begin) 
	end = int (end)
	lines = end -  begin + 1
	
	the_file = open(file_name, encoding = 'utf-8')
 
	for i in range(begin):
		the_file.readline()
	if lines < 0:
		print(the_file.read())
	else:
		for each_line in range (lines):
			print(the_file.readline(),end = '')

	the_file.close()





def main_menu():


##############start##############
	prompt = '''
	|====新建====.new|
	|====对比====.com|
	|====预览====.see|
	|====退出====.out|
	'''
	command = ['.com','.new','.out','.see']
	see_commend = ['.nom','.ex','.out']
	while True:
		chosen = False
		while not chosen:
			to_do = input(prompt)
			if to_do not in command:
				print('别tm乱输啊，重输:')
			else:
				chosen = True

	if to_do == '.out':
		main_menu()
	if to_do == '.new':
			newtxt()
	if to_do == '.com':
		do_compare()

	if to_do == '.see':
		while True:
			see_lv = False
			while see_lv == False:
				to_see = input('''预览等级:\n普通==>'.nom'\n高级'.ex'\n''')
				if to_see not in see_commend :
					print('别tm乱输啊，重输:')
				else:
					see_lv = True

			if to_see == '.nom':
				file_view()
			if to_see == '.ex':
				file_view_ex()
			if to_see == '.out':
				main_menu()







