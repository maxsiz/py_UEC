# -*- coding: cp1251 -*-
# Скрипт
import subprocess as sp
import fnmatch 
import os
import sys
#1. first buld SET of active cards
ac_file=open('Ans_r4_38_20161102_0080.csv', encoding='cp1251')
ac_ls = [x.rstrip().split(';')[0] for x in ac_file if x.rstrip().split(';')[0] !='NUM']
AC=set(ac_ls)
AC.discard('')
#2. buld SET of linked cards
lc_root_folder=r"/home/max_siz/Documents/LINK/YAD/MINSOC/R1"
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
LC=set()#создаем пустое ммножество
ls=[]
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #список файлов с полным путем
    if fnmatch.fnmatch(f, 'r1_*.csv'): #фильтр файлов по маске - r1
       cur_file=open(os.path.join(d[0],f), encoding='cp1251') #открываем отобраный файл
       temp_ls = [x.rstrip().split(';')[5]+';'+ x.rstrip().split(';')[4] for x in cur_file
                   if x.rstrip().split(';')[4] != 'SNILS'  and len(x.rstrip().split(';')[4])==11
                      and x.rstrip().split(';')[5] in AC
                 ]
       ls = ls + temp_ls
LC = set(ls)
LC.discard('')
ls = list(LC)
ls1=[]

for y in LC:
    temp_ls = list(filter((lambda x: x.rstrip().split(';')[1] == y.rstrip().split(';')[1]), ls))
    temp_ls.sort()
    if  len(temp_ls)==2:
        #print (temp_ls[0].split(';')[0], temp_ls[1].split(';')[0])
        ls1.append(temp_ls[0].split(';')[0]+';'+temp_ls[1].split(';')[0])
        print ('.', end='')
    elif len(temp_ls)==3:
        print (temp_ls[0].split(';')[0],temp_ls[1].split(';')[0],temp_ls[2].split(';')[0])
    elif len(temp_ls)>3:
        print ( len(temp_ls))
    
S1 = set(ls1)
S1.discard('')    
print(len(S1))
ls1 = list(S1)
ls1.sort() 
logfile = open('pair_card','w')
for n in ls1:
  logfile.write(n+'\n')
#print(len(LC))
#filter((lambda x: x > 0), range(-5, 5))



                        
