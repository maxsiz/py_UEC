# -*- coding: cp1251 -*-
# ������ ���������� ������� ���������� �� ����� � r6
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
blocked_ls=[]
unblocked_ls=[]
bc_root_folder=r"C:\Share_transport\LINK\MINSOC\R6"
tree = os.walk(bc_root_folder) #������ ����� � ������ � �������-���������� 
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #������ ������ � ������ �����
    if fnmatch.fnmatch(f, 'r6_*.csv'): #������ ������ �� ����� - r6
       cur_file=open(os.path.join(d[0],f)) #��������� ��������� ����
       #cur_file_text = cur_file.read()
       #cur_file_ls = cur_file_text.split('\n') #��������� �� ��������� ������
       cur_file_ls = [cur_str.split(';')[0] for cur_str in cur_file if cur_str.split(';')[3]=='0']
       for s in cur_file_ls: #���� �� ������ ������
         #cur_str = s.split(';')
           if  len(s)>7:  #�������� ������ ������
               blocked_ls.append(s)
                # unblocked_ls.append(cur_str[0])  

print ('������������� ����', len(blocked_ls))
print ('��������������� ����', len(unblocked_ls))                    
#if int(cur_str.split(';')[3])==0

                        