# -*- coding: cp1251 -*-
# ��� ������ ����� ���� �� ������
# usage: settle_test_final.py file1 file2
# file1 - �������� ������ ����������.
# file2 - �������� ������ ������������
import subprocess as sp
import fnmatch 
import os
import sys
#������� ������ ����������  �� ��������� ������, ���� �� �������
if len(sys.argv)==3:
   file1 = sys.argv[1]
   file2 = sys.argv[2]
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: settle_test_final.py file1 file2')
   sys.exit
#1. first buld list of cards file1
used_cards_ls =[card.split(';')[4] for card in open(file2)]
UC = set(used_cards_ls)
UC.discard('')
print ('Set of used card ', len(UC), ' is builded from ', len(UC))
charged_cards_ls =[card.split(';')[4] for card in open(file1)]
CHC = set(charged_cards_ls)
CHC.discard('')
print ('Set of charged card ', len(CHC), ' is builded from ', len(CHC))
#charged_cards_ls = [charge_card.split(';')[4] for charge_card in open(file4)]
print ('�������� ����� ����������',len(UC-CHC))
print ('���������� ����� ��������',len(CHC-UC))
                        