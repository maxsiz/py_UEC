# -*- coding: cp1251 -*-
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
#/home/max_siz/Documents/LINK/YAD/
#!!!��� �� ��������������, ����������!
import subprocess as sp
import fnmatch 
import os
import sys
import math
import datetime
def get_sum_card_and_carr (card_num,carrier_code):
    """
    card_num - transport crad number
    carrier_code  - subj
    ����� �� ����� � �����������
    """
    res = 0
    if  len(cardcarrier_sum)>0:
        res = cardcarrier_sum[carrier_code+'_'+card_num]    
    else:
        if  card_num not in card_change_sl and card_num not in card_change_sl.values():
            res = math.trunc(int(r4_cardcarrier_sum[carrier_code+'_'+card_num])
                                      /card_trip_count_sl[card_num]
                                       *150*100#/100*100
                                      )/100 #c���� �� �����                            
        else: #���� � ������������
            res = math.trunc(int(r4_cardcarrier_sum[carrier_code+'_'+card_num])
                             #round(int(r4_cardcarrier_sum[carrier_code+'_'+card_num])
                                      /card_trip_count_sl[card_num]
                                       *150*100#100*100/2
                                      )//2/100
    return res
#*****************************************************************************************
print (sys.argv)
if len(sys.argv)==3:
   file1 = sys.argv[1]#Ans_r4*
   file2 = sys.argv[2]#�����������: �����;������
   file3 = ''
elif len(sys.argv)==4:
   file1 = sys.argv[1]#Ans_r4*
   file2 = sys.argv[2]#�����������: �����;������
   file3 = sys.argv[3]#��������� ���� ������������  
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: r4_to_carrier.py file1 file2')
   sys.exit
#������ ������� � ������� �� ������� �������������� ����
print ('������ ������� � ������� �� ������� �������������� ���� - .. ', end='')
card_trip_count_sl = {data.rstrip().split(';')[0]:0  for data in open(file1, encoding='cp1251') 
                if len(data.rstrip().split(';')[0])==9 
                    #and int(data.rstrip().split(';')[4])==0
                     }
print ('ok '+ str(len(card_trip_count_sl)))
#������ ������� � ������� �� ������� �������������� ����
print ('������ ������� � ������� �� ������� �������������� ���� - .. ', end='')
card_change_sl = {data.rstrip().split(';')[0][10:]:data.rstrip().split(';')[1][10:]  
                 for data in open(file2, encoding='cp1251')}
print(card_change_sl)
#R4 - ������ ������� �� ����� � ������� "����������_�����"
print ('R4 - ������ ������� � ������� �� "����������_�����" - .. ', end='')
r4_cardcarrier_sum = {cs.rstrip().split(';')[1]+'_'
                      +cs.rstrip().split(';')[0]:int(cs.rstrip().split(';')[2]) 
                       for cs in open(file1, encoding='cp1251') if len(cs.rstrip().split(';')[0])==9}
print ('ok '+ str(len(r4_cardcarrier_sum)))
#���� �������� ������ ��������, �� ��� ���� ����. ������ �������
if  file3 !='' :
    print(file3)
    print ('������ ������� � ������� �� "����������_�����" - .. ', end='')
    cardcarrier_sum = {cs.rstrip().split(';')[0]+'_'
                       +cs.rstrip().split(';')[4][10:]:int(cs.rstrip().split(';')[6]) 
                       for cs in open(file3)  if len(cs.rstrip().split(';')[4][10:])==9}
    print ('ok '+ str(len(cardcarrier_sum)))
else:
    cardcarrier_sum ={}
#�������� ������� ����� ����������� ������� �� ������
all_trips = 0
for x in open(file1,encoding='cp1251'):
    if  x.rstrip().split(';')[0] in card_trip_count_sl.keys():
        card_trip_count_sl[x.rstrip().split(';')[0]]  += int(x.rstrip().split(';')[2])
        all_trips +=int(x.rstrip().split(';')[2])
