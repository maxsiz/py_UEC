# -*- coding: cp1251 -*-
# ������ ���������� ������� ���������� �� ����� � r6
import subprocess as sp
import fnmatch 
import os
import sys
#2. buld SET of identifyed cards
bc_root_folder=r"C:\Share_transport\LINK\MINSOC\R6"
card = int(input('����� �����:'))
tree = os.walk(bc_root_folder) #������ ����� � ������ � �������-���������� 
for d in tree:  
  for f in d[2]:
    #print (os.path.join(d[0],f)) #������ ������ � ������ �����
    if fnmatch.fnmatch(f, 'r6_*.csv'): #������ ������ �� ����� - r6
       cur_file=open(os.path.join(d[0],f)) #��������� ��������� ����
       cur_file_text = cur_file.read()
       cur_file_ls = cur_file_text.split('\n') #��������� �� ��������� ������
       for s in cur_file_ls: #���� �� ������ ������
         cur_str = s.split(';')
         if len(cur_str[0])>4:  #�������� ������ ������
            try:
              #print (card, d[2], cur_str[0:])
              if int(cur_str[0])==card:
                  print (card, f, cur_str[1:])
            except:
              print ('������ � �����: ',os.path.join(d[0],f))


                        