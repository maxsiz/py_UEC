# -*- coding: cp1251 -*-
# ������ �������� �������� ���� �� ������� �� ��������� � r1
import subprocess as sp
import fnmatch 
import os
import sys
#1. first buld SET of recharged cards
rc_file=open('C:\\Share_transport\\autoscript\\recharged_.csv')
rc_text=rc_file.read()
rc_ls=rc_text.split('\n')
RC=set(rc_ls)
print (len(RC))
RC.discard('')
print (len(RC))
#2. buld SET of tested cards
tc_file=open('C:\\Share_transport\\autoscript\\tempcard_.csv')
tc_text=tc_file.read()
tc_ls=tc_text.split('\n')
TC=set(tc_ls)
print (len(TC))
TC.discard('')
print (len(TC))

logfile = open('tempcard_log.txt','w')
logfile.write( '�� ����������� �� �������� �����: '+str(len(TC-RC))+'\n')
for n in TC-RC:
  logfile.write(n+'\n')
#logfile.write( '����� ��������� �� �������� �����, �� �� ������ � ���: '+str(len(RC-UC))+'\n')
#for n in RC-UC:
#  logfile.write(n+'\n')

print (' ����������� � tempcard_log.txt')



                        