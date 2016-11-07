# -*- coding: cp1251 -*-
# Для замены новых карт на старую
# usage: settle_canhge_new_cards.py file2 file3 file4
# !!!!!!!!!!!!где file1-файл C:\Users\Sizykh\python_example\settle_change_new_cards.pyс номерами карт,котороые ездят, но не пополнялись - перевыпущенные (один номер в строке) НЕ ИСПОЛЬЗУЕТСЯ.
# file2 - файл с -соответствием! перевыпущенная карта;старая карта (одна пара в строке, разделитель ";")
# file3 - реестр перечислений, в котром нужно сделать подмену
# file4 - текущий реестр пополнений для сверки 
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
#/home/max_siz/Documents/LINK/YAD/
import subprocess as sp
import fnmatch 
import os
import sys
uec_tp_ls=[]
res_file = open('uectp.csv', 'w') #итоговый файл

lc_root_folder=r"/home/max_siz/Documents/LINK/YAD/MINSOC/R1"
#lc_root_folder=r"/home/max_siz/python_example"
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
l = 0
uec_ls = [us.decode('cp1251').rstrip() for us in open(r"uec_201610.csv",'rb')]
for d in tree:  
  for f in d[2]:
    #if fnmatch.fnmatch(f, 'Ans_r1_*.csv'): #фильтр файлов по маске - r1
     if fnmatch.fnmatch(f, 'r1_*.csv'): #фильтр файлов по маске - r1
       cur_file=open(os.path.join(d[0],f),'rb') #открываем отобраный файл
       j = 0
       print (f, end='=>')
       x_ls =[ curr_str.decode('cp1251').rstrip().split(';')[5]+';'+s1.split(';')[8] for curr_str in cur_file for s1 in uec_ls if curr_str.decode('cp1251').rstrip().split(';')[4] ==s1.split(';')[4]] 
       print (x_ls)
#cur_file_ls = [curr_str.decode('cp1251').rstrip() for curr_str in cur_file]       
#       for curr_str in cur_file:
#           k = 0
#           j +=1
#           cur_str_ls = curr_str.decode('cp1251').rstrip().split(';') #цикл по каждой строке
#           for s1 in open(r"C:\Share_transport\UEC\uec_201610.csv"):
#               s1_ls=s1.rstrip().split(';')
#               k +=1
#               print (f+' '+str(0)+' '+str(j)+' '+str(k))
#               if  (cur_str_ls[4]==s1_ls[4]) or (cur_str_ls[0].upper()+cur_str_ls[1].upper()+cur_str_ls[2].upper()+cur_str_ls[3]==s1_ls[0]+s1_ls[1]+s1_ls[2]+s1_ls[3]):
#                   res_file.write(cur_str_ls[5]+';'+cur_str_ls[0]+' '+cur_str_ls[1][0]+cur_str_ls[2][0]+';'+s1_ls[8]+'\n')
