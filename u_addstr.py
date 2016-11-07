# -*- coding: cp1251 -*-
# разделение реестра пополнений
import subprocess as sp
import fnmatch 
import os
import sys
if len(sys.argv)==2:
   file1 = sys.argv[1] #файл на входе
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: u_addstr.py file1')
   sys.exit
#нужно получить список пкарт из первого файла
cards_file1_ls =[card.rstrip('\n') for card in open(file1)]

res_file = open(file1+'_new', 'w') #новый файл реестра пополнений
for str1 in cards_file1_ls: #цикл по списку
    res_file.write("'0"+str1+"'," + '\n')

                        