# -*- coding: cp1251 -*-
# ��� ������ ����� ���� �� ������
# usage: settle_canhge_new_cards.py file2 file3 file4
# !!!!!!!!!!!!��� file1-���� C:\Users\Sizykh\python_example\settle_change_new_cards.py� �������� ����,�������� �����, �� �� ����������� - �������������� (���� ����� � ������) �� ������������.
# file2 - ���� � -�������������! �������������� �����;������ ����� (���� ���� � ������, ����������� ";")
# file3 - ������ ������������, � ������ ����� ������� �������
# file4 - ������� ������ ���������� ��� ������ 
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
import subprocess as sp
import fnmatch 
import os
import sys
uec_tp_ls=[]
res_file = open('uectp.csv', 'w') #�������� ����

lc_root_folder=r"C:\Share_transport\LINK\MINSOC\R1"
tree = os.walk(lc_root_folder) #������ ����� � ������ � �������-���������� 
l = 0
for d in tree:  
  for f in d[2]:
    #if fnmatch.fnmatch(f, 'Ans_r1_*.csv'): #������ ������ �� ����� - r1
     if fnmatch.fnmatch(f, 'r1_38_*.csv'): #������ ������ �� ����� - r1
       cur_file=open(os.path.join(d[0],f),'rb') #��������� ��������� ����
       j = 0
       print (f, end='')
       #cur_file_ls = [curr_str.decode('cp1251').rstrip() for curr_str in cur_file]       
       for curr_str in cur_file:
           k = 0
           j +=1
           cur_str_ls = curr_str.decode('cp1251').rstrip().split(';') #���� �� ������ ������
           for s1 in open(r"C:\Share_transport\UEC\uec_201610.csv"):
               s1_ls=s1.rstrip().split(';')
               k +=1
               print (f+' '+str(0)+' '+str(j)+' '+str(k))
               if  (cur_str_ls[4]==s1_ls[4]) or (cur_str_ls[0].upper()+cur_str_ls[1].upper()+cur_str_ls[2].upper()+cur_str_ls[3]==s1_ls[0]+s1_ls[1]+s1_ls[2]+s1_ls[3]):
                   res_file.write(cur_str_ls[5]+';'+cur_str_ls[0]+' '+cur_str_ls[1][0]+cur_str_ls[2][0]+';'+s1_ls[8]+'\n')