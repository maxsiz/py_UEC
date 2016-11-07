# -*- coding: cp1251 -*-
# ������ �������� �� ���� ������ ������������ ���������� � ����� � � ���� ����  perevipusk.csv
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
#lc_root_folder=r"C:\Share_transport\LINK\nko"
lc_root_folder=os.getcwd()
tree = os.walk(lc_root_folder) #������ ����� � ������ � �������-���������� 
LC=set()#������� ������ ����������
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #������ ������ � ������ �����
    if fnmatch.fnmatch(f, 'RegisterPersonTransfers_*.csv'): #������ ������ �� ����� - ���� ������������
       cur_file=open(os.path.join(d[0],f)) #��������� ��������� ����
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #��������� �� ��������� ������
       for s in cur_file_ls: #���� �� ������ ������
         cur_str = s.split(';')
         if len(cur_str)>1:  #�������� ������ ������
            try:
              if len(cur_str[11])==19: #�������� ����� ����
                 LC.add(cur_str[11]+';'+cur_str[12]+'\n') #���������� �������� �� ��������� 
            except:
              print ('������ � �����: ',os.path.join(d[0],f))
LC.discard('')
#print(LC)
lc_ls=list(LC)
lc_ls.sort()
logfile = open('perevipusk.csv','w')
logfile.writelines( lc_ls)
print ('������ ������������� ���� ��������: '+str(len(lc_ls)))



                        