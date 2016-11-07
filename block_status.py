# -*- coding: cp1251 -*-
# Скрипт показывает историю блокировки по карте в r6
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
bc_root_folder=r"C:\Share_transport\LINK\MINSOC\R6"
card = int(input('Номер карты:'))
tree = os.walk(bc_root_folder) #дерево папок и файлов в объекте-генераторе 
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #список файлов с полным путем
    if fnmatch.fnmatch(f, 'r6_*.csv'): #фильтр файлов по маске - r6
       cur_file=open(os.path.join(d[0],f)) #открываем отобраный файл
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #разделяем на отдельные строки
       for s in cur_file_ls: #цикл по каждой строке
         cur_str = s.split(';')
         if len(cur_str[0])>4:  #отсекаем пустые строки
            try:
              #print (card, d[2], cur_str[0:])
              if int(cur_str[0])==card:
                  print (card, f, cur_str[1:])
            except:
              print ('Ошибка в файле: ',os.path.join(d[0],f))


                        