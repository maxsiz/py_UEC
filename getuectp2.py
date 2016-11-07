# -*- coding: cp1251 -*-
# Поиск ранее выданных УЭК
# usage: getuectp.py file1
import subprocess as sp
import fnmatch 
import os
import sys
if  len(sys.argv)==2:
    file1 = sys.argv[1]
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: getuectp.py file1')
   print(sys.argv)
   sys.exit
res_file = open('uectp'+file1, 'w') #итоговый файл
cur_file=open(file1,'rb') #открываем отобраный файл
j = 0
k = 0
#cur_file_ls = [curr_str.decode('cp1251').rstrip() for curr_str in cur_file]       
for curr_str in cur_file:
    j +=1
    cur_str_ls = curr_str.decode('cp1251').rstrip().split(';') #цикл по каждой строке
    for s1 in open(r"C:\Share_transport\UEC\uec_201610.csv"):
        print (file1+' '+str(j)+' '+str(k))
        s1_ls=s1.rstrip().split(';')
        k +=1
        if  (cur_str_ls[4]==s1_ls[4]) or (cur_str_ls[0].upper()+cur_str_ls[1].upper()+cur_str_ls[2].upper()+cur_str_ls[3]==s1_ls[0]+s1_ls[1]+s1_ls[2]+s1_ls[3]):
            res_file.write(cur_str_ls[5]+';'+cur_str_ls[0]+' '+cur_str_ls[1][0]+cur_str_ls[2][0]+';'+s1_ls[8]+'\n')