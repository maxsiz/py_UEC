# -*- coding: cp1251 -*-
# фильтр записей первого файла по уникальным картам из второго файла
import subprocess as sp
import fnmatch 
import os
import sys
if len(sys.argv)==3:
   file1 = sys.argv[1] #файл на входе
   file2 = sys.argv[2] #файл c условием фильтра (карты)
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: ', sys.argv[0], ' file1 file2')
   sys.exit
#1. Prepare result file
resfile = open(sys.argv[2].split('.')[0]+'_filter.'+sys.argv[2].split('.')[1],'w')
#buld SET of source cards
source_ls=[curr_str.rstrip().split(';')[4] for curr_str in open(file2)]
print (len(source_ls))
source_set=set(source_ls)
source_set.discard('')
print (len(source_set))
#build result set
res_ls=[curr_str for curr_str in open(file1) if curr_str.rstrip().split(';')[4] in source_set]
print('Result:', len(res_ls))
res_ls.sort()
resfile.writelines(res_ls)

