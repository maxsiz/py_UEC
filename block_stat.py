# -*- coding: cp1251 -*-
# Скрипт показывает историю блокировки по карте в r6
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
blocked_ls=[]
unblocked_ls=[]
bc_root_folder=r"C:\Share_transport\LINK\MINSOC\R6"
tree = os.walk(bc_root_folder) #дерево папок и файлов в объекте-генераторе 
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #список файлов с полным путем
    if fnmatch.fnmatch(f, 'r6_*.csv'): #фильтр файлов по маске - r6
       cur_file=open(os.path.join(d[0],f)) #открываем отобраный файл
       #cur_file_text = cur_file.read()
       #cur_file_ls = cur_file_text.split('\n') #разделяем на отдельные строки
       cur_file_ls = [cur_str.split(';')[0] for cur_str in cur_file if cur_str.split(';')[3]=='0']
       for s in cur_file_ls: #цикл по каждой строке
         #cur_str = s.split(';')
           if  len(s)>7:  #отсекаем пустые строки
               blocked_ls.append(s)
                # unblocked_ls.append(cur_str[0])  

print ('Заблокировано карт', len(blocked_ls))
print ('Разаблокировано карт', len(unblocked_ls))                    
#if int(cur_str.split(';')[3])==0

                        