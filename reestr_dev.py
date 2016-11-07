# -*- coding: cp1251 -*-
# ���������� ������� ����������
import subprocess as sp
import fnmatch 
import os
import sys
if len(sys.argv)==4:
   file1 = sys.argv[1] #������, ������ �������� ����� ��������� �� �������
   file2 = sys.argv[2] #������ ������
   file3 = sys.argv[2] #������ ������������ ��� ��������
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: reestr_dev.py file1 file2')
   sys.exit
#����� �������� ������ ����� �� ������� �����
cards_file1_ls =[card.split(';')[4] for card in open(file1)]
#����� �������� ������ ���� �� ����� 3 (�����)
cards_file3_ls =[card.split(';')[4] for card in open(file3)]
CF3=set(cards_file3_ls)
CF3.discard('')
print (len(CF3))

res_file = open('file2'+'_new', 'w') #����� ���� ������� ����������
res_file.write ('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT'+'\n')
for str1 in open(file2): #���� �� ������� ����� ������� ����������
    if  str1.split(';')[4] not in cards_file1_ls: #���� ����� ��� � ������ �� ������� ����� , �� ������ ����� � ����� ����
        if  str1.split(';')[4]  in CF3: #������������� ��������, ��� ����� ���� � ������ �� �����3
            res_file.write(str1)

                        