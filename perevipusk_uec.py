# -*- coding: cp1251 -*-
# Скрипт собирает по всем файлам перевыпусков uec -лежат  в  папках с р1 и пишет её в один файл  perevipusk_uec.csv
import subprocess as sp
import fnmatch 
import os
import sys
#2. 
lc_root_folder=r"/home/max_siz/Documents/LINK/YAD/MINSOC/R1"
#lc_root_folder=os.getcwd()
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
LC=set()#создаем пустое ммножество
all_card_ls = []
for d in tree:  
  for f in d[2]:
      #print (os.path.join(d[0],f)) #список файлов с полным путем
      if  fnmatch.fnmatch(f, 'uectp*.csv'): #фильтр файлов по маске - файл перевыпусков уэк
          print ('Working with ', os.path.join(d[0],f) + ' ... ', end='')
          cur_file=open(os.path.join(d[0],f), encoding='cp1251') #открываем отобраный файл
          cur_card_ls = ['9643103883' + cur_str.rstrip().split(';')[0]+';'+ 
                         '9643103883' + cur_str.rstrip().split(';')[2][1:] + '\n' 
                        for cur_str in cur_file if cur_str.rstrip().split(';')[0] != 'NUM']
          print (str(len(cur_card_ls)))
          all_card_ls  = all_card_ls + cur_card_ls
LC = set(all_card_ls)      
LC.discard('')
#print(LC)
lc_ls=list(LC)
lc_ls.sort()
logfile = open('perevipusk_uec.csv','w')
logfile.write('NEWNUM;UECNUM\n')
logfile.writelines(lc_ls)
print ('Список перевыпущеных карт обновлен: '+str(len(lc_ls)))



                        
