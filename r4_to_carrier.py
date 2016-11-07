# -*- coding: cp1251 -*-
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
#/home/max_siz/Documents/LINK/YAD/
#!!!код не структурирован, переделать!
import subprocess as sp
import fnmatch 
import os
import sys
import math
import datetime
if len(sys.argv)==2:
   file1 = sys.argv[1]#Ans_r4*
   #file2 = sys.argv[2]#for carrier
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: r4_to_carrier.py file1 file2')
   sys.exit
#строим словарь с ключами из номеров подтвержденных карт
print ('строим словарь с ключами из номеров подтвержденных карт - .. ', end='')
card_trip_count_sl = {data.rstrip().split(';')[0]:0  for data in open(file1, encoding='cp1251') if len(data.rstrip().split(';')[0])==9 and int(data.rstrip().split(';')[4])==0}
#del card_trip_count_sl['']
print ('ok '+ str(len(card_trip_count_sl)))
#заполним словарь общим количеством поездок по картам
all_trips = 0
for x in open(file1,encoding='cp1251'):
    if  x.rstrip().split(';')[0] in card_trip_count_sl.keys():
        card_trip_count_sl[x.rstrip().split(';')[0]]  += int(x.rstrip().split(';')[2])
        all_trips +=int(x.rstrip().split(';')[2])
print ('Словарь заполнен- ', str(all_trips)) 
#строим множество перевозчиков по городу
ans_r4_f = open(file1,encoding='cp1251')
carrier_gorod_ls = [curr_str.rstrip().split(';')[1] for curr_str in ans_r4_f if len(curr_str.rstrip().split(';')[0])==9 and  int(curr_str.rstrip().split(';')[4])==0 and curr_str.rstrip().split(';')[7]=='0']
carrier_gorod_set =set(carrier_gorod_ls)
carrier_gorod_set.discard('')
print (carrier_gorod_set)
ans_r4_f.close()
for carrier in carrier_gorod_set:
    print ('Do with '+carrier+'\n')
    ans_r4_f = open(file1, encoding='cp1251')#файл для разделения
    carrier_tickets = [cur_str.rstrip().split(';')[0]+';'+cur_str.rstrip().split(';')[2]+';'+ \
        str(card_trip_count_sl[cur_str.rstrip().split(';')[0]] if int(card_trip_count_sl[cur_str.rstrip().split(';')[0]])<=30 else 30)+';'+ \
        str(round(int(cur_str.rstrip().split(';')[2])/card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100,2))+';'+\
        str(math.trunc(int(cur_str.rstrip().split(';')[2])/card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100*150/100*100)/100)+'\n'\
    
        for cur_str in ans_r4_f if cur_str.rstrip().split(';')[1]==carrier and int(cur_str.rstrip().split(';')[4])==0] 
    now_date = datetime.date.today()
    cur_carrier_file=open(carrier+'_raschet_g_'+str(now_date.year)+str(now_date.month).rjust(2,'0')+str(now_date.day).rjust(2,'0')+'.csv','w')
    cur_carrier_file.writelines(carrier_tickets)
ans_r4_f.close()
#строим множество перевозчиков по пригороду
ans_r4_f = open(file1,encoding='cp1251')
carrier_prigorod_ls = [curr_str.rstrip().split(';')[1] for curr_str in ans_r4_f if len(curr_str.rstrip().split(';')[0])==9 and  int(curr_str.rstrip().split(';')[4])==0 and curr_str.rstrip().split(';')[7]=='1']
carrier_prigorod_set =set(carrier_prigorod_ls)
carrier_prigorod_set.discard('')
print (carrier_prigorod_set)
ans_r4_f.close()
for carrier in carrier_prigorod_set:
    print ('Do with '+carrier+'\n')
    ans_r4_f = open(file1, encoding='cp1251')#файл для разделения
    carrier_tickets = [cur_str.rstrip().split(';')[0]+';'+cur_str.rstrip().split(';')[2]+';'+ \
        str(card_trip_count_sl[cur_str.rstrip().split(';')[0]] if int(card_trip_count_sl[cur_str.rstrip().split(';')[0]])<=30 else 30)+';'+ \
        str(round(int(cur_str.rstrip().split(';')[2])/card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100,2))+';'+\
        str(math.trunc(int(cur_str.rstrip().split(';')[2])/card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100*150/100*100)/100)+'\n'\
    
        for cur_str in ans_r4_f if cur_str.rstrip().split(';')[1]==carrier and int(cur_str.rstrip().split(';')[4])==0] 
    cur_carrier_file=open(carrier+'_raschet_p_'+str(now_date.year)+str(now_date.month).rjust(2,'0')+str(now_date.day).rjust(2,'0')+'.csv','w')
    cur_carrier_file.writelines(carrier_tickets)
ans_r4_f.close()
