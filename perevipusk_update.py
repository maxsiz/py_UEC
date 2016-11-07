# -*- coding: cp1251 -*-
# Скрипт собирает по всем файлам перевыпусков информацию и пишет её в один файл  perevipusk.csv
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
#lc_root_folder=r"C:\Share_transport\LINK\nko"
lc_root_folder=os.getcwd()
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
LC=set()#создаем пустое ммножество
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #список файлов с полным путем
    if fnmatch.fnmatch(f, 'RegisterPersonTransfers_*.csv'): #фильтр файлов по маске - файл перевыпусков
       cur_file=open(os.path.join(d[0],f)) #открываем отобраный файл
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #разделяем на отдельные строки
       for s in cur_file_ls: #цикл по каждой строке
         cur_str = s.split(';')
         if len(cur_str)>1:  #отсекаем пустые строки
            try:
              if len(cur_str[11])==19: #проверка длины поля
                 LC.add(cur_str[11]+';'+cur_str[12]+'\n') #добавление элемента во множество 
            except:
              print ('Ошибка в файле: ',os.path.join(d[0],f))
LC.discard('')
#print(LC)
lc_ls=list(LC)
lc_ls.sort()
logfile = open('perevipusk.csv','w')
logfile.writelines( lc_ls)
print ('Список перевыпущеных карт обновлен: '+str(len(lc_ls)))



                        