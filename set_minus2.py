# -*- coding: cp1251 -*-
# Скрипт проверки активных карт на предмет их включения в r1
import subprocess as sp
import fnmatch 
import os
import sys
res_file4 = open('from_perevip.txt', 'w') #новый файл реестра пополнений
f22=open('x1.csv')
f22_ls=[card.rstrip('\n') for card in f22]
rc_file=open('perevipusk.csv')
rc_ls =[cardsper.split(';')[0] for cardsper in rc_file]
print (rc_ls)
for str1 in f22_ls:
    print (str1)
    if  str1 in rc_ls:
        res_file4.write(str1+'\n')
        print (' Найдена в перевыпусках. подробности в from_perevip.txt')



                        