print ('������� ��������- ', str(all_trips)) 
#������ ��������� ������������ �� ������
ans_r4_f = open(file1,encoding='cp1251')
carrier_gorod_ls = [curr_str.rstrip().split(';')[1] for curr_str in ans_r4_f 
                   if len(curr_str.rstrip().split(';')[0])==9 
                      and  int(curr_str.rstrip().split(';')[4])==0 
                      and curr_str.rstrip().split(';')[7]=='0']
carrier_gorod_set =set(carrier_gorod_ls)
carrier_gorod_set.discard('')
print (carrier_gorod_set)
ans_r4_f.close()
for carrier in carrier_gorod_set:
    print ('Working with '+carrier+'...', end='')
    ans_r4_f = open(file1, encoding='cp1251')#���� ��� ����������
    carrier_tickets = [cur_str.rstrip().split(';')[0]+';'#����� �����
                       +cur_str.rstrip().split(';')[2]+';'#���-�� ������� � �����������
                       +str(card_trip_count_sl[cur_str.rstrip().split(';')[0]]# ����� ���-�� ������� �� �����
                         if int(card_trip_count_sl[cur_str.rstrip().split(';')[0]])<=30 #�������� 30 �������
                         else 30)+';'
                       +str(round(int(cur_str.rstrip().split(';')[2])
                                  /card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100,2))+';' #���� � %
                       +str(get_sum_card_and_carr(cur_str.rstrip().split(';')[0],carrier)
                           ).replace('.',',')+'\n'    
                      for cur_str in ans_r4_f if cur_str.rstrip().split(';')[1]==carrier #������ ����������
                                                # and int(cur_str.rstrip().split(';')[4])==0 # ������ ������������
                      ] 
    now_date = datetime.date.today()
    cur_carrier_file=open(carrier+'_raschet_g_'
                          +str(now_date.year)
                          +str(now_date.month).rjust(2,'0')
                          +str(now_date.day).rjust(2,'0')
                          +'.csv','w')
    cur_carrier_file.writelines(carrier_tickets)
    print ('ok '+ str(len(carrier_tickets)))
ans_r4_f.close()
#������ ��������� ������������ �� ���������
ans_r4_f = open(file1,encoding='cp1251')
carrier_prigorod_ls = [curr_str.rstrip().split(';')[1] for curr_str in ans_r4_f
                       if len(curr_str.rstrip().split(';')[0])==9 
                         # and  int(curr_str.rstrip().split(';')[4])==0 # ������ ������������
                          and curr_str.rstrip().split(';')[7]=='1']#prigorod
carrier_prigorod_set =set(carrier_prigorod_ls)
carrier_prigorod_set.discard('')
print (carrier_prigorod_set)
ans_r4_f.close()
for carrier in carrier_prigorod_set:
    print ('Working with '+carrier+'...', end='')
    ans_r4_f = open(file1, encoding='cp1251')#���� ��� ����������
    carrier_tickets = [cur_str.rstrip().split(';')[0]+';'#����� �����
                       +cur_str.rstrip().split(';')[2]+';'#���-�� ������� � �����������
                       +str(card_trip_count_sl[cur_str.rstrip().split(';')[0]]# ����� ���-�� ������� �� �����
                         if int(card_trip_count_sl[cur_str.rstrip().split(';')[0]])<=30 #�������� 30 �������

                         else 30)+';'
                       +str(round(int(cur_str.rstrip().split(';')[2])
                                  /card_trip_count_sl[cur_str.rstrip().split(';')[0]]*100,2))+';' #���� � %
                       +str(get_sum_card_and_carr(cur_str.rstrip().split(';')[0],carrier)
                           ).replace('.',',')+'\n'    
                      for cur_str in ans_r4_f if cur_str.rstrip().split(';')[1]==carrier #������ ����������
                                                # and int(cur_str.rstrip().split(';')[4])==0 # ������ ������������
                      ] 
    cur_carrier_file=open(carrier+'_raschet_p_'
                          +str(now_date.year)
                          +str(now_date.month).rjust(2,'0')
                          +str(now_date.day).rjust(2,'0')
                          +'.csv','w')
    cur_carrier_file.writelines(carrier_tickets)
    print ('ok '+ str(len(carrier_tickets)))
ans_r4_f.close()
