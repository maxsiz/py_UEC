# -*- coding: cp1251 -*-
# фильтр униальных записей
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

#1. first buld SET of recharged cards
rc_file=open(file1)
rc_ls=[curr_str.rstrip().split(';')[0] for curr_str in rc_file]
print (len(rc_ls))
RC=set(rc_ls)
print (len(RC))
RC.discard('')
print (len(RC))
logfile = open('filtered_'+file1,'w')
L=list(RC)
L.sort()
for n in L:
  logfile.write(n+'\n')
print ('результат '+ 'filtered_'+file1)
