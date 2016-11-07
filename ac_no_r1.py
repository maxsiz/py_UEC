# -*- coding: cp1251 -*-
# ������ �������� �������� ���� �� ������� �� ��������� � r1
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
#2. buld SET of linked cards
lc_root_folder=r"C:\Share_transport\LINK\MINSOC\R1"
#lc_root_folder=r"C:\Share_transport\LINK\MINSOC\���������� �����\20160418"
tree = os.walk(lc_root_folder) #������ ����� � ������ � �������-���������� 
LC=set()#������� ������ ����������
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #������ ������ � ������ �����
    if fnmatch.fnmatch(f, 'r1_*.csv'): #������ ������ �� ����� - r1
       cur_file=open(os.path.join(d[0],f)) #��������� ��������� ����
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #��������� �� ��������� ������
       for s in cur_file_ls: #���� �� ������ ������
         cur_str = s.split(';')
         if len(cur_str)>1:  #�������� ������ ������
            try:
              if len(cur_str[5])==9: #�������� ����� ����
                 LC.add(cur_str[5]) #���������� �������� �� ��������� 
            except:
              print ('������ � �����: ',os.path.join(d[0],f))
logfile = open('log_no_r1.txt','w')
logfile.write( '�������� �����, �� ������������ � ������: '+str(len(AC-LC))+'\n')
for n in AC-LC:
  logfile.write(n+'\n')
print ('�������� �����, �� ������������ � ������: '+str(len(AC-LC))+'\n' + ' ����������� � log_no_r1.txt')



                        