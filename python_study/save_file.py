#-*- coding : utf-8 -*-
# coding: utf-8
# pickle模块 学习文件
import pickle
my_list = [123,'46356463',[131,123]]
pickle_file = open('my_list.txt','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()