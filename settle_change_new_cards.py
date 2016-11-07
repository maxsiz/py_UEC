# -*- coding: cp1251 -*-
# ��� ������ ����� ���� �� ������
# usage: settle_canhge_new_cards file2 file3 file4
# !!!!!!!!!!!!��� file1-���� � �������� ����,�������� �����, �� �� ����������� - �������������� (���� ����� � ������) �� ������������.
# file2 - ���� � -�������������! �������������� �����;������ ����� (���� ���� � ������, ����������� ";")
# file3 - ������ ������������, � ������ ����� ������� �������
# file4 - ������� ������ ���������� ��� ������ 
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
import subprocess as sp
import fnmatch 
import os
import sys
#������� ������ ����������  �� ��������� ������, ���� �� �������
if len(sys.argv)==4:
   #file1 = sys.argv[1]
   file2 = sys.argv[1]
   file3 = sys.argv[2]
   file4 = sys.argv[3]
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: settle_canhge_new_cards.py file2 file3 file4')
   sys.exit
#1. first buld list of cards file1
used_cards_ls =[card.split(';')[4] for card in open(file3)]
UC = set(used_cards_ls)
UC.discard('')
print ('Set of used card ', len(UC), ' is builded from ', len(used_cards_ls))
charged_cards_ls =[card.split(';')[4] for card in open(file4)]
CHC = set(charged_cards_ls)
CHC.discard('')
print ('Set of charged card ', len(CHC), ' is builded from ', len(charged_cards_ls))
#charged_cards_ls = [charge_card.split(';')[4] for charge_card in open(file4)]
card_ls = list(UC-CHC)
#card_ls=[card.rstrip() for card in open(file1)]
print ('List of uncharged cards is builded: ', len(card_ls))
#print (card_ls)
#2. buld 
exch_dct = {}
for card in card_ls:#���� �� ������ ����, ������� �� ���������(��������������)
    print (card, end='')
    for exch_str in open(file2):#���� �� ����� ������������ ������������ ��� ���������� �������
        #print (exch_str.rstrip())
        if  int(card) == int(exch_str.split(';')[0]) and int(exch_str.split(';')[0]) > int(exch_str.split(';')[1]):
            exch_dct[exch_str.split(';')[0]]=exch_str.split(';')[1].rstrip()
            print(' -added with ',exch_str.split(';')[1].rstrip())
            break 
        elif int(card)== int(exch_str.split(';')[1]) and int(exch_str.split(';')[1]) > int(exch_str.split(';')[0]):
            exch_dct[exch_str.split(';')[1]]=exch_str.split(';')[0].rstrip()
            print(' -added with ',exch_str.split(';')[0].rstrip())
            break
    else:
        print ('-no match')   
        #print(exch_str.split(';')[0])
print ('����� � ������� ��������� ', len(exch_dct))
#������ ��������� �������  ����� ����� �� ������ ��� file3, �� ������� ��������, ��� "������ �����" ��������� �� ������� �����
#print (exch_dct.values(), len(exch_dct.values()))
not_charged_ls =[]
for old_card in exch_dct.values():#���� �� ��������� �������             
    if  old_card in CHC: #�������� �� ��������� �� ��������� ����������� ����
        print (old_card, ' is charged - OK') 
    else:                        
        not_charged_ls.add(old_card)
j=0
if  len(not_charged_ls)==0: #if all cards are charged, do replace
    print ('Replacing in ', file3,' ...')
    res_file = open(file3+'_new','w') #����� ����
    res_file.write('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT\n')
    for f3_st in open(file3):  #���� �� ����� ������� ������������
        #���� � ������� ������ ����� ������������ ���� "�����" �����, �� � ����� �������� �� ������
        if  f3_st.split(';')[4] in exch_dct.keys():
            res_file.write(f3_st.replace(f3_st.split(';')[4], exch_dct.get(f3_st.split(';')[4])))
            j +=1
        else:
            res_file.write(f3_st)
    print ('Done... ',str(j),' ',res_file.name)
else:
    print (not_charged_ls, ' list of not charged OLD cards in current month')
                                             
                        