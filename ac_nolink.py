# -*- coding: cp1251 -*-
# Скрипт проверки активных карт на предмет их включения в r1
#0-OK (или OK-2 кода присваевается вторая действующая карта)+
#1-Номер присвоен карту необходимо заблокировать+
#2-номер карты был присвоен ранее+
#3-сошлось по СНИЛС не сошлось по ФИО+др-
#4-сошлось по ФИО+др не сошлось по СНИЛС-
#5-Личное дело не идентифицировано-
#6-Перевыпуск карты (присвоен новый номер с даты выдачи)+
# USAGE: ac_nolink.py [card_num]
import subprocess as sp
import fnmatch 
import os
import sys
if  len(sys.argv)==2:
    ac_ls =[]
    ac_ls.append(sys.argv[1])
    mode = 'single'
else:   
    mode = 'list'
    #ac_file=open('C:\\Share_transport\\autoscript\\ac.csv')
    ac_file=open('C:\\Share_transport\\autoscript\\from_r4.csv')
    #ac_file=open('C:\\Share_transport\\autoscript\\usedcard_.csv')
    #ac_file=open('ac.csv')
    #ac_text=ac_file.read()
    #ac_ls=ac_text.split('\n')
    ac_ls=[num.rstrip() for num in ac_file]
    print (len(ac_ls))
    #del ac_ls[ac_ls.index('')]
    print (len(ac_ls)) 
SL = {}.fromkeys(ac_ls,[('-2','UnKnown','UnKnown')])#структура данных для истории статусов карты
#print ('New SL:', SL)
#2. buld SET of linked cards
#lc_root_folder=r"/home/max_siz/Documents/LINK/YAD/MINSOC/R1"
lc_root_folder=r"C:\Share_transport\LINK\MINSOC\R1"
tree = os.walk(lc_root_folder) #дерево папок и файлов в объекте-генераторе 
for d in tree:  
  for f in d[2]:
    #if fnmatch.fnmatch(f, 'Ans_r1_*.csv'): #фильтр файлов по маске - r1
     if fnmatch.fnmatch(f, '*r1_*.csv'): #фильтр файлов по маске - r1
       cur_file=open(os.path.join(d[0],f),'rb') #открываем отобраный файл
       j = 0
       k = 0
       print (f, end='')
       #cur_file_ls = [curr_str.decode('cp1251').rstrip() for curr_str in cur_file]       
       for curr_str in cur_file:
           cur_str_ls = curr_str.decode('cp1251').rstrip().split(';') #цикл по каждой строке
           j +=1
           #print(cur_str_ls,  cur_str_ls[0])
           #if  cur_str_ls[0] in SL: 
           if  f.upper()[:3]=='ANS' and cur_str_ls[0] in SL: 
               cur_str_ls.append(f)
               #cur_str_ls.append(f.split('_')[3])
               #cur_str_ls.extend([f,f.split('_')[3]])
               #print (' for add:',tuple(cur_str_ls), ', SL[n before]:',SL[cur_str_ls[0]], ' SL full before',SL)
               if  SL[cur_str_ls[0]] == [('-2','UnKnown','UnKnown')]:
                   SL[cur_str_ls[0]] = list()
                   SL[cur_str_ls[0]].append(tuple(cur_str_ls[1:]))
               else:
                   SL[cur_str_ls[0]].append(tuple(cur_str_ls[1:]))
               #print (' SL[new]:',SL[cur_str_ls[0]])
               #print ('SL full ',SL)
               k +=1
           if  f.upper()[:3]=='R1_' and cur_str_ls[5] in SL: 
               #print (cur_str_ls,f)
               cur_str_ls.append(f)
               cur_str_ls = cur_str_ls[5:]
               if  SL[cur_str_ls[0]] == [('-2','UnKnown','UnKnown')]:
                   SL[cur_str_ls[0]] = list()
                   SL[cur_str_ls[0]].append(tuple(cur_str_ls))
               else:
                   SL[cur_str_ls[0]].append(tuple(cur_str_ls))
               k +=1
       print ('..... обработано ', str(j), ', добавлено в словарь: ', str(k))
#logfile = open('log_nolink.txt','w')
print ('Анализ карт: ',len(SL))
#if len(SL) < 100: print(SL)
#второй проход - поиск незавершенных
i = 0
unlink = []
for cur_num_str in SL:#цикл по ключам словаря
    #print (cur_num_str)
    for state_str in SL[cur_num_str]:
        if  mode =='single':
            print (state_str)
        else:
            if  int(state_str[0]) in [0,1,2,6]:#подтвержден 
                #SL.pop(cur_num_str)
                #print (cur_num_str, state_str[2])  
                break
    else:
        i +=1
        unlink.append(cur_num_str+'\n') 
        #print (cur_num_str)
        #print ('......... ', state_str)
unlink.sort()
#print(unlink)
if  mode != 'single':
    print ('Неподтвержденных карт (unlinked.csv): ',str(i))
    logfile = open('unlinked.csv','w')
    logfile.writelines( unlink)
else:
    logfile = open('unlinked.csv','w')
    for state_str in SL[cur_num_str]:
        logfile.write(str(state_str)+'\n') 

#if len(SL) < 100: print(SL)

                        