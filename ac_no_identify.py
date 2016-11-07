# -*- coding: cp1251 -*-
# Скрипт проверки активных карт на предмет их включения в r1
import subprocess as sp
import fnmatch 
import os
import sys
#1. first buld SET of active cards
ac_file=open('C:\\Share_transport\\autoscript\\ac.csv')
ac_text=ac_file.read()
ac_ls=ac_text.split('\n')
AC=set(ac_ls)
AC.discard('')
#2. buld SET of identifyed cards
lc_root_folder=r"C:\Share_transport\LINK\nko"
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
LC=set()#создаем пустое ммножество
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #список файлов с полным путем
    if fnmatch.fnmatch(f, 'RegisterPerson_*.csv'): #фильтр файлов по маске - r1
       cur_file=open(os.path.join(d[0],f)) #открываем отобраный файл
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #разделяем на отдельные строки
       for s in cur_file_ls: #цикл по каждой строке
         cur_str = s.split(';')
         if len(cur_str)>1:  #отсекаем пустые строки
            try:
              if len(cur_str[10])==19: #проверка длины поля
                 LC.add(cur_str[10][10:]) #добавление элемента во множество 
            except:
              print ('Ошибка в файле: ',os.path.join(d[0],f))
logfile = open('log_no_identify.txt','w')
logfile.write( 'Активные карты, которых нет в реестрах идентификации: '+str(len(AC-LC))+'\n')
for n in AC-LC:
  logfile.write(n+'\n')
print ('Активные карты, которых нет в реестрах идентификации: '+str(len(AC-LC))+'\n' + ' подробности в log_no_identify.txt')



                        