# -*- coding: cp1251 -*-
# ������ �������� �����
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
#2. buld SET of used cards
uc_file=open('C:\\Share_transport\\autoscript\\usedcard_.csv')
uc_text=uc_file.read()
uc_ls=uc_text.split('\n')
UC=set(uc_ls)
print (len(UC))
UC.discard('')
print (len(UC))

logfile = open('settle_log.txt','w')
logfile.write( '����� ������, �� �� �����������: '+str(len(UC-RC))+'\n')
L=list(UC-RC)
L.sort()
for n in L:
  logfile.write(n+'\n')
logfile.write( '����� ��������� �� �������� �����, �� �� ������ � ���: '+str(len(RC-UC))+'\n')
M=list(RC-UC)
M.sort()
for n in M:
  logfile.write(n+'\n')

print (' ����������� � settle_log.txt')



                        